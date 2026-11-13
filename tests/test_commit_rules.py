import subprocess
import sys
from pathlib import Path


SCRIPT = Path("scripts/check_commit_message.py")


def run_check(tmp_path, message):
    path = tmp_path / "COMMIT_EDITMSG"
    path.write_text(message + "\n", encoding="utf-8")
    return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)


def test_commit_rule_accepts_conventional_commit(tmp_path):
    assert run_check(tmp_path, "feat(api): add retry").returncode == 0


def test_commit_rule_rejects_unstructured_commit(tmp_path):
    result = run_check(tmp_path, "mudanças no projeto")
    assert result.returncode == 1
