"""Persistência local para estudar upsert e auditoria sem credenciais."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Protocol


class EventStore(Protocol):
    def upsert_batch(self, records: list[dict[str, Any]]) -> int: ...

    def register_execution(
        self,
        processed: int,
        batches: int,
        errors: int,
        status: str,
        details: str | None = None,
    ) -> None: ...


class SQLiteStore:
    """Implementação offline com a mesma ideia de chave natural do Supabase."""

    def __init__(self, path: str | Path):
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(
            """
            create table if not exists cme_events (
                activity_id text primary key,
                start_time text,
                speed real,
                type text,
                is_earth_directed integer not null,
                source_location text,
                instruments text not null,
                fetched_at text default current_timestamp
            );
            create table if not exists execucoes (
                id integer primary key autoincrement,
                executed_at text default current_timestamp,
                registros_processados integer not null,
                lotes integer not null,
                erros integer not null,
                status text not null,
                detalhes text
            );
            """
        )
        self.connection.commit()

    def upsert_batch(self, records: list[dict[str, Any]]) -> int:
        for record in records:
            if not record.get("activity_id"):
                raise ValueError("não é possível persistir evento sem activity_id")
        self.connection.executemany(
            """
            insert into cme_events
              (activity_id, start_time, speed, type, is_earth_directed,
               source_location, instruments)
            values (?, ?, ?, ?, ?, ?, ?)
            on conflict(activity_id) do update set
              start_time = excluded.start_time,
              speed = excluded.speed,
              type = excluded.type,
              is_earth_directed = excluded.is_earth_directed,
              source_location = excluded.source_location,
              instruments = excluded.instruments
            """,
            [
                (
                    record["activity_id"],
                    record.get("start_time"),
                    record.get("speed"),
                    record.get("type"),
                    int(record.get("is_earth_directed", False)),
                    record.get("source_location"),
                    json.dumps(record.get("instruments", [])),
                )
                for record in records
            ],
        )
        self.connection.commit()
        return len(records)

    def register_execution(
        self,
        processed: int,
        batches: int,
        errors: int,
        status: str,
        details: str | None = None,
    ) -> None:
        self.connection.execute(
            """
            insert into execucoes
              (registros_processados, lotes, erros, status, detalhes)
            values (?, ?, ?, ?, ?)
            """,
            (processed, batches, errors, status, details),
        )
        self.connection.commit()

    def count_events(self) -> int:
        return int(self.connection.execute("select count(*) from cme_events").fetchone()[0])

    def last_execution(self) -> dict[str, Any] | None:
        row = self.connection.execute(
            "select * from execucoes order by id desc limit 1"
        ).fetchone()
        return dict(row) if row else None

    def close(self) -> None:
        self.connection.close()
