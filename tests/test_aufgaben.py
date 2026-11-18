import json
import subprocess
import sys
from pathlib import Path

import pytest


SKRIPT = Path(__file__).resolve().parents[1] / "aufgaben.py"


@pytest.fixture
def datendatei(tmp_path):
    return tmp_path / "aufgaben.json"


@pytest.fixture
def cli(tmp_path):
    def ausfuehren(*argumente):
        return subprocess.run(
            [sys.executable, str(SKRIPT), *argumente],
            cwd=tmp_path,
            capture_output=True,
            text=True,
        )

    return ausfuehren


def test_leere_liste_legt_keine_datei_an(cli, datendatei):
    ergebnis = cli("list")
    assert ergebnis.returncode == 0
    assert "Keine Aufgaben" in ergebnis.stdout
    assert not datendatei.exists()


def test_aufgaben_hinzufuegen_auflisten_und_erledigen(cli, datendatei):
    assert cli("add", "Workshop vorbereiten").returncode == 0
    assert cli("add", "  E-Mails prüfen  ").returncode == 0
    ergebnis = cli("list")
    assert ergebnis.returncode == 0
    assert "1. [ ] Workshop vorbereiten" in ergebnis.stdout
    assert "2. [ ] E-Mails prüfen" in ergebnis.stdout

    assert cli("done", "1").returncode == 0
    assert cli("done", "1").returncode == 0
    ergebnis = cli("list")
    assert "1. [x] Workshop vorbereiten" in ergebnis.stdout
    assert "2. [ ] E-Mails prüfen" in ergebnis.stdout
    daten = json.loads(datendatei.read_text(encoding="utf-8"))
    assert daten[0]["erledigt"] is True
    assert daten[1]["erledigt"] is False


def test_unbekannte_aufgabe(cli, datendatei):
    ergebnis = cli("done", "42")
    assert ergebnis.returncode != 0
    assert "Aufgabe 42 existiert nicht" in ergebnis.stderr
    assert not datendatei.exists()


@pytest.mark.parametrize("befehl", [("add", "  "), ("done", "0"), ("done", "abc"), ("add",)])
def test_ungueltige_eingaben(cli, datendatei, befehl):
    ergebnis = cli(*befehl)
    assert ergebnis.returncode != 0
    assert ergebnis.stderr
    assert "Traceback" not in ergebnis.stderr
    assert not datendatei.exists()


@pytest.mark.parametrize("inhalt", [
    "{ kaputt",
    '{"id": 1}',
    '[{"id": 1, "titel": "Test", "erledigt": 1}]',
])
def test_beschaedigte_datei_wird_nicht_ueberschrieben(cli, datendatei, inhalt):
    datendatei.write_text(inhalt, encoding="utf-8")
    ergebnis = cli("add", "Neu")
    assert ergebnis.returncode != 0
    assert "Datendatei" in ergebnis.stderr
    assert datendatei.read_text(encoding="utf-8") == inhalt


def test_datei_kann_nicht_gelesen_werden(cli, datendatei):
    datendatei.mkdir()
    ergebnis = cli("list")
    assert ergebnis.returncode != 0
    assert "konnte nicht gelesen werden" in ergebnis.stderr
    assert "Traceback" not in ergebnis.stderr
