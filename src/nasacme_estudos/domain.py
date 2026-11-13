"""Regras de negócio puras: fáceis de testar sem rede ou banco."""

from __future__ import annotations

from typing import Any


def pick_best_analysis(analyses: list[dict[str, Any]] | None) -> dict[str, Any] | None:
    """Escolhe a análise marcada como mais precisa ou a última disponível."""
    if not analyses:
        return None
    return next((item for item in analyses if item.get("isMostAccurate")), analyses[-1])


def is_earth_directed(analysis: dict[str, Any] | None) -> bool:
    """Aplica a regra didática de latitude/longitude próximas de zero."""
    if not analysis or analysis.get("latitude") is None or analysis.get("longitude") is None:
        return False
    return abs(analysis["latitude"]) < 30 and abs(analysis["longitude"]) < 30


def normalize_event(raw: dict[str, Any]) -> dict[str, Any]:
    """Converte o contrato da API em um registro menor e estável para o banco."""
    analysis = pick_best_analysis(raw.get("cmeAnalyses"))
    instruments = [
        item["displayName"]
        for item in raw.get("instruments", [])
        if item and item.get("displayName")
    ]
    linked_events = [
        item["activityID"]
        for item in raw.get("linkedEvents", [])
        if item and item.get("activityID")
    ]
    return {
        "activity_id": raw.get("activityID"),
        "start_time": raw.get("startTime"),
        "source_location": raw.get("sourceLocation") or None,
        "note": raw.get("note") or None,
        "instruments": instruments,
        "speed": analysis.get("speed") if analysis else None,
        "type": analysis.get("type") if analysis else None,
        "is_earth_directed": is_earth_directed(analysis),
        "latitude": analysis.get("latitude") if analysis else None,
        "longitude": analysis.get("longitude") if analysis else None,
        "half_angle": analysis.get("halfAngle") if analysis else None,
        "link": raw.get("link") or None,
        "linked_events": linked_events,
    }


def deduplicate_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Preserva a primeira ocorrência de cada activity_id."""
    seen: set[str | None] = set()
    unique: list[dict[str, Any]] = []
    for record in records:
        key = record.get("activity_id")
        if not isinstance(key, str) or not key.strip():
            raise ValueError("todo evento precisa de um activity_id não vazio")
        if key in seen:
            continue
        seen.add(key)
        unique.append(record)
    return unique
