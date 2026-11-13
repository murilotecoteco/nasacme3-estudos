import pytest

from nasacme_estudos.domain import (
    deduplicate_records,
    is_earth_directed,
    normalize_event,
    pick_best_analysis,
)


def test_pick_best_analysis_prefers_marked_item():
    assert pick_best_analysis([{"speed": 1}, {"speed": 2, "isMostAccurate": True}])["speed"] == 2


def test_missing_analysis_is_safe():
    assert normalize_event({"activityID": "x", "cmeAnalyses": []})["speed"] is None
    assert is_earth_directed(None) is False


def test_normalization_applies_earth_rule():
    event = normalize_event({
        "activityID": "x",
        "cmeAnalyses": [{"latitude": 29, "longitude": -29, "speed": 500}],
        "instruments": [{"displayName": "LASCO"}],
    })
    assert event["is_earth_directed"] is True
    assert event["instruments"] == ["LASCO"]


def test_deduplication_is_idempotent():
    records = [{"activity_id": "a"}, {"activity_id": "a"}, {"activity_id": "b"}]
    assert deduplicate_records(records) == [records[0], records[2]]


def test_missing_activity_id_is_rejected():
    with pytest.raises(ValueError, match="activity_id"):
        deduplicate_records([{"activity_id": ""}])
