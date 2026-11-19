# Aufgabenverwaltung

Benötigt Python 3.7 oder neuer und [uv](https://docs.astral.sh/uv/). Die Befehle werden im Projektverzeichnis ausgeführt:

```bash
uv run python src/aufgaben.py add "Workshop vorbereiten"
uv run python src/aufgaben.py list
uv run python src/aufgaben.py done 1
```

Die Daten werden in `data/aufgaben.json` relativ zum aktuellen Arbeitsverzeichnis gespeichert. Ein fehlendes Verzeichnis und eine fehlende Datei werden beim ersten Hinzufügen angelegt. `list` zeigt offene Aufgaben mit `[ ]` und erledigte mit `[x]`. `done` kann für bereits erledigte Aufgaben erneut ausgeführt werden.

## Tests

Die Tests verwenden temporäre Verzeichnisse und verändern keine vorhandenen Aufgabendaten. Mit installiertem [uv](https://docs.astral.sh/uv/) lassen sie sich wie folgt starten:

```bash
uv run pytest
```

`uv` erstellt bei Bedarf eine virtuelle Umgebung und installiert die Entwicklungsabhängigkeiten aus `uv.lock`. Mit `uv sync` lassen sich diese auch vorab installieren.

## Skill-Nutzung in OpenCode

Das lokale OpenCode-Plugin protokolliert erfolgreiche Skill-Aufrufe und Schreibvorgänge an Markdown-Dateien unter `docs/` in `.opencode/skill-usage.csv`. Die Datei entsteht beim ersten protokollierten Ereignis und wird nicht mit Git versioniert. Sie enthält UTC-Zeitpunkt, Session-ID, Ereignistyp und Skill-Name oder Dateipfad. Es werden nur Schreibvorgänge über die vom Plugin erfassten OpenCode-Werkzeuge protokolliert.

Das Protokoll belegt einen Aufruf, nicht die korrekte Anwendung des Skills oder eine direkte Zuordnung zu einem Dokument. Bei Fehlern blockiert der Logger die Arbeit nicht. Er benötigt `python3` im PATH.

Die Plugin-Tests benötigen Node.js und laufen mit:

```bash
node --test .opencode/tests/skill-usage-log.test.js
```
