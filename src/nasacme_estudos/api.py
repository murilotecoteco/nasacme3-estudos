"""Cliente HTTP mínimo para estudar timeout, retry e JSON."""

from __future__ import annotations

import argparse
import logging
import time
from typing import Any

import requests

from .domain import normalize_event

LOGGER = logging.getLogger(__name__)
NASA_CME_URL = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/CME"


RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def fetch_cme(
    start: str,
    end: str,
    retries: int = 3,
    sleep_fn: Any = time.sleep,
) -> list[dict[str, Any]]:
    """Busca e normaliza CME com retry controlado e backoff exponencial."""
    if retries < 1:
        raise ValueError("retries deve ser maior ou igual a 1")

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                NASA_CME_URL,
                params={"startDate": start, "endDate": end},
                timeout=30,
            )
            response.raise_for_status()
            payload = response.json()
            if not isinstance(payload, list):
                raise ValueError("A API retornou JSON em formato inesperado")
            return [normalize_event(item) for item in payload]
        except ValueError:
            # Payload inválido não é corrigido repetindo a mesma resposta.
            raise
        except requests.RequestException as error:
            response = getattr(error, "response", None)
            status = getattr(response, "status_code", None)
            if status is not None and status not in RETRYABLE_STATUS:
                raise
            LOGGER.warning("tentativa %d/%d falhou", attempt, retries, exc_info=True)
            if attempt == retries:
                raise
            sleep_fn(min(30, 2 ** (attempt - 1)))
    return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()
    events = fetch_cme(args.start, args.end)
    print(f"{len(events)} evento(s) normalizado(s)")
