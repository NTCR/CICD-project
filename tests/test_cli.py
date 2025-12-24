from __future__ import annotations

from src.myproject.cli import main


def test_version_prints_version(capsys):
    code = main(["--version"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "0.1.0"


def test_hello_prints_greeting(capsys):
    code = main(["hello", "Ada"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "Hello, Ada!"