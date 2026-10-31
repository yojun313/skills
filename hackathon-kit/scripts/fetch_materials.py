#!/usr/bin/env python3
"""Download small public semiconductor references and the UCI SECOM dataset."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import tempfile
from urllib.request import Request, urlopen
import zipfile

MATERIALS = [
    {
        "name": "secom.zip",
        "folder": "datasets/secom",
        "url": "https://archive.ics.uci.edu/static/public/179/secom.zip",
        "source": "https://archive.ics.uci.edu/dataset/179/secom",
        "citation": "McCann, M. & Johnston, A. (2008). SECOM. UCI Machine Learning Repository. DOI: 10.24432/C54305.",
        "license": "CC BY 4.0; see source landing page",
    },
    {
        "name": "nist-virtual-metrology-2025.pdf",
        "folder": "materials",
        "url": "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958452",
        "source": "https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic",
        "citation": "Han et al. (2025), A Comparative Study of Semiconductor Virtual Metrology Methods and Novel Algorithmic Framework for Dynamic Sampling. DOI: 10.1109/TSM.2025.3531920.",
        "license": "Author manuscript from NIST; consult notices in PDF and source for reuse",
    },
    {
        "name": "nist-semiconductor-manufacturing-2026.pdf",
        "folder": "materials",
        "url": "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=961532",
        "source": "https://www.nist.gov/publications/innovations-advanced-processes-and-systems-semiconductor-manufacturing",
        "citation": "Shih et al. (2026), Innovations in advanced processes and systems for semiconductor manufacturing. DOI: 10.1016/j.cirp.2026.04.115.",
        "license": "Author manuscript from NIST; consult notices in PDF and source for reuse",
    },
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest", type=Path, default=Path.home() / "hackathon-reference"
    )
    args = parser.parse_args()
    root = args.dest.expanduser().resolve()
    records, failures = [], []
    for material in MATERIALS:
        file = root / material["folder"] / material["name"]
        file.parent.mkdir(parents=True, exist_ok=True)
        try:
            if file.exists():
                payload = file.read_bytes()
            else:
                request = Request(
                    material["url"], headers={"User-Agent": "hackathon-reference-kit"}
                )
                with urlopen(request, timeout=60) as response:
                    payload = response.read(64 * 1024 * 1024 + 1)
                if len(payload) > 64 * 1024 * 1024:
                    raise ValueError("download exceeds 64 MiB")
            expected = b"%PDF-" if file.suffix == ".pdf" else b"PK"
            if not payload.startswith(expected):
                raise ValueError("unexpected file format (possibly an HTML error page)")
            if not file.exists():
                with tempfile.NamedTemporaryFile(
                    dir=file.parent, delete=False
                ) as output:
                    output.write(payload)
                    temporary = Path(output.name)
                temporary.replace(file)
            record = {
                **material,
                "path": str(file.relative_to(root)),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "bytes": len(payload),
                "checked_at": datetime.now(timezone.utc).isoformat(),
            }
            if file.suffix == ".zip":
                with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                    for name in ["secom.data", "secom_labels.data", "secom.names"]:
                        matching = [
                            member
                            for member in archive.namelist()
                            if Path(member).name == name
                        ]
                        if len(matching) != 1:
                            raise ValueError(f"expected one {name} in SECOM archive")
                        (file.parent / name).write_bytes(archive.read(matching[0]))
                features = [
                    line.split()
                    for line in (file.parent / "secom.data").read_text().splitlines()
                    if line.strip()
                ]
                labels = [
                    line.split()[0]
                    for line in (file.parent / "secom_labels.data")
                    .read_text()
                    .splitlines()
                    if line.strip()
                ]
                assert (
                    len(features) == len(labels)
                    and len({len(row) for row in features}) == 1
                )
                record["raw_data_shape"] = [len(features), len(features[0])]
                record["label_counts"] = dict(Counter(labels))
                record["missing_values"] = sum(
                    value.lower() == "nan" for row in features for value in row
                )
                (file.parent / "PROVENANCE.json").write_text(
                    json.dumps(record, ensure_ascii=False, indent=2) + "\n"
                )
                (file.parent / "README.md").write_text(
                    "# UCI SECOM\n\n"
                    + material["citation"]
                    + "\n\n"
                    + material["source"]
                    + "\n\n"
                    "License: CC BY 4.0. Label: -1=pass, +1=fail.\n"
                    "Raw secom.data contains 590 sensor columns. Timestamp is in secom_labels.data.\n"
                    "UCI landing-page metadata reports 591 features; inspect raw data before using.\n"
                    "Use original feature/label order; do not fit preprocessing on test data.\n"
                    "This public dataset is not SK hynix internal data.\n"
                )
            records.append(record)
            print(f"OK {file} ({len(payload):,} bytes)", flush=True)
        except Exception as exc:
            failures.append({"name": material["name"], "error": str(exc)})
            print(f"FAILED {material['name']}: {exc}", flush=True)
    (root / "MATERIALS_STATUS.json").write_text(
        json.dumps(
            {"materials": records, "failures": failures}, ensure_ascii=False, indent=2
        )
        + "\n"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
