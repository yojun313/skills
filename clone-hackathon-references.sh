#!/usr/bin/env bash
# 내 레포 clone.sh와 독립적인 해커톤 참고 자료 준비 스크립트.
# 사용법: ./clone-hackathon-references.sh [--dest 경로] [--jobs 6] [--category 분야]
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
for required in git python3; do
  if ! command -v "$required" >/dev/null 2>&1; then
    echo "필수 프로그램이 없습니다: $required" >&2
    exit 1
  fi
done
exec python3 "$SCRIPT_DIR/hackathon-kit/scripts/prepare.py" "$@"
