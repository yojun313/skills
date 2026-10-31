# SK하이닉스 해커톤용 반도체 빠른 이해

이 문서는 공개 자료의 준비용 요약이다. 실제 과제·공정 조건·내부 지표는 제공받은 데이터와 안내로 확인한다. 확인일 2026-10-31. 아래의 활용 아이디어는 출제 예측이 아니다.

## 1. 회사와 기술을 연결하는 최소 맥락

SK하이닉스 연구 자료는 DRAM·NAND의 발전, 메모리 시스템, 계측·검사, 장비 진단, 패키징을 다룬다. AI를 적용할 지점도 모델 자체뿐 아니라 데이터 품질, 결함 검출, 공정·장비 분석, 메모리 성능으로 나눠 생각할 수 있다. [공식 연구 분야](https://research.skhynix.com/research-areas/future-memory-technologies/evolutionary-memory)

| 용어 | 알아둘 의미 | 과제에서 먼저 물을 것 |
| --- | --- | --- |
| DRAM | 전원이 유지되는 동안 데이터를 보관하는 고속 작업 메모리 | 용량·대역폭·지연·전력 중 목표는? |
| DDR / LPDDR / GDDR | 서버·PC, 모바일, 그래픽 등 용도에 따라 다른 DRAM 인터페이스 계열 | 실제 제품·세대·사용 환경은? |
| HBM | DRAM die를 적층하고 넓은 인터페이스로 대역폭을 확보하는 메모리 | 용량·유효 대역폭·열·접근 패턴은? |
| NAND flash | 전원이 없어도 데이터를 보관하는 비휘발성 메모리 | 읽기·쓰기·수명·용량 중 목표는? |
| 3D NAND | 메모리 셀을 수직으로 쌓아 집적도를 높이는 구조 | 적층 구조와 결함·계측의 관계는? |
| SSD | NAND와 컨트롤러·펌웨어 등을 결합한 저장장치 | IOPS·지연·처리량·내구성·QoS 중 무엇을 평가하나? |
| CXL | 메모리 확장·공유 등과 관련된 시스템 연결 기술 | 어떤 계층과 실제 구성을 가정하나? |
| PIM / PNM | 메모리 내부 또는 근처에서 연산해 데이터 이동을 줄이려는 접근 | 이동 비용과 계산 비용 중 병목은? |

DRAM·NAND 기본 구분은 [SK하이닉스 Evolutionary Memory](https://research.skhynix.com/research-areas/future-memory-technologies/evolutionary-memory), 시스템 계층의 성능·비용 고려는 [Memory & Storage Solution](https://research.skhynix.com/research-areas/memory-systems-research/next-gen-memory-storage-solution)을 참고한다. 제품별 수치·출시 상태는 여기서 고정하지 않고 과제에서 쓰는 공식 자료로 확인한다.

## 2. 제조 흐름을 데이터 문제로 읽기

웨이퍼 위에 막을 쌓고, 패턴을 전사하고, 식각·이온 주입·측정을 반복한 뒤 칩을 분리·패키징한다. 공정은 단순한 일회성 직선 흐름이 아니며 여러 장비와 단계가 반복된다. [ASML 공정 설명](https://www.asml.com/en/company/stories/2021/semiconductor-manufacturing-process-steps)

| 단계/대상 | 흔히 관찰할 데이터의 예 | 준비할 분석 방식 |
| --- | --- | --- |
| 증착·산화 | 온도·압력·유량·막 두께 | 조건별 분포와 품질 예측 |
| 포토·노광 | overlay·선폭·패턴 이미지 | 정렬 오차와 결함 분석 |
| 식각 | 시간·압력·플라즈마·형상 | 센서 이상·단계별 특징 |
| CMP | 제거율·압력·두께·평탄도 | 가상 계측과 drift 확인 |
| 계측·검사 | 측정값·광학/SEM 이미지·결함 좌표 | 불량 후보 분류와 위치 표시 |
| 테스트 | 전기적 특성·pass/fail·bin | 희소 불량 탐지와 수율 집계 |
| 패키징·본딩 | 정렬·warpage·열·접합 관련 측정 | 결함·신뢰성 위험 분석 |
| 장비·물류 | event·alarm·recipe·대기·처리 시간 | 설비 진단·병목·스케줄링 |

표의 분석 방식은 준비용 설계 제안이다. 실제 이용 가능한 센서·측정값은 과제마다 다르다. 계측·검사의 AI 적용 맥락은 [SK하이닉스 MI 연구](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/advanced-metrology-inspection), 장비 진단은 [Machine Engineering](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/machine-engineering)에서 확인할 수 있다.

## 3. 데이터에서 자주 만날 이름

| 이름 | 데이터에서의 의미 / 주의점 |
| --- | --- |
| fab | 제조 시설. 서로 다른 fab의 조건 차이를 확인 |
| lot | 함께 관리되는 웨이퍼 묶음. 분할·집계·추적 키 후보 |
| wafer | 개별 웨이퍼. 같은 wafer의 die·이미지·센서가 누수되지 않게 묶기 |
| die / chip | 웨이퍼 위 개별 칩 영역. 제품에 따라 위치·크기·유효 영역이 다름 |
| tool / chamber | 장비와 내부 처리 공간. chamber별 상태 차이 확인 |
| recipe / step | 공정 조건과 단계. 정상 신호라도 단계에 따라 분포가 다름 |
| WAT / E-test | 웨이퍼 공정 전기 특성 측정 맥락. 실제 필드 정의 확인 |
| wafer map / bin map | die 위치와 결과를 공간적으로 표시. 원시 검사 이미지와 구분 |
| KLARF | 검사 결함 정보 교환에 쓰이는 파일 형식. 버전·좌표·단위 확인 |
| MES | 제조 실행·추적 관련 시스템. 실제 제공 event schema 확인 |
| FDC | Fault Detection and Classification. 센서·상태에서 이상을 찾고 구분 |
| SPC | Statistical Process Control. 시간에 따른 공정의 통계적 안정성 모니터링 |
| APC | Advanced Process Control. 공정 제어 맥락; 추천과 실제 제어를 구별 |
| VM | Virtual Metrology. 센서 등으로 계측값을 예측; 실제 측정의 대체 가능 범위 확인 |
| RUL / PdM | 잔여수명·예지보전. 라벨·고장 이력·시간 누수 확인 |
| yield / bin / scrap / rework | 수율·결과 그룹·폐기·재작업. 분모와 기준이 서로 다름 |

위 용어는 필드를 해석하기 위한 일반 용어집이다. 회사별 약어·bin 의미·공정 단계는 데이터 사전으로 확인한다. VM의 실제 연구 과제인 측정 비용·센서 drift·불확실성은 [NIST VM 연구](https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic)를 참고한다.

## 4. 수치와 성능을 잘못 해석하지 않기

- 수율은 `정의된 합격 수 / 정의된 평가 대상 수`. die 수율·wafer 합격률·출하 기준을 섞지 않는다.
- precision은 알람 중 실제 불량 비율, recall은 실제 불량 중 찾은 비율이다. 알람이 많아지는 비용과 놓치는 비용을 같이 본다.
- 웨이퍼 맵의 `None`은 데이터셋 정의에 따른 패턴 라벨일 수 있다. 모든 die가 완전 정상이라는 뜻으로 임의 변환하지 않는다.
- 센서 예측에서는 실제 측정 시각과 라벨을 사용할 수 있었던 시점을 구분한다. 불량 확정 뒤 생성된 정보를 사전 탐지 모델에 넣지 않는다.
- 대역폭(GB/s), 접근 지연(ns/μs), 처리량(IOPS), 저장 용량(GB/TB)은 서로 대체할 수 없는 지표다. bit/byte와 SI/IEC 단위를 확인한다.
- 공정 규격의 상·하한과 통계적 관리한계는 목적이 다르다. 알람 기준을 같은 것으로 쓰지 않는다.

안정 공정의 양측 규격과 정규성 등 가정하에서 `Cp=(USL-LSL)/(6σ)`, `Cpk=min((USL-μ)/(3σ),(μ-LSL)/(3σ))`. 표본 수·분포·안정성·σ 추정 방법에 따라 해석이 달라지므로 숫자 하나만으로 공정 능력을 확정하지 않는다. [NIST Process Capability](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)

## 5. 해커톤에서 시도할 문제 유형 — 출제 예측 아님

| 제공 데이터 | 만들 수 있는 작은 결과물 | 먼저 쓸 후보 | 검증의 핵심 |
| --- | --- | --- | --- |
| 공정 CSV + pass/fail | 불량 후보 우선 검토 대시보드 | scikit-learn·CatBoost·SHAP·Streamlit | lot/time 분리, baseline·PR·알람량 |
| 다변량 센서 시계열 | 이상 구간과 관련 센서 표시 | tsfresh·PyOD·River·Plotly | 시간 누수, 단계 정렬, 오탐 |
| 정상 이미지 중심 검사 데이터 | 결함 heatmap과 리뷰 화면 | anomalib·PatchCore·Gradio | 정상/불량·위치 수준 평가 분리 |
| 웨이퍼 맵·KLARF | 결함 패턴·공간 분포 뷰어 | klarfkit·OpenCV·Plotly | 좌표·wafer 방향·단위 검증 |
| 장비 event log | 대기 병목·흐름 분석 | DuckDB·pm4py·SimPy | timestamp·동시 이벤트·제약 |
| 작업·장비·납기 표 | 실행 가능한 일정 추천 | OR-Tools | 자원 충돌·순서·실행 가능성 |
| PDF 매뉴얼·보고서 | 출처를 보여 주는 검색 보조 | Docling·sentence-transformers·Qdrant | 근거 정확성·문서 버전·답변 유보 |
| 메모리 trace·구성 | 접근 패턴별 성능 비교 | Ramulator2·DRAMsim3·MQSim | 시뮬레이터 가정·단위·재현성 |

이 표는 공개 도구를 과제 유형에 연결한 준비 전략이다. 전체 제조 문제를 한 번에 자동화하려 하지 말고 제공 데이터로 검증할 수 있는 한 흐름을 선택한다.

## 6. 우선 읽을 공식 자료

1. [Evolutionary Memory](https://research.skhynix.com/research-areas/future-memory-technologies/evolutionary-memory): DRAM·NAND의 출발점.
2. [Advanced Metrology & Inspection](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/advanced-metrology-inspection): 계측·결함과 데이터 분석 맥락.
3. [Machine Engineering](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/machine-engineering): 장비 진단과 자율화 방향.
4. [Advanced Memory Package Architecture](https://research.skhynix.com/research-areas/advanced-package/advanced-memory-package-architecture): 적층·열·인터커넥트 관점.
5. [Next Gen. Memory & Storage Solution](https://research.skhynix.com/research-areas/memory-systems-research/next-gen-memory-storage-solution): 용량·지연·대역폭·비용 관점.
6. [NIST 반도체 제조 연구](https://www.nist.gov/publications/innovations-advanced-processes-and-systems-semiconductor-manufacturing): 제조·계측·운영 최적화 연구의 넓은 배경.

원문이 없어도 이 문서와 `SOURCES.md`의 짧은 요약은 로컬에서 읽을 수 있다. 원문 전체·유료 표준 문서·내부 공정 정보는 수집하지 않았다. 로드맵 수치나 특정 세대의 양산 상태를 근거 없이 현재 사실로 확장하지 않는다.
