"""Pipeline local: ler, normalizar, deduplicar, dividir em lotes e medir."""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Iterable

from .domain import deduplicate_records, normalize_event
from .storage import EventStore, SQLiteStore

LOGGER = logging.getLogger(__name__)
STATUS_CONCLUIDO = "concluido"
STATUS_ERRO_PARCIAL = "erro_parcial"
STATUS_ERRO_CRITICO = "erro_critico"


def batches(items: list[dict[str, Any]], size: int) -> Iterable[list[dict[str, Any]]]:
    """Divide uma lista em lotes sem perder a ordem."""
    if size <= 0:
        raise ValueError("o tamanho do lote deve ser positivo")
    for start in range(0, len(items), size):
        yield items[start : start + size]


def prepare_fixture(path: Path) -> list[dict[str, Any]]:
    """Lê o formato bruto do fixture e aplica o mesmo contrato do pipeline."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    return deduplicate_records([normalize_event(item) for item in raw])


def summarize(records: list[dict[str, Any]], batch_size: int = 2) -> dict[str, int]:
    """Produz métricas que, no projeto real, seriam gravadas em `execucoes`."""
    return {
        "records": len(records),
        "batches": sum(1 for _ in batches(records, batch_size)),
        "earth_directed": sum(1 for item in records if item["is_earth_directed"]),
    }


def process_batches(
    records: list[dict[str, Any]],
    store: EventStore,
    batch_size: int = 50,
) -> dict[str, Any]:
    """Processa lotes, registra o resultado e devolve métricas observáveis."""
    unique_records = deduplicate_records(records)
    processed = 0
    batches_count = 0
    errors: list[str] = []

    for number, batch in enumerate(batches(unique_records, batch_size), 1):
        batches_count += 1
        try:
            processed += store.upsert_batch(batch)
        except Exception as error:  # o pipeline continua para medir falha parcial
            errors.append(f"lote {number}: {error}")

    if not errors:
        status = STATUS_CONCLUIDO
    elif processed:
        status = STATUS_ERRO_PARCIAL
    else:
        status = STATUS_ERRO_CRITICO

    details = "; ".join(errors) if errors else None
    store.register_execution(processed, batches_count, len(errors), status, details)
    return {
        "records": processed,
        "batches": batches_count,
        "errors": len(errors),
        "status": status,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--database", type=Path)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    records = prepare_fixture(args.fixture)
    if args.database:
        args.database.parent.mkdir(parents=True, exist_ok=True)
        store = SQLiteStore(args.database)
        try:
            metrics = process_batches(records, store, args.batch_size)
        finally:
            store.close()
    else:
        metrics = summarize(records, args.batch_size)
    LOGGER.info("métricas: %s", metrics)


if __name__ == "__main__":
    main()
