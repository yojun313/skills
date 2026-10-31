# 문제 유형별로 먼저 볼 레포

아래 선택은 빠른 구현을 위한 준비 제안이다. 목록이 많아도 앱 하나에는 익숙한 스택과 필요한 도구만 고른다. 정식 레포 이름과 로컬 경로는 `../CATALOG.md`, 실제 파일 위치는 `../LOCAL_INDEX.json`에 있다.

| 상황 | 먼저 볼 조합 | 시작할 곳 | 먼저 확인할 결과 |
| --- | --- | --- | --- |
| 시간 짧은 데이터 앱 | Streamlit + DuckDB/Polars + Plotly | 각 README와 examples | 업로드 → 변환 → 표/그래프 |
| 정형 불량 예측 | scikit-learn + CatBoost 또는 LightGBM + SHAP | examples·pipeline·model persistence | 학습/평가 분리와 baseline |
| 센서 이상 탐지 | tsfresh + PyOD + Plotly | feature extraction·model examples | 시간 구간별 점수·알람량 |
| 새 데이터가 계속 옴 | River + MQTT client | online examples·client examples | 이벤트 수신 → 점수 → 화면 |
| 통계적 시계열 예측 | StatsForecast | docs·examples | naive baseline 대비 미래 구간 오차 |
| pretrained 시계열 | Chronos 또는 TimesFM | inference notebook | GPU/메모리·사용 조건·적용 단위 |
| 정상 이미지 위주 검사 | anomalib + PatchCore | examples·config·dataset module | 이미지별 점수와 결함 위치 |
| 결함 검출·분류 | Ultralytics + Supervision | detection/classification examples | 라벨 체계·실제 이미지 추론 |
| 웨이퍼 검사 파일 | klarfkit + Plotly | README·examples·tests | 좌표/단위 보존한 웨이퍼 맵 |
| PDF 검색 보조 | Docling + sentence-transformers + Qdrant | conversion·embedding·quickstart | 인용 근거와 답변할 수 없는 질의 |
| PDF 텍스트가 깨짐 | pdfplumber → PaddleOCR | text/table extraction·OCR examples | 원문 표와 추출 결과 대조 |
| 긴 작업·재시도 필요 | LangGraph 또는 PydanticAI | quickstart·examples | 상태 전환·실패 복구 |
| 웹 기반 AI 서비스 | Vite/Next.js + shadcn/ui + AI SDK | templates·examples·components | 실제 API와 연결된 주 흐름 |
| Python API + DB | FastAPI + Pydantic + SQLModel | tutorial·full-stack template | 검증·저장·에러 응답 |
| 일정/자원 제약 | OR-Tools CP-SAT | scheduling examples | 제약 위반 0건, 목적함수 비교 |
| 병목 설명 | DuckDB + pm4py + SimPy | process discovery·resource examples | event 순서·대기시간·가정 |
| 실험 조건 최적화 | Optuna 또는 pymoo | objective·multi-objective examples | 비용/시간·허용 범위·재현 seed |
| 인과 후보 분석 | DoWhy + causal-learn | causal model·refutation examples | 인과 가정과 예측 기여도의 구분 |
| HBM/DRAM trace | Ramulator2·DRAMsim3 | config·trace·README | 같은 workload의 지연·대역폭 비교 |
| SSD 성능·큐잉 | MQSim | configuration·workload examples | trace·큐 깊이·latency 분포 |
| RTL 검증 | cocotb + Verilator | examples·tests | 작은 DUT의 실제 simulation |
| LLM 평가 | promptfoo 또는 Ragas | config examples·testsets | 고정된 질문/기대 결과 회귀 |
| 실제 브라우저 검증 | Playwright | tests·trace viewer | 사용자 핵심 흐름의 E2E |
| 발표/설명 | Mermaid + Plotly + Slidev | syntax/examples·starter | 구조·검증 결과·한계가 보임 |

## 스킬 모음에서 골라 보기

- 일반 문서·디자인·브라우저 테스트: anthropics/skills.
- React·웹 UI 작업: vercel-labs/agent-skills.
- 모델·데이터셋·학습 작업: huggingface/skills.
- Azure가 과제에서 제공될 때: microsoft/skills.
- SDK·툴·플러그인 워크플로 참고: openai/plugins와 openai/skills.
- 개발 계획·디버깅 방식 비교: obra/superpowers.
- 구체적 기술별 instructions/prompts 탐색: github/awesome-copilot.

이 명칭은 코드/스킬을 찾을 출발점이다. 실제 스킬 이름·경로는 현재 checkout에서 만든 `SKILLS_INDEX.md`에 있다. 원본 스킬을 전부 설치하거나 불필요한 외부 서비스를 연결할 필요는 없다.

## 선택 전에 1분 확인

README의 최소 예제가 현재 환경에서 가능한가? API 키·GPU·모델 파일이 필요한가? 사용하려는 부분의 라이선스는? 기존 프로젝트와 버전이 맞는가? 더 작은 패키지나 제공된 스택으로 같은 결과를 만들 수 있는가?

P0는 먼저 살펴볼 후보, P1은 상황별 대안, P2는 전문 연구·학습 또는 도입 비용이 큰 참조다. 품질 점수나 대회 공식 우선순위가 아니다. 보관 레포도 참고용으로 남겼으며 새 프로젝트의 첫 선택에서는 유지 상태를 확인한다.
