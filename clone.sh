#!/usr/bin/env bash
# 사용법: ./clone.sh [GitHub 계정] [저장 폴더]
# 기본값: yojun313의 public 레포(fork 포함) 중 CSED로 시작하는 레포를 제외하고
# ~/yojun/에 HTTPS로 clone. 기본 브랜치의 최신 커밋 하나만 받고 태그·과거 이력은 생략.
# Git LFS 대용량 파일은 다운로드하지 않고 포인터 파일만 받습니다.
set -euo pipefail

if [[ $# -gt 2 ]]; then
  echo "사용법: $0 [GitHub 계정] [저장 폴더]" >&2
  exit 1
fi

GITHUB_USER="${1:-yojun313}"
DEST_DIR="${2:-$HOME/yojun}"

for command in git python3; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "필수 프로그램이 없습니다: $command" >&2
    exit 1
  fi
done

REPO_LIST="$(mktemp)"
trap 'rm -f "$REPO_LIST"' EXIT

echo "GitHub public 레포 목록 조회: $GITHUB_USER"
# 페이지당 최대 100개씩 조회하여 레포가 100개를 넘어도 모두 가져옵니다.
# 로그인이나 GitHub 토큰은 필요하지 않습니다.
python3 - "$GITHUB_USER" > "$REPO_LIST" <<'PY'
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

user = quote(sys.argv[1], safe="")
page = 1
try:
    while True:
        url = (
            f"https://api.github.com/users/{user}/repos"
            f"?type=owner&sort=full_name&per_page=100&page={page}"
        )
        request = Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "clone-public-repos",
        })
        with urlopen(request, timeout=30) as response:
            repos = json.load(response)
        for repo in repos:
            if not repo.get("private", True):
                print(f"{repo['name']}\t{repo['clone_url']}")
        if len(repos) < 100:
            break
        page += 1
except HTTPError as exc:
    print(f"GitHub API 조회 실패: HTTP {exc.code}", file=sys.stderr)
    if exc.code in (403, 429):
        print("API 요청 한도에 도달했을 수 있습니다. 잠시 후 다시 실행하세요.", file=sys.stderr)
    sys.exit(1)
except (URLError, TimeoutError, ValueError, KeyError) as exc:
    print(f"레포 목록 조회 실패: {exc}", file=sys.stderr)
    sys.exit(1)
PY

mkdir -p "$DEST_DIR"
cloned=0
skipped=0
failed=0

while IFS=$'\t' read -r name url; do
  if [[ "$name" == CSED* ]]; then
    echo "[건너뜀] CSED 레포 제외: $name"
    skipped=$((skipped + 1))
    continue
  fi

  if [[ -e "$DEST_DIR/$name" || -L "$DEST_DIR/$name" ]]; then
    echo "[건너뜀] 이미 존재: $DEST_DIR/$name"
    skipped=$((skipped + 1))
    continue
  fi

  echo "[clone] $url"
  if GIT_TERMINAL_PROMPT=0 GIT_LFS_SKIP_SMUDGE=1 git clone \
    --depth 1 --single-branch --no-tags -- "$url" "$DEST_DIR/$name"; then
    cloned=$((cloned + 1))
  else
    echo "[실패] $name — 나머지 레포는 계속 진행합니다." >&2
    failed=$((failed + 1))
  fi
done < "$REPO_LIST"

echo "완료: clone $cloned / 건너뜀 $skipped / 실패 $failed"
echo "저장 위치: $DEST_DIR"
[[ "$failed" -eq 0 ]]
