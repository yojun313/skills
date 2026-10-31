#!/usr/bin/env python3
"""Search the local repository/skill catalog without external dependencies."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--skills", action="store_true")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    root = args.root.expanduser()
    filename = "SKILLS_INDEX.json" if args.skills else "repositories.json"
    file = root / filename
    if not file.exists():
        parser.error(
            f"{file}가 없습니다. 먼저 clone-hackathon-references.sh를 실행하세요."
        )
    data = json.loads(file.read_text())
    rows = data if args.skills else data["repositories"]
    tokens = args.query.casefold().split()
    matches = [
        row
        for row in rows
        if all(
            token in json.dumps(row, ensure_ascii=False).casefold() for token in tokens
        )
    ]
    for row in matches[: args.limit]:
        if args.skills:
            print(
                f"{row['name']} ({row['repo']})\n  {root / row['path']}\n  {row['description']}"
            )
        else:
            print(
                f"{row['priority']} {row['repo']} [{row['category']}]\n  {row['summary']}\n  {root / row['directory']}"
            )
    print(f"검색 결과 {len(matches)}개; 표시 {min(len(matches), args.limit)}개")


if __name__ == "__main__":
    main()
