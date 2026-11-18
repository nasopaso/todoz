# Aufgabenverwaltung

Benötigt Python 3.7 oder neuer und [uv](https://docs.astral.sh/uv/). Die Befehle werden im Projektverzeichnis ausgeführt:

```bash
uv run python aufgaben.py add "Workshop vorbereiten"
uv run python aufgaben.py list
uv run python aufgaben.py done 1
```

Die Daten werden in `aufgaben.json` im aktuellen Arbeitsverzeichnis gespeichert; eine noch nicht vorhandene Datei wird beim ersten Hinzufügen angelegt. `list` zeigt offene Aufgaben mit `[ ]` und erledigte mit `[x]`. `done` kann für bereits erledigte Aufgaben erneut ausgeführt werden.

## Tests

Die Tests verwenden temporäre Verzeichnisse und verändern keine vorhandenen Aufgabendaten. Mit installiertem [uv](https://docs.astral.sh/uv/) lassen sie sich wie folgt starten:

```bash
uv run pytest
```

`uv` erstellt bei Bedarf eine virtuelle Umgebung und installiert die Entwicklungsabhängigkeiten aus `uv.lock`. Mit `uv sync` lassen sich diese auch vorab installieren.
