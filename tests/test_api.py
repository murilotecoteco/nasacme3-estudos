import requests
import pytest

from nasacme_estudos import api


class FakeResponse:
    def __init__(self, payload=None, status_code=200, json_error=None):
        self.payload = payload
        self.status_code = status_code
        self.json_error = json_error

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(response=self)

    def json(self):
        if self.json_error:
            raise self.json_error
        return self.payload


def test_transient_error_retries_with_backoff(monkeypatch):
    responses = [requests.RequestException("offline"), FakeResponse([])]
    sleeps = []

    def fake_get(*args, **kwargs):
        response = responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response

    monkeypatch.setattr(api.requests, "get", fake_get)
    assert api.fetch_cme("2026-01-01", "2026-01-02", sleep_fn=sleeps.append) == []
    assert sleeps == [1]


def test_timeout_is_treated_as_transient(monkeypatch):
    calls = []

    def fake_get(*args, **kwargs):
        calls.append(1)
        if len(calls) == 1:
            raise requests.Timeout("too slow")
        return FakeResponse([])

    monkeypatch.setattr(api.requests, "get", fake_get)
    assert api.fetch_cme("2026-01-01", "2026-01-02", sleep_fn=lambda _: None) == []
    assert len(calls) == 2


def test_rate_limit_is_retryable(monkeypatch):
    responses = [FakeResponse(status_code=429), FakeResponse([])]
    monkeypatch.setattr(api.requests, "get", lambda *args, **kwargs: responses.pop(0))
    assert api.fetch_cme("2026-01-01", "2026-01-02", sleep_fn=lambda _: None) == []


def test_client_error_is_not_retried(monkeypatch):
    calls = []

    def fake_get(*args, **kwargs):
        calls.append(1)
        return FakeResponse(status_code=400)

    monkeypatch.setattr(api.requests, "get", fake_get)
    with pytest.raises(requests.HTTPError):
        api.fetch_cme("2026-01-01", "2026-01-02", sleep_fn=lambda _: None)
    assert len(calls) == 1


def test_invalid_json_is_not_retried(monkeypatch):
    calls = []

    def fake_get(*args, **kwargs):
        calls.append(1)
        return FakeResponse(json_error=ValueError("json inválido"))

    monkeypatch.setattr(api.requests, "get", fake_get)
    with pytest.raises(ValueError):
        api.fetch_cme("2026-01-01", "2026-01-02", sleep_fn=lambda _: None)
    assert len(calls) == 1
