#!/usr/bin/env python3
"""Record OpenCode skill calls and Markdown writes under docs/ as CSV.

Reads a tool event from stdin. Logging failures never block the tool call.
"""

import json
import os
import sys
from datetime import datetime, timezone

HEADER = "timestamp,session_id,type,value"


def clean(value):
    """Keep commas and line breaks out of the simple CSV format."""
    return str(value).replace(",", "_").replace("\n", " ").replace("\r", " ").strip()


def classify(tool_name, tool_input, project_dir):
    if tool_name == "Skill":
        skill = tool_input.get("skill")
        return ("skill", skill) if skill else None

    if tool_name in ("Write", "Edit"):
        path = tool_input.get("file_path")
        if not path:
            return None
        rel = os.path.relpath(path, project_dir) if project_dir else path
        rel = rel.replace(os.sep, "/")
        if rel.startswith("docs/") and rel.endswith(".md"):
            return ("write", rel)

    return None


def main():
    payload = json.load(sys.stdin)
    project_dir = os.environ.get("OPENCODE_PROJECT_DIR") or ""
    entry = classify(
        payload.get("tool_name", ""), payload.get("tool_input") or {}, project_dir
    )
    if entry is None:
        return 0

    kind, value = entry
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    session = payload.get("session_id") or "unbekannt"
    row = f"{stamp},{clean(session)},{kind},{clean(value)}"

    csv_path = os.path.join(project_dir or ".", ".opencode", "skill-usage.csv")
    needs_header = not os.path.exists(csv_path)
    with open(csv_path, "a", encoding="utf-8") as fh:
        if needs_header:
            fh.write(HEADER + "\n")
        fh.write(row + "\n")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
