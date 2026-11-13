from nasacme_estudos.pipeline import process_batches
from nasacme_estudos.storage import SQLiteStore


def record(activity_id, speed=500):
    return {
        "activity_id": activity_id,
        "start_time": "2026-01-01T00:00Z",
        "speed": speed,
        "type": "S",
        "is_earth_directed": False,
        "source_location": "S10E10",
        "instruments": ["LASCO"],
    }


def test_upsert_is_idempotent_and_logs_execution(tmp_path):
    store = SQLiteStore(tmp_path / "study.db")
    records = [record("a"), record("b")]
    first = process_batches(records, store, batch_size=1)
    second = process_batches(records, store, batch_size=1)

    assert first["status"] == "concluido"
    assert second["status"] == "concluido"
    assert store.count_events() == 2
    assert store.last_execution()["status"] == "concluido"
    store.close()
