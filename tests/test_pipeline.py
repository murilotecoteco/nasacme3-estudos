from pathlib import Path

import pytest

from nasacme_estudos.pipeline import batches, prepare_fixture, summarize


def test_fixture_is_normalized_and_deduplicated():
    records = prepare_fixture(Path("fixtures/cme.json"))
    assert len(records) == 2
    assert summarize(records, batch_size=1) == {"records": 2, "batches": 2, "earth_directed": 1}


def test_batches_reject_non_positive_size():
    with pytest.raises(ValueError):
        list(batches([], 0))
