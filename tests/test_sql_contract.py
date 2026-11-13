from pathlib import Path


SQL = Path("sql/01_schema.sql").read_text(encoding="utf-8").lower()


def test_sql_contains_required_security_contract():
    assert "unique" in SQL
    assert "enable row level security" in SQL
    assert "to anon, authenticated" in SQL
    assert "to service_role" in SQL
    assert "grant select" in SQL
