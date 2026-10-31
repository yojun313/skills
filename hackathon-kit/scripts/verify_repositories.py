#!/usr/bin/env python3
"""Maintainer helper: refresh public GitHub repository metadata using gh auth."""

import csv
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fetch(row):
    result = subprocess.run(
        ["gh", "api", "repos/" + row["repo"]],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode:
        return None, {"repo": row["repo"], "error": result.stderr.strip()}
    data = json.loads(result.stdout)
    if data.get("private") or data.get("disabled"):
        return None, {"repo": row["repo"], "error": "private or disabled"}
    row.update(
        repo=data["full_name"],
        url=data["html_url"],
        clone_url=data["clone_url"],
        default_branch=data["default_branch"],
        stars=data["stargazers_count"],
        archived=data["archived"],
        pushed_at=data["pushed_at"],
        license=(data.get("license") or {}).get("spdx_id", "UNKNOWN"),
        upstream_description=data.get("description") or "",
        size_kb=data["size"],
        verified_at=datetime.now(timezone.utc).isoformat(),
    )
    row["directory"] = f"repos/{row['category']}/{row['repo'].replace('/', '__')}"
    return row, None


def main():
    with (ROOT / "repositories.tsv").open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    verified, failures = [], []
    with ThreadPoolExecutor(max_workers=6) as pool:
        for row, error in pool.map(fetch, rows):
            if error:
                failures.append(error)
                print("UNAVAILABLE", error["repo"], flush=True)
            else:
                verified.append(row)
                print(
                    "OK",
                    row["repo"],
                    row["stars"],
                    "archived=" + str(row["archived"]),
                    flush=True,
                )
    manifest = {
        "schema_version": 1,
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "repositories": verified,
    }
    (ROOT / "repositories.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    (ROOT / "unavailable-repositories.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2) + "\n"
    )
    print(f"{len(verified)} verified, {len(failures)} unavailable")


if __name__ == "__main__":
    main()
