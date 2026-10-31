# 해커톤 공개 레포 카탈로그

GitHub 메타데이터 확인: 2026-10-30T16:02:19.266139+00:00 · 레포 153개 · 19개 분야.

P0: 먼저 살펴볼 후보 / P1: 상황별 대안 / P2: 전문 연구·학습 또는 도입 비용이 큰 참조. 공식 순위가 아닌 준비용 분류다.
별 수·라이선스 표시는 스냅샷이며, 혼합 라이선스와 모델·데이터의 개별 조건은 원본에서 확인한다. NOASSERTION/UNKNOWN은 사용 허가를 뜻하지 않는다.
로컬 링크는 기본 설치 루트 ~/hackathon-reference/ 기준이다. 실제 README·예제 경로와 clone한 commit은 LOCAL_INDEX.json, 실패 여부는 CLONE_STATUS.json에 있다.

| 분야 | 개수 |
| --- | --- |
| 01-agent-skills: 에이전트 스킬·작업 지침 | 11 |
| 02-llm-agents: LLM 에이전트·워크플로 | 9 |
| 03-rag-search: RAG·임베딩·검색 | 11 |
| 04-document-ocr: 문서 처리·OCR | 8 |
| 05-web-ui: 웹앱·데모 UI | 11 |
| 06-api-backend: API·백엔드 | 6 |
| 07-tabular-ml: 정형 데이터·머신러닝 | 10 |
| 08-timeseries-anomaly: 시계열·이상 탐지 | 10 |
| 09-industrial-vision: 산업 비전·영상 검사 | 9 |
| 10-manufacturing-optimization: 제조 최적화·통계·인과 | 9 |
| 11-local-llm: 로컬 모델·추론·미세조정 | 7 |
| 12-eval-observability: 평가·실험·관측 | 7 |
| 13-automation-mcp: 브라우저 자동화·MCP | 7 |
| 14-visualization-presentation: 시각화·발표 | 6 |
| 15-cookbooks-learning: 공식 예제·학습 자료 | 6 |
| 16-semiconductor-data: 반도체 데이터·웨이퍼 검사 | 7 |
| 17-memory-storage-simulation: DRAM·HBM·SSD 시뮬레이션 | 9 |
| 18-eda-hardware: EDA·하드웨어 검증 | 8 |
| 19-industrial-integration: 산업 센서·장비 연동 | 2 |

## 01-agent-skills — 에이전트 스킬·작업 지침

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) · [로컬](repos/01-agent-skills/anthropics__skills/) | P0 | 문서·프런트엔드·테스트 등 작업별 SKILL.md 예제와 보조 스크립트 | 185,063 | UNKNOWN | 공개 |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) · [로컬](repos/01-agent-skills/agentskills__agentskills/) | P1 | 에이전트 스킬 규격과 참조 도구; 스킬 구조를 확인할 때 | 26,796 | Apache-2.0 | 공개 |
| [openai/skills](https://github.com/openai/skills) · [로컬](repos/01-agent-skills/openai__skills/) | P1 | Codex 스킬 구조와 공식 예제; 보관 상태 및 대체 경로 확인 | 28,414 | UNKNOWN | 공개 |
| [openai/plugins](https://github.com/openai/plugins) · [로컬](repos/01-agent-skills/openai__plugins/) | P0 | OpenAI 공식 플러그인과 포함된 스킬·워크플로 참조 | 7,670 | UNKNOWN | 공개 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · [로컬](repos/01-agent-skills/vercel-labs__agent-skills/) | P0 | React·웹 디자인 관련 에이전트 작업 지침 | 33,249 | UNKNOWN | 공개 |
| [huggingface/skills](https://github.com/huggingface/skills) · [로컬](repos/01-agent-skills/huggingface__skills/) | P0 | 모델·데이터셋·평가·학습 관련 Hugging Face 작업 스킬 | 11,238 | Apache-2.0 | 공개 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) · [로컬](repos/01-agent-skills/github__awesome-copilot/) | P1 | 재사용 가능한 instructions·prompts·agents·skills 모음 | 40,597 | MIT | 공개 |
| [microsoft/skills](https://github.com/microsoft/skills) · [로컬](repos/01-agent-skills/microsoft__skills/) | P1 | Azure SDK·AI 서비스 관련 작업 스킬과 예제 | 3,157 | MIT | 공개 |
| [obra/superpowers](https://github.com/obra/superpowers) · [로컬](repos/01-agent-skills/obra__superpowers/) | P1 | 계획·디버깅·검증 중심 개발 워크플로 스킬 | 309,222 | MIT | 공개 |
| [trailofbits/skills](https://github.com/trailofbits/skills) · [로컬](repos/01-agent-skills/trailofbits__skills/) | P2 | 코드 검토와 보안 분석용 전문 스킬 | 7,892 | CC-BY-SA-4.0 | 공개 |
| [databricks/databricks-agent-skills](https://github.com/databricks/databricks-agent-skills) · [로컬](repos/01-agent-skills/databricks__databricks-agent-skills/) | P2 | Databricks 데이터·SQL·분석 작업용 스킬 | 378 | NOASSERTION | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 02-llm-agents — LLM 에이전트·워크플로

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) · [로컬](repos/02-llm-agents/langchain-ai__langgraph/) | P0 | 상태와 분기·재시도를 가진 에이전트 워크플로 | 44,167 | MIT | 공개 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) · [로컬](repos/02-llm-agents/langchain-ai__langchain/) | P1 | 모델·도구·retriever 통합 예제 | 148,715 | MIT | 공개 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) · [로컬](repos/02-llm-agents/pydantic__pydantic-ai/) | P0 | 타입이 있는 출력과 도구 호출 중심 Python 에이전트 | 20,956 | MIT | 공개 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) · [로컬](repos/02-llm-agents/stanfordnlp__dspy/) | P1 | LLM 파이프라인을 평가 지표로 개선하는 실험 | 38,857 | MIT | 공개 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) · [로컬](repos/02-llm-agents/openai__openai-agents-python/) | P1 | 도구 호출·handoff·tracing 기반 에이전트 SDK | 30,394 | MIT | 공개 |
| [google/adk-python](https://github.com/google/adk-python) · [로컬](repos/02-llm-agents/google__adk-python/) | P1 | Google Agent Development Kit의 도구·워크플로 예제 | 22,049 | Apache-2.0 | 공개 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) · [로컬](repos/02-llm-agents/huggingface__smolagents/) | P1 | 코드 실행 기반의 경량 에이전트 예제 | 30,149 | Apache-2.0 | 공개 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) · [로컬](repos/02-llm-agents/crewAIInc__crewAI/) | P2 | 역할별 에이전트 협업 프레임워크 비교 | 60,299 | MIT | 공개 |
| [microsoft/autogen](https://github.com/microsoft/autogen) · [로컬](repos/02-llm-agents/microsoft__autogen/) | P2 | 대화형 에이전트 협업 설계와 기존 예제 | 61,633 | CC-BY-4.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 03-rag-search — RAG·임베딩·검색

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) · [로컬](repos/03-rag-search/run-llama__llama_index/) | P0 | 문서 인덱싱·검색·질의 파이프라인 예제 | 52,743 | MIT | 공개 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) · [로컬](repos/03-rag-search/deepset-ai__haystack/) | P1 | 컴포넌트 기반 검색·RAG 파이프라인 | 26,885 | Apache-2.0 | 공개 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) · [로컬](repos/03-rag-search/infiniflow__ragflow/) | P1 | 문서 처리부터 검색·대화 UI까지 통합 RAG 구현 | 93,195 | Apache-2.0 | 공개 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) · [로컬](repos/03-rag-search/microsoft__graphrag/) | P2 | 엔터티 관계와 그래프 요약을 사용하는 검색 | 36,498 | MIT | 공개 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · [로컬](repos/03-rag-search/HKUDS__LightRAG/) | P1 | 그래프를 결합한 경량 RAG 구현 | 40,441 | MIT | 공개 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) · [로컬](repos/03-rag-search/qdrant__qdrant/) | P0 | 벡터 검색 서버와 필터링 설계 | 35,334 | Apache-2.0 | 공개 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) · [로컬](repos/03-rag-search/chroma-core__chroma/) | P1 | 로컬 프로토타입용 임베딩 저장·검색 | 29,607 | Apache-2.0 | 공개 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) · [로컬](repos/03-rag-search/pgvector__pgvector/) | P1 | PostgreSQL 안에서 벡터 유사도 검색 | 23,535 | NOASSERTION | 공개 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) · [로컬](repos/03-rag-search/facebookresearch__faiss/) | P1 | 로컬 대규모 벡터 유사도 검색 | 41,235 | MIT | 공개 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) · [로컬](repos/03-rag-search/huggingface__sentence-transformers/) | P0 | 문장 임베딩과 cross-encoder 재순위화 | 19,237 | Apache-2.0 | 공개 |
| [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) · [로컬](repos/03-rag-search/FlagOpen__FlagEmbedding/) | P1 | BGE 임베딩과 reranker 모델 활용 | 12,288 | MIT | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 04-document-ocr — 문서 처리·OCR

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [docling-project/docling](https://github.com/docling-project/docling) · [로컬](repos/04-document-ocr/docling-project__docling/) | P0 | PDF·표·레이아웃을 구조화하는 문서 파싱 | 69,872 | MIT | 공개 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) · [로컬](repos/04-document-ocr/Unstructured-IO__unstructured/) | P1 | 여러 문서 형식에서 요소를 추출하는 ETL | 15,645 | Apache-2.0 | 공개 |
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) · [로컬](repos/04-document-ocr/jsvine__pdfplumber/) | P0 | PDF 텍스트·표·좌표 기반 추출과 디버깅 | 10,856 | MIT | 공개 |
| [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) · [로컬](repos/04-document-ocr/pymupdf__PyMuPDF/) | P1 | PDF 렌더링·텍스트·이미지 처리; 라이선스 확인 | 11,026 | AGPL-3.0 | 공개 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) · [로컬](repos/04-document-ocr/PaddlePaddle__PaddleOCR/) | P0 | 스캔 문서·이미지 OCR와 문서 이해 | 91,993 | Apache-2.0 | 공개 |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) · [로컬](repos/04-document-ocr/tesseract-ocr__tesseract/) | P1 | CPU 기반 OCR 엔진과 언어 데이터 연동 | 77,248 | Apache-2.0 | 공개 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) · [로컬](repos/04-document-ocr/opendatalab__MinerU/) | P1 | 복잡한 PDF를 구조화된 문서로 변환 | 82,814 | NOASSERTION | 공개 |
| [datalab-to/marker](https://github.com/datalab-to/marker) · [로컬](repos/04-document-ocr/datalab-to__marker/) | P2 | PDF에서 Markdown·구조화 데이터로 변환 | 40,708 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 05-web-ui — 웹앱·데모 UI

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [vercel/next.js](https://github.com/vercel/next.js) · [로컬](repos/05-web-ui/vercel__next.js/) | P1 | React 기반 웹앱 구현과 공식 examples | 143,212 | MIT | 공개 |
| [vitejs/vite](https://github.com/vitejs/vite) · [로컬](repos/05-web-ui/vitejs__vite/) | P0 | 빠른 프런트엔드 개발 환경과 템플릿 | 83,625 | MIT | 공개 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) · [로컬](repos/05-web-ui/shadcn-ui__ui/) | P0 | 대시보드·폼·대화창 UI 컴포넌트 패턴 | 126,965 | MIT | 공개 |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) · [로컬](repos/05-web-ui/tailwindlabs__tailwindcss/) | P1 | 유틸리티 CSS 기반 스타일링 | 98,019 | MIT | 공개 |
| [vercel/ai](https://github.com/vercel/ai) · [로컬](repos/05-web-ui/vercel__ai/) | P0 | 스트리밍·도구 호출을 포함한 TypeScript AI UI | 27,626 | NOASSERTION | 공개 |
| [vercel/chatbot](https://github.com/vercel/chatbot) · [로컬](repos/05-web-ui/vercel__chatbot/) | P1 | AI 채팅 웹앱 템플릿; 이전·보관 상태 확인 | 21,019 | NOASSERTION | 공개 |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) · [로컬](repos/05-web-ui/fastapi__full-stack-fastapi-template/) | P0 | FastAPI·DB·프런트엔드를 묶은 풀스택 템플릿 | 46,119 | MIT | 공개 |
| [supabase/supabase](https://github.com/supabase/supabase) · [로컬](repos/05-web-ui/supabase__supabase/) | P1 | Postgres·인증·스토리지 결합 백엔드 참조 | 114,341 | Apache-2.0 | 공개 |
| [streamlit/streamlit](https://github.com/streamlit/streamlit) · [로컬](repos/05-web-ui/streamlit__streamlit/) | P0 | Python만으로 데이터 분석·AI 데모 UI 제작 | 46,167 | Apache-2.0 | 공개 |
| [gradio-app/gradio](https://github.com/gradio-app/gradio) · [로컬](repos/05-web-ui/gradio-app__gradio/) | P0 | 모델 추론·이미지·대화형 데모 UI 제작 | 43,933 | Apache-2.0 | 공개 |
| [plotly/dash](https://github.com/plotly/dash) · [로컬](repos/05-web-ui/plotly__dash/) | P1 | Python 데이터 대시보드와 콜백 구성 | 24,473 | MIT | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 06-api-backend — API·백엔드

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) · [로컬](repos/06-api-backend/fastapi__fastapi/) | P0 | 입력 검증과 OpenAPI를 갖춘 Python API | 104,280 | MIT | 공개 |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) · [로컬](repos/06-api-backend/pydantic__pydantic/) | P0 | 데이터 스키마와 구조화 출력 검증 | 29,237 | MIT | 공개 |
| [fastapi/sqlmodel](https://github.com/fastapi/sqlmodel) · [로컬](repos/06-api-backend/fastapi__sqlmodel/) | P1 | Pydantic·SQLAlchemy 연계 DB 모델 | 18,507 | MIT | 공개 |
| [encode/httpx](https://github.com/encode/httpx) · [로컬](repos/06-api-backend/encode__httpx/) | P1 | 동기·비동기 HTTP 클라이언트와 타임아웃 | 15,705 | BSD-3-Clause | 공개 |
| [expressjs/express](https://github.com/expressjs/express) · [로컬](repos/06-api-backend/expressjs__express/) | P1 | 경량 Node.js API 서버 | 69,578 | MIT | 공개 |
| [nestjs/nest](https://github.com/nestjs/nest) · [로컬](repos/06-api-backend/nestjs__nest/) | P2 | 모듈화된 TypeScript 백엔드 구조 | 76,948 | MIT | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 07-tabular-ml — 정형 데이터·머신러닝

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [pola-rs/polars](https://github.com/pola-rs/polars) · [로컬](repos/07-tabular-ml/pola-rs__polars/) | P0 | 빠른 CSV·Parquet 처리와 lazy 데이터 변환 | 40,235 | MIT | 공개 |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) · [로컬](repos/07-tabular-ml/duckdb__duckdb/) | P0 | 파일을 직접 SQL로 분석하는 로컬 분석 DB | 42,688 | MIT | 공개 |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) · [로컬](repos/07-tabular-ml/scikit-learn__scikit-learn/) | P0 | 전처리·교차검증·분류·회귀의 기본 baseline | 67,926 | BSD-3-Clause | 공개 |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) · [로컬](repos/07-tabular-ml/dmlc__xgboost/) | P0 | 정형 센서·공정 데이터용 부스팅 baseline | 28,927 | Apache-2.0 | 공개 |
| [lightgbm-org/LightGBM](https://github.com/lightgbm-org/LightGBM) · [로컬](repos/07-tabular-ml/lightgbm-org__LightGBM/) | P0 | 대용량 정형 데이터의 빠른 부스팅 | 18,940 | MIT | 공개 |
| [catboost/catboost](https://github.com/catboost/catboost) · [로컬](repos/07-tabular-ml/catboost__catboost/) | P0 | 장비·공정·제품 등 범주형 변수가 많은 예측 | 9,184 | Apache-2.0 | 공개 |
| [autogluon/autogluon](https://github.com/autogluon/autogluon) · [로컬](repos/07-tabular-ml/autogluon__autogluon/) | P1 | 정형 데이터·시계열 AutoML baseline | 10,803 | Apache-2.0 | 공개 |
| [shap/shap](https://github.com/shap/shap) · [로컬](repos/07-tabular-ml/shap__shap/) | P0 | 예측 기여도와 오류 사례 해석; 인과와 구분 | 25,840 | MIT | 공개 |
| [Data-Centric-AI-Community/fg-data-profiling](https://github.com/Data-Centric-AI-Community/fg-data-profiling) · [로컬](repos/07-tabular-ml/Data-Centric-AI-Community__fg-data-profiling/) | P1 | 결측·분포·데이터 품질을 빠르게 탐색 | 13,746 | MIT | 공개 |
| [scikit-learn-contrib/imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn) · [로컬](repos/07-tabular-ml/scikit-learn-contrib__imbalanced-learn/) | P0 | 희소 불량 클래스의 재표집·분류; 학습 fold 내부에서만 적용 | 7,135 | MIT | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 08-timeseries-anomaly — 시계열·이상 탐지

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [unit8co/darts](https://github.com/unit8co/darts) · [로컬](repos/08-timeseries-anomaly/unit8co__darts/) | P1 | 여러 시계열 예측 모델을 같은 API로 비교 | 9,567 | Apache-2.0 | 공개 |
| [sktime/sktime](https://github.com/sktime/sktime) · [로컬](repos/08-timeseries-anomaly/sktime__sktime/) | P1 | 시계열 예측·분류·변환 도구 | 10,082 | BSD-3-Clause | 공개 |
| [Nixtla/statsforecast](https://github.com/Nixtla/statsforecast) · [로컬](repos/08-timeseries-anomaly/Nixtla__statsforecast/) | P0 | 통계 기반 시계열 예측 baseline | 4,956 | Apache-2.0 | 공개 |
| [Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast) · [로컬](repos/08-timeseries-anomaly/Nixtla__neuralforecast/) | P1 | 딥러닝 시계열 예측 모델 모음 | 4,301 | Apache-2.0 | 공개 |
| [blue-yonder/tsfresh](https://github.com/blue-yonder/tsfresh) · [로컬](repos/08-timeseries-anomaly/blue-yonder__tsfresh/) | P0 | 센서 시계열에서 통계 특징 추출 | 9,482 | MIT | 공개 |
| [ymirsky/KitNET-py](https://github.com/ymirsky/KitNET-py) · [로컬](repos/08-timeseries-anomaly/ymirsky__KitNET-py/) | P2 | 온라인 비지도 이상 탐지의 경량 구현 참고 | 262 | MIT | 공개 |
| [yzhao062/pyod](https://github.com/yzhao062/pyod) · [로컬](repos/08-timeseries-anomaly/yzhao062__pyod/) | P0 | Isolation Forest 등 이상 탐지 모델 비교 | 10,064 | BSD-2-Clause | 공개 |
| [amazon-science/chronos-forecasting](https://github.com/amazon-science/chronos-forecasting) · [로컬](repos/08-timeseries-anomaly/amazon-science__chronos-forecasting/) | P1 | 사전학습 시계열 모델을 통한 빠른 예측 | 6,209 | Apache-2.0 | 공개 |
| [google-research/timesfm](https://github.com/google-research/timesfm) · [로컬](repos/08-timeseries-anomaly/google-research__timesfm/) | P1 | 시계열 파운데이션 모델 활용 | 34,839 | Apache-2.0 | 공개 |
| [online-ml/river](https://github.com/online-ml/river) · [로컬](repos/08-timeseries-anomaly/online-ml__river/) | P1 | 스트리밍 센서 데이터의 온라인 학습·드리프트 탐지 | 6,137 | BSD-3-Clause | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 09-industrial-vision — 산업 비전·영상 검사

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [open-edge-platform/anomalib](https://github.com/open-edge-platform/anomalib) · [로컬](repos/09-industrial-vision/open-edge-platform__anomalib/) | P0 | 산업 이미지 이상 탐지·결함 위치 추정 | 6,341 | Apache-2.0 | 공개 |
| [amazon-science/patchcore-inspection](https://github.com/amazon-science/patchcore-inspection) · [로컬](repos/09-industrial-vision/amazon-science__patchcore-inspection/) | P0 | 정상 이미지 중심 PatchCore 산업 검사 구현 | 1,430 | Apache-2.0 | 공개 |
| [facebookresearch/sam2](https://github.com/facebookresearch/sam2) · [로컬](repos/09-industrial-vision/facebookresearch__sam2/) | P1 | 이미지·영상 세그멘테이션 모델 | 20,080 | Apache-2.0 | 공개 |
| [IDEA-Research/GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) · [로컬](repos/09-industrial-vision/IDEA-Research__GroundingDINO/) | P1 | 텍스트 조건을 활용한 객체 검출 | 10,721 | Apache-2.0 | 공개 |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) · [로컬](repos/09-industrial-vision/ultralytics__ultralytics/) | P0 | 이미지 결함 검출·분류·세그멘테이션 baseline | 62,986 | AGPL-3.0 | 공개 |
| [roboflow/supervision](https://github.com/roboflow/supervision) · [로컬](repos/09-industrial-vision/roboflow__supervision/) | P0 | 검출 결과 후처리·시각화·추적 도구 | 51,436 | MIT | 공개 |
| [opencv/opencv](https://github.com/opencv/opencv) · [로컬](repos/09-industrial-vision/opencv__opencv/) | P0 | 영상 전처리·형상·이미지 측정 기본 도구 | 91,386 | Apache-2.0 | 공개 |
| [albumentations-team/albumentations](https://github.com/albumentations-team/albumentations) · [로컬](repos/09-industrial-vision/albumentations-team__albumentations/) | P1 | 영상 데이터 증강; 보관·대체 경로 확인 | 15,306 | MIT | 보관(archived) |
| [huggingface/pytorch-image-models](https://github.com/huggingface/pytorch-image-models) · [로컬](repos/09-industrial-vision/huggingface__pytorch-image-models/) | P1 | 사전학습 이미지 분류 backbone 활용 | 37,261 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 10-manufacturing-optimization — 제조 최적화·통계·인과

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [google/or-tools](https://github.com/google/or-tools) · [로컬](repos/10-manufacturing-optimization/google__or-tools/) | P0 | 생산 스케줄링·배치·자원 제약 최적화 | 14,303 | Apache-2.0 | 공개 |
| [anyoptimization/pymoo](https://github.com/anyoptimization/pymoo) · [로컬](repos/10-manufacturing-optimization/anyoptimization__pymoo/) | P1 | 수율·비용·시간의 다목적 최적화 | 2,984 | Apache-2.0 | 공개 |
| [optuna/optuna](https://github.com/optuna/optuna) · [로컬](repos/10-manufacturing-optimization/optuna__optuna/) | P0 | 하이퍼파라미터·실험 조건 탐색 | 14,994 | MIT | 공개 |
| [simpx/simpy](https://github.com/simpx/simpy) · [로컬](repos/10-manufacturing-optimization/simpx__simpy/) | P1 | 장비 대기열·공정 흐름 이산사건 시뮬레이션 | 52 | MIT | 공개 |
| [pgmpy/pgmpy](https://github.com/pgmpy/pgmpy) · [로컬](repos/10-manufacturing-optimization/pgmpy__pgmpy/) | P1 | 확률 그래프와 조건부 추론 | 3,365 | MIT | 공개 |
| [py-why/dowhy](https://github.com/py-why/dowhy) · [로컬](repos/10-manufacturing-optimization/py-why__dowhy/) | P1 | 관측 데이터의 인과 가정과 반증 분석 | 8,383 | MIT | 공개 |
| [py-why/causal-learn](https://github.com/py-why/causal-learn) · [로컬](repos/10-manufacturing-optimization/py-why__causal-learn/) | P2 | 인과 구조 탐색 알고리즘 비교 | 1,707 | MIT | 공개 |
| [process-intelligence-solutions/pm4py](https://github.com/process-intelligence-solutions/pm4py) · [로컬](repos/10-manufacturing-optimization/process-intelligence-solutions__pm4py/) | P1 | 이벤트 로그를 활용한 공정 흐름·병목 분석 | 1,073 | AGPL-3.0 | 공개 |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) · [로컬](repos/10-manufacturing-optimization/statsmodels__statsmodels/) | P0 | 통계 검정·회귀·시계열의 해석 가능한 baseline | 11,731 | BSD-3-Clause | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 11-local-llm — 로컬 모델·추론·미세조정

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [ollama/ollama](https://github.com/ollama/ollama) · [로컬](repos/11-local-llm/ollama__ollama/) | P0 | 로컬 모델 서빙과 간단한 추론 API | 185,349 | MIT | 공개 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) · [로컬](repos/11-local-llm/ggml-org__llama.cpp/) | P0 | CPU·GPU 양자화 LLM 추론 | 132,847 | MIT | 공개 |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) · [로컬](repos/11-local-llm/vllm-project__vllm/) | P1 | GPU 기반 LLM 고처리량 서빙 | 95,916 | Apache-2.0 | 공개 |
| [huggingface/transformers](https://github.com/huggingface/transformers) · [로컬](repos/11-local-llm/huggingface__transformers/) | P0 | 언어·비전·멀티모달 사전학습 모델 활용 | 168,352 | Apache-2.0 | 공개 |
| [huggingface/peft](https://github.com/huggingface/peft) · [로컬](repos/11-local-llm/huggingface__peft/) | P1 | LoRA 등 적은 자원으로 모델 미세조정 | 21,863 | Apache-2.0 | 공개 |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) · [로컬](repos/11-local-llm/unslothai__unsloth/) | P1 | 효율적인 모델 미세조정 워크플로 | 78,805 | Apache-2.0 | 공개 |
| [huggingface/trl](https://github.com/huggingface/trl) · [로컬](repos/11-local-llm/huggingface__trl/) | P2 | SFT·선호 최적화 등 후학습 예제 | 19,635 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 12-eval-observability — 평가·실험·관측

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [로컬](repos/12-eval-observability/promptfoo__promptfoo/) | P0 | 프롬프트·모델 회귀 평가와 테스트 케이스 | 26,636 | MIT | 공개 |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) · [로컬](repos/12-eval-observability/vibrantlabsai__ragas/) | P0 | RAG 검색·답변 품질 평가 | 16,190 | Apache-2.0 | 공개 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) · [로컬](repos/12-eval-observability/confident-ai__deepeval/) | P1 | LLM 출력 품질 평가와 회귀 테스트 | 19,201 | Apache-2.0 | 공개 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) · [로컬](repos/12-eval-observability/mlflow__mlflow/) | P1 | 모델·실험·평가 추적 | 28,600 | Apache-2.0 | 공개 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) · [로컬](repos/12-eval-observability/Arize-ai__phoenix/) | P1 | LLM trace·평가·오류 분석 | 12,076 | NOASSERTION | 공개 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) · [로컬](repos/12-eval-observability/langfuse__langfuse/) | P1 | LLM 요청 trace와 프롬프트 관리 | 36,759 | NOASSERTION | 공개 |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) · [로컬](repos/12-eval-observability/evidentlyai__evidently/) | P1 | 모델·데이터 드리프트와 품질 리포트 | 8,024 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 13-automation-mcp — 브라우저 자동화·MCP

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [microsoft/playwright](https://github.com/microsoft/playwright) · [로컬](repos/13-automation-mcp/microsoft__playwright/) | P0 | 브라우저 실제 사용자 흐름 검증 | 98,881 | Apache-2.0 | 공개 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) · [로컬](repos/13-automation-mcp/browser-use__browser-use/) | P1 | 에이전트의 브라우저 조작 구현 예제 | 119,575 | MIT | 공개 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) · [로컬](repos/13-automation-mcp/PrefectHQ__fastmcp/) | P1 | Python MCP 서버·도구 구성 | 28,247 | Apache-2.0 | 공개 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · [로컬](repos/13-automation-mcp/modelcontextprotocol__servers/) | P1 | MCP 서버 참조 구현과 연결 패턴 | 91,695 | NOASSERTION | 공개 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) · [로컬](repos/13-automation-mcp/modelcontextprotocol__python-sdk/) | P1 | MCP Python 프로토콜 구현 | 24,711 | MIT | 공개 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) · [로컬](repos/13-automation-mcp/firecrawl__firecrawl/) | P2 | 웹 문서 수집 API와 파이프라인 구현 | 196,987 | AGPL-3.0 | 공개 |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) · [로컬](repos/13-automation-mcp/unclecode__crawl4ai/) | P1 | 웹 페이지를 LLM이 읽을 수 있는 데이터로 수집 | 86,589 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 14-visualization-presentation — 시각화·발표

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [plotly/plotly.py](https://github.com/plotly/plotly.py) · [로컬](repos/14-visualization-presentation/plotly__plotly.py/) | P0 | 수율·센서·성능 지표 인터랙티브 차트 | 18,862 | MIT | 공개 |
| [vega/altair](https://github.com/vega/altair) · [로컬](repos/14-visualization-presentation/vega__altair/) | P1 | 선언형 통계 시각화 | 10,510 | BSD-3-Clause | 공개 |
| [apache/echarts](https://github.com/apache/echarts) · [로컬](repos/14-visualization-presentation/apache__echarts/) | P1 | 웹 대시보드 차트와 데이터 시각화 | 67,641 | Apache-2.0 | 공개 |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) · [로컬](repos/14-visualization-presentation/mermaid-js__mermaid/) | P0 | 텍스트로 구조·흐름·시퀀스 다이어그램 작성 | 90,931 | MIT | 공개 |
| [slidevjs/slidev](https://github.com/slidevjs/slidev) · [로컬](repos/14-visualization-presentation/slidevjs__slidev/) | P1 | Markdown 기반 발표 슬라이드 제작 | 49,299 | MIT | 공개 |
| [marimo-team/marimo](https://github.com/marimo-team/marimo) · [로컬](repos/14-visualization-presentation/marimo-team__marimo/) | P1 | 재현 가능한 Python 분석 노트북과 앱 | 23,373 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 15-cookbooks-learning — 공식 예제·학습 자료

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [로컬](repos/15-cookbooks-learning/openai__openai-cookbook/) | P0 | LLM API·검색·도구 호출의 공식 예제 | 76,873 | MIT | 공개 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) · [로컬](repos/15-cookbooks-learning/anthropics__claude-cookbooks/) | P1 | 도구·문서·평가 관련 Claude 활용 예제 | 53,955 | MIT | 공개 |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) · [로컬](repos/15-cookbooks-learning/microsoft__generative-ai-for-beginners/) | P1 | 생성형 AI 애플리케이션 개념과 실습 | 122,479 | MIT | 공개 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) · [로컬](repos/15-cookbooks-learning/microsoft__ai-agents-for-beginners/) | P1 | 에이전트 설계 패턴과 실습 | 78,278 | MIT | 공개 |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) · [로컬](repos/15-cookbooks-learning/rasbt__LLMs-from-scratch/) | P2 | LLM 내부 구조를 이해하기 위한 구현 | 107,562 | NOASSERTION | 공개 |
| [ageron/handson-ml3](https://github.com/ageron/handson-ml3) · [로컬](repos/15-cookbooks-learning/ageron__handson-ml3/) | P2 | 머신러닝 실습·전처리·모델 평가 참고 | 14,405 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 16-semiconductor-data — 반도체 데이터·웨이퍼 검사

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [makinarocks/awesome-industrial-machine-datasets](https://github.com/makinarocks/awesome-industrial-machine-datasets) · [로컬](repos/16-semiconductor-data/makinarocks__awesome-industrial-machine-datasets/) | P0 | SECOM·웨이퍼·설비 등 산업 공개 데이터 탐색 | 565 | UNKNOWN | 공개 |
| [jonathanwvd/awesome-industrial-datasets](https://github.com/jonathanwvd/awesome-industrial-datasets) · [로컬](repos/16-semiconductor-data/jonathanwvd__awesome-industrial-datasets/) | P0 | 제조·설비·품질 데이터셋 설명과 원출처 링크 | 619 | NOASSERTION | 공개 |
| [markditsworth/Semiconductor-Fault-Detection](https://github.com/markditsworth/Semiconductor-Fault-Detection) · [로컬](repos/16-semiconductor-data/markditsworth__Semiconductor-Fault-Detection/) | P2 | SECOM 반도체 공정 분류 사례; 소규모 커뮤니티 예제로 검증 후 참고 | 21 | MIT | 공개 |
| [SpatialAILab/WaferDC](https://github.com/SpatialAILab/WaferDC) · [로컬](repos/16-semiconductor-data/SpatialAILab__WaferDC/) | P2 | SEM 웨이퍼 결함 검출·분류 연구 코드; 데이터와 모델은 별도 확인 | 23 | NOASSERTION | 공개 |
| [MichaelHotaling/klarfkit](https://github.com/MichaelHotaling/klarfkit) · [로컬](repos/16-semiconductor-data/MichaelHotaling__klarfkit/) | P1 | 반도체 검사 KLARF 파일 로딩·웨이퍼 결함 맵 처리 | 31 | MIT | 공개 |
| [chrisshaffer/wafer-defect-maps](https://github.com/chrisshaffer/wafer-defect-maps) · [로컬](repos/16-semiconductor-data/chrisshaffer__wafer-defect-maps/) | P2 | WM811K 웨이퍼 맵 CNN 분류 커뮤니티 사례 | 40 | UNKNOWN | 공개 |
| [PanithanS/Wafers-Defect-Recognition-using-Visual-Transformer](https://github.com/PanithanS/Wafers-Defect-Recognition-using-Visual-Transformer) · [로컬](repos/16-semiconductor-data/PanithanS__Wafers-Defect-Recognition-using-Visual-Transformer/) | P2 | MixedWM38 혼합 웨이퍼 결함 패턴 인식 연구 사례 | 55 | MIT | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 17-memory-storage-simulation — DRAM·HBM·SSD 시뮬레이션

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [CMU-SAFARI/ramulator2](https://github.com/CMU-SAFARI/ramulator2) · [로컬](repos/17-memory-storage-simulation/CMU-SAFARI__ramulator2/) | P0 | DRAM·HBM 메모리 타이밍과 컨트롤러 시뮬레이션 | 698 | MIT | 공개 |
| [umd-memsys/DRAMsim3](https://github.com/umd-memsys/DRAMsim3) · [로컬](repos/17-memory-storage-simulation/umd-memsys__DRAMsim3/) | P0 | DRAM 타이밍·대역폭·메모리 시스템 시뮬레이션 | 524 | MIT | 공개 |
| [tukl-msd/DRAMSys](https://github.com/tukl-msd/DRAMSys) · [로컬](repos/17-memory-storage-simulation/tukl-msd__DRAMSys/) | P1 | DRAM 시스템 성능·전력 분석 시뮬레이션 | 407 | NOASSERTION | 공개 |
| [CMU-SAFARI/MQSim](https://github.com/CMU-SAFARI/MQSim) · [로컬](repos/17-memory-storage-simulation/CMU-SAFARI__MQSim/) | P0 | SSD 큐·컨트롤러·flash 계층 성능 시뮬레이션 | 407 | MIT | 공개 |
| [SimpleSSD/SimpleSSD](https://github.com/SimpleSSD/SimpleSSD) · [로컬](repos/17-memory-storage-simulation/SimpleSSD__SimpleSSD/) | P1 | SSD 컨트롤러·펌웨어·성능 연구용 시뮬레이터 | 64 | GPL-3.0 | 공개 |
| [ChampSim/ChampSim](https://github.com/ChampSim/ChampSim) · [로컬](repos/17-memory-storage-simulation/ChampSim__ChampSim/) | P1 | 캐시·prefetch·메모리 접근 성능 실험 | 775 | Apache-2.0 | 공개 |
| [gem5/gem5](https://github.com/gem5/gem5) · [로컬](repos/17-memory-storage-simulation/gem5__gem5/) | P2 | CPU·캐시·메모리를 포함한 시스템 시뮬레이터 | 2,903 | BSD-3-Clause | 공개 |
| [CMU-SAFARI/DRAM-Bender](https://github.com/CMU-SAFARI/DRAM-Bender) · [로컬](repos/17-memory-storage-simulation/CMU-SAFARI__DRAM-Bender/) | P2 | 실제 DRAM 특성을 실험하는 FPGA 기반 연구 플랫폼 | 144 | MIT | 공개 |
| [CMU-SAFARI/HBM-Power](https://github.com/CMU-SAFARI/HBM-Power) · [로컬](repos/17-memory-storage-simulation/CMU-SAFARI__HBM-Power/) | P1 | 실제 HBM2 연구 기반 전력 모델; 세대·가정·적용 범위 확인 | 22 | NOASSERTION | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 18-eda-hardware — EDA·하드웨어 검증

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [The-OpenROAD-Project/OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) · [로컬](repos/18-eda-hardware/The-OpenROAD-Project__OpenROAD/) | P1 | RTL 이후 물리 설계 자동화 도구 | 3,240 | BSD-3-Clause | 공개 |
| [YosysHQ/yosys](https://github.com/YosysHQ/yosys) · [로컬](repos/18-eda-hardware/YosysHQ__yosys/) | P1 | RTL 합성과 회로 분석 도구 | 4,855 | ISC | 공개 |
| [verilator/verilator](https://github.com/verilator/verilator) · [로컬](repos/18-eda-hardware/verilator__verilator/) | P1 | Verilog·SystemVerilog 시뮬레이션과 lint | 4,042 | NOASSERTION | 공개 |
| [cocotb/cocotb](https://github.com/cocotb/cocotb) · [로컬](repos/18-eda-hardware/cocotb__cocotb/) | P1 | Python 기반 RTL 테스트벤치 | 2,558 | BSD-3-Clause | 공개 |
| [KLayout/klayout](https://github.com/KLayout/klayout) · [로컬](repos/18-eda-hardware/KLayout__klayout/) | P1 | 반도체 레이아웃 시각화·스크립트 처리 | 1,251 | GPL-3.0 | 공개 |
| [The-OpenROAD-Project/OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA) · [로컬](repos/18-eda-hardware/The-OpenROAD-Project__OpenSTA/) | P1 | 정적 타이밍 분석과 경로 진단 | 636 | GPL-3.0 | 공개 |
| [chipfoundry/openlane2](https://github.com/chipfoundry/openlane2) · [로컬](repos/18-eda-hardware/chipfoundry__openlane2/) | P2 | 모듈형 RTL-to-GDS 구현 흐름; 실행 환경과 공정 설정 확인 | 381 | Apache-2.0 | 공개 |
| [google/skywater-pdk](https://github.com/google/skywater-pdk) · [로컬](repos/18-eda-hardware/google__skywater-pdk/) | P2 | 공개 PDK 구조와 설계 규칙 참고; 실제 공정과 구분 | 3,770 | Apache-2.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 19-industrial-integration — 산업 센서·장비 연동

| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [eclipse-paho/paho.mqtt.python](https://github.com/eclipse-paho/paho.mqtt.python) · [로컬](repos/19-industrial-integration/eclipse-paho__paho.mqtt.python/) | P1 | MQTT 센서·설비 데이터 수신과 이벤트 연동 | 2,432 | NOASSERTION | 공개 |
| [FreeOpcUa/opcua-asyncio](https://github.com/FreeOpcUa/opcua-asyncio) · [로컬](repos/19-industrial-integration/FreeOpcUa__opcua-asyncio/) | P1 | OPC UA 산업 장비 데이터의 비동기 연동 | 1,507 | LGPL-3.0 | 공개 |

먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.

## 데이터와 별도 파일

SECOM과 공개 NIST PDF는 scripts/fetch_materials.py로 수집한다. 원문·데이터셋의 배포와 실습 조건은 guides/SOURCES.md에 있다.
레포 clone은 shallow이며 모델 가중치·LFS 객체·submodule·의존성 설치는 포함하지 않는다.
