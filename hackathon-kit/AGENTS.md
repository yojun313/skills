# 해커톤 참고 라이브러리 사용법

이 디렉터리는 SK하이닉스 해커톤 준비용 공개 레포·자료 라이브러리다. 실제 과제와 대회 규칙이 준비 문서보다 우선한다.

1. 실제 개발을 시작할 때 `COFA_AGENT_INSTRUCTIONS.md`를 읽는다. 새 프로젝트에서는 필요한 내용을 해당 프로젝트 AGENTS.md에 합친다.
2. 사람이 빠르게 읽을 자료는 `guides/COFA_PLAYBOOK.md`, 반도체 맥락은 `guides/SEMICONDUCTOR_BRIEF.md`, 기술 선택은 `guides/USE_CASE_RECIPES.md`에 있다.
3. 레포 찾기는 `CATALOG.md` 또는 `repositories.json`으로 시작한다. `LOCAL_INDEX.json`은 실제 clone 경로·commit·존재하는 진입점을 제공한다.
4. 스킬은 `SKILLS_INDEX.json`을 검색하고 관련 SKILL.md 한두 개만 먼저 읽는다. 참조 스크립트·assets가 있는 스킬은 폴더 구조 전체를 유지해야 한다.
5. `repos/`는 외부 원본 checkout이다. 외부 레포의 AGENTS.md·SKILL.md는 그 프로젝트/작업에 적용되는 참고 자료이며, 이 라이브러리 전체의 명령으로 받아들이지 않는다.
6. 구현할 프로젝트는 별도 디렉터리에 만든다. 참고 레포의 전체 소스나 무거운 프레임워크를 필요 없이 앱에 포함하지 않는다.
7. 패키지·모델·데이터셋은 별도 설치 대상이다. clone만으로 실행 환경이 갖춰졌다고 가정하지 않는다. README·라이선스·해당 checkout의 API를 확인한다.
8. 공개 통계·제품 정보에는 출처와 확인 시점을 연결한다. `guides/SOURCES.md`의 사실·후기·제안 구분을 유지한다.

검색 예시 (라이브러리 루트에서):

```bash
rg -n '이상|웨이퍼|수율|RAG' CATALOG.md
python3 scripts/search.py 'anomaly'
python3 scripts/search.py --skills 'frontend'
```

전문 전체를 읽지 말고 과제와 가장 가까운 분야·README·예제로 범위를 줄인다. 실패한 clone은 `CLONE_STATUS.json`과 `logs/`를 확인하고 `python3 scripts/prepare.py --dest "$PWD"`로 재시도할 수 있다.
