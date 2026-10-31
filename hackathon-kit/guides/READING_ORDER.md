# 오늘 준비 순서

## 시간이 15분이면

1. COFA_PLAYBOOK.md의 다섯 가지와 평가 관점 표를 읽는다.
2. SEMICONDUCTOR_BRIEF.md의 제품 구분·데이터 용어를 본다.
3. 첫 프롬프트와 COFA_AGENT_INSTRUCTIONS.md의 경로를 준비한다.
4. 아래 실행으로 키트가 있는지 확인한다.

```bash
python3 ~/hackathon-reference/scripts/search.py '이상'
python3 ~/hackathon-reference/scripts/search.py --skills 'frontend'
```

## 시간이 1시간이면 — 연습 제안

- 10분: 위 문서 확인, 기술 스택 하나 선택.
- 25분: 공개 SECOM 또는 직접 만든 작은 CSV로 업로드 → 요약 → 결과 화면을 끝까지 구현.
- 15분: 잘못된 CSV·빈 입력·실제 출력 수치 확인. 실행 방법 기록.
- 10분: 입력부터 결과까지 본인 말로 설명. 가장 큰 한계와 확인 방법을 답해 보기.

실제 예측 모델 학습까지 하려면 전처리와 데이터 분할부터 잡는다. 시간 안에 못 하면 데이터 탐색·리뷰 흐름까지만 완성하고 모델은 미구현으로 명시한다.

## 내일 시작 전

대회 안내에서 사전 코드·외부 clone·설치·네트워크·모델·확인 문항 규칙을 확인한다. 이 키트의 기본 준비는 공개 레포와 자료를 읽기 위한 것이다. 기본 clone에는 전체 tip 소스가 포함되지만 LFS 파일·submodule·모델 가중치·패키지 의존성은 포함되지 않는다.

공유 라이브러리 수십 GB를 모두 여는 대신 문제 유형을 보고 `USE_CASE_RECIPES.md`와 `CATALOG.md`에서 2~3개 레포만 고른다. 데이터·API 접근이 실제로 가능한지 확인한 다음 구현한다.
