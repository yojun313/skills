# SK하이닉스 해커톤 참고 키트

**19개 분야의 공개 레포 153개**, 에이전트가 검색할 로컬 스킬 색인, 반도체 요약, COFA 실행 지침을 준비하는 패키지다. 개인 레포를 받는 `../clone.sh`와 별개다. 실제 대회 안내·과제가 준비 문서보다 우선한다.

## 지금 읽을 것

| 원하는 것 | 파일 |
| --- | --- |
| AI에게 바로 줄 작업 지침 | [COFA_AGENT_INSTRUCTIONS.md](COFA_AGENT_INSTRUCTIONS.md) |
| 사람이 읽는 평가 관점·준비 전략 | [COFA_PLAYBOOK.md](guides/COFA_PLAYBOOK.md) |
| 반도체·메모리·제조 데이터 용어 | [SEMICONDUCTOR_BRIEF.md](guides/SEMICONDUCTOR_BRIEF.md) |
| 문제에 맞는 레포 조합 | [USE_CASE_RECIPES.md](guides/USE_CASE_RECIPES.md) |
| 전체 목록·설명·우선순위·출처 | [CATALOG.md](CATALOG.md) |
| 공식 자료와 후기의 구분 | [SOURCES.md](guides/SOURCES.md) |
| 오늘 남은 시간별 준비 | [READING_ORDER.md](guides/READING_ORDER.md) |
| 새 세션의 탐색 시작점 | [AGENTS.md](AGENTS.md) |

## 한 번에 준비

요구사항: Bash, Git, Python **3.9 이상**, 인터넷. GitHub 로그인·API 키·추가 Python 패키지는 필요 없다. `gh`는 목록을 갱신하는 관리용 스크립트에서만 사용한다.

skills 레포 루트에서:

```bash
./clone-hackathon-references.sh
```

기본 위치: `~/hackathon-reference/`. HTTPS shallow clone으로 현재 branch의 소스를 받으며, 기본 동시 작업 수는 6이다. 2026-10-31 실제 준비에서는 약 **24 GiB**를 사용했다. 기존 레포는 수정하거나 pull하지 않고 원격 주소를 확인해 건너뛴다. 실패한 clone은 상태와 로그를 남기고 다른 레포를 계속 받는다. 다시 실행하면 빠진 레포를 재시도한다.

기본 실행은 공개 **UCI SECOM 데이터와 NIST PDF 2개**도 수집한다. 원문 출처·파일 SHA·실제 shape는 설치 폴더에 기록한다. 모델 가중치·Git LFS 파일·submodule·런타임 의존성은 별도 준비 대상이다. 패키지 설치나 외부 서비스 등록은 실행하지 않는다.

### 시간이 짧거나 디스크가 작은 환경

```bash
# 전체 후보 목록만 조회: clone/다운로드 없음
./clone-hackathon-references.sh --list

# P0 후보만 받기 (필요한 분야별로 더 줄일 수 있음)
./clone-hackathon-references.sh --priority P0 --jobs 4

# 스킬·반도체 데이터·메모리 시뮬레이션만
./clone-hackathon-references.sh --category 01- --category 16- --category 17-

# 제조 분석 중심
./clone-hackathon-references.sh --category 07- --category 08- --category 09- --category 10-

# 저장 위치 변경, PDF·데이터 다운로드 생략
./clone-hackathon-references.sh --dest "$HOME/hackathon-reference" --jobs 4 --skip-materials
```

`--priority P1`은 P0+P1, P2는 전체를 뜻한다. `--category`는 분야 문자열 일부로 필터링하며 여러 번 지정하면 합집합이다. 전체 카탈로그가 있어도 실제 받은 레포만 로컬 색인에 들어간다.

## 에이전트에 주는 첫 요청

설치 후 대회 프로젝트에서 다음처럼 지시한다. sandbox에서 HOME이나 clone 경로가 다르면 실제 경로로 바꾼다.

```text
~/hackathon-reference/AGENTS.md와 COFA_AGENT_INSTRUCTIONS.md를 먼저 읽어줘.
실제 과제와 README를 확인해서 완료 조건을 정리하고, 필요한 자료만 골라 참고해.
목표에 맞는 가장 작은 동작 흐름을 구현한 뒤 실제 실행으로 검증해줘.
중요한 결정과 검증 결과는 실제 파일·함수·로그에 연결해서 짧게 남겨줘.
내가 제출물의 동작·선택 이유·실패 조건을 이해할 수 있게 설명해줘.
```

대회 프로젝트 AGENTS.md가 이미 있으면 지침을 필요한 부분만 합친다. 템플릿은 `templates/`에 있으며 모든 파일을 만들 필요는 없다.

## 로컬 자료 검색

```bash
cd ~/hackathon-reference
python3 scripts/search.py '수율'
python3 scripts/search.py 'wafer'
python3 scripts/search.py --skills 'frontend'
python3 scripts/search.py --skills 'pdf' --limit 10
rg -n '이상|메모리|HBM' CATALOG.md
```

- `LOCAL_INDEX.json`: 실제 레포 위치·commit SHA·존재하는 README/docs/examples 경로.
- `SKILLS_INDEX.md` / `.json`: checkout에서 발견한 SKILL.md 파일의 이름·설명·경로. 번역·중복·예제도 있어 고유 스킬 수를 뜻하지 않는다.
- `CLONE_STATUS.json` / `logs/`: clone 성공·실패·기존 레포와 상세 로그.
- `MATERIALS_STATUS.json`: PDF·데이터 다운로드 결과, 출처, SHA-256.
- `datasets/secom/PROVENANCE.json`: 실제 원본 데이터 shape·라벨 분포·결측 수.

스킬을 전부 읽거나 전역 설치하지 않는다. 관련 스킬을 골라 읽고, 실행이 필요한 경우 README와 상대경로 의존 자료를 확인한다.

## 이 키트를 찾는 Codex 스킬

자체 작성한 `hackathon-reference` 스킬은 `skill/hackathon-reference/`에 있다. 현재 준비 머신에서는 `~/.codex/skills/hackathon-reference/`에도 배치했다. 새 머신에서 원하면 다음처럼 복사한다.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ~/hackathon-reference/skill/hackathon-reference "${CODEX_HOME:-$HOME/.codex}/skills/"
```

새 세션에서 `$hackathon-reference`로 요청할 수 있다. 기본 라이브러리 위치를 바꿨다면 `HACKATHON_REFERENCE_HOME`으로 실제 경로를 알려준다. 다른 에이전트는 AGENTS.md와 실행 지침을 직접 읽으면 된다. 외부 레포에 들어 있는 수천 개 스킬은 자동 설치하지 않는다.

## 갱신·재사용

이 skills 레포에는 목록·가이드·스크립트만 보관한다. 수십 GB의 외부 clone은 `~/hackathon-reference/`에 따로 둔다. 다른 컴퓨터에서는 이 레포를 clone한 다음 동일한 준비 스크립트를 실행한다.

```bash
# 설치 폴더의 가이드와 색인만 갱신, clone/다운로드 안 함
./clone-hackathon-references.sh --index-only

# 공개 PDF·SECOM만 따로 준비
python3 hackathon-kit/scripts/fetch_materials.py

# 관리용: GitHub 메타데이터 재조회 (gh 로그인 필요)
python3 hackathon-kit/scripts/verify_repositories.py
python3 hackathon-kit/scripts/build_catalog.py
```

이 패키지에서 다시 실행하면 배포용 가이드·스크립트 사본을 설치 폴더에 갱신한다. 개인 작업·메모는 별도 프로젝트에 둔다. 기존 clone은 자동 업데이트하지 않으며 실제 사용 버전은 LOCAL_INDEX.json의 SHA로 구별한다.

공식 대회 상세 배점은 확인하지 못했다. 사용자 제공 글은 별도 Cofathon 참가 후기이며, 준비 전략과 공식 사실을 문서에서 구분했다. 어떤 문서·행동도 득점을 보장하지 않는다.
