#!/usr/bin/env python3
"""Create a local mastery session notes file from the template.

Usage:
  python scripts/init_session.py --topic "Redis locks" --mode Interview --level L3
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    return text.strip("-") or "session"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True, help="Session topic")
    parser.add_argument("--mode", default="Workshop", help="ELI5, ELI14, ELII, Expert, Interview, Review, Workshop")
    parser.add_argument("--level", default="L2", help="Target mastery level: L1, L2, L3, L4")
    parser.add_argument("--goal", default="", help="Optional session goal")
    parser.add_argument("--output-dir", default="sessions", help="Output directory")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    template_path = root / "assets" / "session_notes_template.md"
    template = template_path.read_text(encoding="utf-8")

    today = datetime.now().strftime("%Y-%m-%d")
    content = (
        template
        .replace("{{date}}", today)
        .replace("{{topic}}", args.topic)
        .replace("{{mode}}", args.mode)
        .replace("{{level}}", args.level)
        .replace("{{goal}}", args.goal or f"Build verified understanding of {args.topic}.")
        .replace("{{starting_understanding}}", "TBD")
        .replace("{{summary}}", "TBD")
    )

    out_dir = root / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{today}-{slugify(args.topic)}.md"
    out_path = out_dir / filename
    out_path.write_text(content, encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
