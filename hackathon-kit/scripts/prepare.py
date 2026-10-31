#!/usr/bin/env python3
"""Clone the curated public repositories and build local, offline reference indexes."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).resolve().parents[1]


def git(*args, cwd=None, timeout=60):
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"},
    )


def clone_one(repo, root):
    destination = root / repo["directory"]
    log = root / "logs" / (repo["repo"].replace("/", "__") + ".log")
    result = {
        "repo": repo["repo"],
        "directory": repo["directory"],
        "log": str(log.relative_to(root)),
    }
    temporary = None
    try:
        if destination.exists() or destination.is_symlink():
            top = git("rev-parse", "--show-toplevel", cwd=destination)
            remote = git("remote", "get-url", "origin", cwd=destination)
            expected = repo["clone_url"].removesuffix(".git").lower()
            if (
                top.returncode
                or Path(top.stdout.strip()).resolve() != destination.resolve()
                or remote.returncode
                or remote.stdout.strip().removesuffix(".git").lower() != expected
            ):
                raise ValueError(
                    "기존 경로가 해당 HTTPS 레포가 아닙니다. 파일을 보존하고 건너뜁니다."
                )
            result["status"] = "existing"
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = Path(
                tempfile.mkdtemp(
                    prefix="." + destination.name + ".partial-", dir=destination.parent
                )
            )
            process = git(
                "clone",
                "--depth",
                "1",
                "--single-branch",
                "--no-tags",
                "--",
                repo["clone_url"],
                str(temporary),
                timeout=900,
            )
            log.write_text(process.stdout + process.stderr)
            if process.returncode:
                raise RuntimeError(f"git clone exit={process.returncode}; {log} 확인")
            temporary.rename(destination)
            temporary = None
            result["status"] = "cloned"
        commit = git("rev-parse", "HEAD", cwd=destination)
        if commit.returncode:
            raise RuntimeError("HEAD를 확인할 수 없습니다.")
        result["commit"] = commit.stdout.strip()
        result["checked_at"] = datetime.now(timezone.utc).isoformat()
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        result.update(status="failed", error=str(exc))
    finally:
        if temporary is not None:
            shutil.rmtree(temporary)
    return result


def copy_guides(root):
    if root.resolve() == SOURCE.resolve():
        return
    for name in [
        "README.md",
        "AGENTS.md",
        "COFA_AGENT_INSTRUCTIONS.md",
        "CATALOG.md",
        "repositories.json",
        "repositories.tsv",
    ]:
        source = SOURCE / name
        if source.exists():
            shutil.copy2(source, root / name)
    for name in ["guides", "templates", "skill", "scripts"]:
        if (SOURCE / name).exists():
            shutil.copytree(SOURCE / name, root / name, dirs_exist_ok=True)


def index_repositories(repos, root, results):
    skills, inventory = [], []
    by_name = {row["repo"]: row for row in results}
    for repo in repos:
        path = root / repo["directory"]
        state = by_name.get(repo["repo"], {})
        if state.get("status") not in ("cloned", "existing") or not path.is_dir():
            continue
        entrypoints = []
        for candidate in [
            "README.md",
            "README.rst",
            "README",
            "readme.md",
            "docs",
            "examples",
            "tutorials",
            "notebooks",
            "skills",
            ".github/skills",
            "plugins",
            "pyproject.toml",
            "package.json",
            "LICENSE",
            "LICENSE.md",
        ]:
            if (path / candidate).exists():
                entrypoints.append(str((path / candidate).relative_to(root)))
        inventory.append(
            {**repo, "commit": state.get("commit"), "entrypoints": entrypoints}
        )
        # Walk avoids .git and does not follow symlinks into another checkout.
        for directory, subdirs, files in os.walk(path, followlinks=False):
            subdirs[:] = [
                name
                for name in subdirs
                if name not in (".git", "node_modules", ".venv")
            ]
            if "SKILL.md" not in files:
                continue
            skill_path = Path(directory) / "SKILL.md"
            if skill_path.is_symlink():
                continue
            content = skill_path.read_text(errors="replace")
            frontmatter = (
                content.split("---", 2)[1]
                if content.startswith("---") and content.count("---") >= 2
                else ""
            )
            name = re.search(r"^name:\s*(.+)", frontmatter, re.MULTILINE)
            description = re.search(r"^description:\s*(.*)", frontmatter, re.MULTILINE)
            excerpt = description.group(1).strip().strip("\"'") if description else ""
            if excerpt in ("", "|", ">", "|-", ">-"):
                excerpt = " ".join(frontmatter.splitlines()[1:12])[:350]
            skills.append(
                {
                    "name": name.group(1).strip().strip("\"'")
                    if name
                    else skill_path.parent.name,
                    "repo": repo["repo"],
                    "path": str(skill_path.relative_to(root)),
                    "description": excerpt,
                }
            )
    (root / "LOCAL_INDEX.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
    )
    (root / "SKILLS_INDEX.json").write_text(
        json.dumps(skills, ensure_ascii=False, indent=2) + "\n"
    )
    lines = [
        "# 로컬 스킬 색인",
        "",
        f"실제 checkout에서 발견한 SKILL.md: {len(skills)}개.",
        "",
        "전체를 로드하지 말고 검색 후 필요한 SKILL.md와 그 상대경로 자료만 읽으세요.",
        "",
        "| 스킬 | 레포 | 파일 | 설명 |",
        "| --- | --- | --- | --- |",
    ]
    for skill in skills:
        clean = lambda value: value.replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {clean(skill['name'])} | {skill['repo']} | [{clean(skill['path'])}]({skill['path']}) | {clean(skill['description'])} |"
        )
    (root / "SKILLS_INDEX.md").write_text("\n".join(lines) + "\n")
    return len(inventory), len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest", type=Path, default=Path.home() / "hackathon-reference"
    )
    parser.add_argument("--jobs", type=int, default=6)
    parser.add_argument(
        "--category",
        action="append",
        default=[],
        help="분야 번호 또는 이름 일부; 여러 번 지정 가능",
    )
    parser.add_argument(
        "--priority",
        choices=["P0", "P1", "P2"],
        help="지정한 우선순위까지 clone (P0만 또는 P0+P1 등)",
    )
    parser.add_argument(
        "--list", action="store_true", help="선택한 레포만 출력하고 종료"
    )
    parser.add_argument(
        "--index-only",
        action="store_true",
        help="기존 상태 파일로 로컬 색인만 다시 생성",
    )
    parser.add_argument(
        "--skip-materials",
        action="store_true",
        help="SECOM과 공개 NIST PDF 다운로드 생략",
    )
    args = parser.parse_args()
    if not 1 <= args.jobs <= 16:
        parser.error("--jobs는 1~16 사이여야 합니다.")
    manifest = json.loads((SOURCE / "repositories.json").read_text())
    all_repos = manifest["repositories"]
    repos = [
        repo
        for repo in all_repos
        if (
            not args.category or any(term in repo["category"] for term in args.category)
        )
        and (not args.priority or repo["priority"] <= args.priority)
    ]
    if not repos:
        parser.error("조건에 맞는 레포가 없습니다. --list로 확인하세요.")
    if args.list:
        for repo in repos:
            print(
                f"{repo['category']}\t{repo['priority']}\t{repo['repo']}\t{repo['summary']}"
            )
        return 0
    root = args.dest.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    (root / "logs").mkdir(exist_ok=True)
    copy_guides(root)
    state_file = root / "CLONE_STATUS.json"
    previous = json.loads(state_file.read_text()) if state_file.exists() else []
    results = {row["repo"]: row for row in previous}
    if not args.index_only:
        print(
            f"{len(repos)}개 레포 → {root}; HTTPS shallow clone, jobs={args.jobs}",
            flush=True,
        )
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(clone_one, repo, root) for repo in repos]
            for i, future in enumerate(as_completed(futures), start=1):
                result = future.result()
                results[result["repo"]] = result
                temporary_state = state_file.with_suffix(".tmp")
                temporary_state.write_text(
                    json.dumps(list(results.values()), ensure_ascii=False, indent=2)
                    + "\n"
                )
                temporary_state.replace(state_file)
                print(
                    f"[{i}/{len(repos)}] {result['status']}: {result['repo']}"
                    + (f" — {result['error']}" if "error" in result else ""),
                    flush=True,
                )
    count, skills = index_repositories(all_repos, root, list(results.values()))
    failures = [
        results[repo["repo"]]
        for repo in repos
        if results.get(repo["repo"], {}).get("status") == "failed"
    ]
    print(
        f"로컬 색인: 레포 {count}개 / SKILL.md {skills}개 / 선택 범위 실패 {len(failures)}개"
    )
    print(f"에이전트 시작점: {root / 'AGENTS.md'}")
    material_failure = False
    if not args.index_only and not args.skip_materials:
        material_failure = (
            subprocess.run(
                [
                    sys.executable,
                    str(SOURCE / "scripts/fetch_materials.py"),
                    "--dest",
                    str(root),
                ]
            ).returncode
            != 0
        )
    return 1 if failures or material_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
