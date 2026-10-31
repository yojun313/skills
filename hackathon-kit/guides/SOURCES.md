# 수집한 자료와 근거의 범위

확인일: 2026-10-31. 공식 페이지·원저자 레포를 우선했다. 웹 페이지는 전체 복제 대신 짧은 요약과 링크를 저장했고, 공개 제공 PDF와 SECOM은 별도 다운로드 스크립트로 수집한다. 제품 수치·페이지·라이선스는 바뀔 수 있으므로 실제 사용 시 해당 버전을 확인한다.

## 대회·COFA

| 출처 | 구분 | 이 키트에서 확인한 것 |
| --- | --- | --- |
| [SK하이닉스 Talent Hub 발표](https://talent.skhynix.com/hub/ko/company/story/237) | 주최사 공식 | Cofa-Probe 등을 활용한 문제 정의·AI 활용·검증 평가와 예선/본선의 성격 |
| [대회 공식 홈페이지](https://skhynix-hackathon.com/ai-2026) | 대회 공식 | 2차 예선 10/31~11/1, 본선 11/11, 실제 현장 문제와 작동 결과 강조 |
| [COFA Probe 한국어](https://www.getcofa.com/ko/probe) | 플랫폼 공식 | 산출물·AI 대화·도구·검증 기록 수집, 사후 설명과 구현 대조, 기술·의도·인지의 관점 |
| [COFA Probe 영어](https://www.getcofa.com/en/probe) | 플랫폼 공식 | 산출물과 과정에 근거한 평가라는 점 교차 확인 |
| [Luka의 크래프톤 FDE 코파톤 후기](https://brunch.co.kr/@luma/5) | 참가자 경험 / 2026-08-02 | 다른 대회에서의 세 축과 FDE 소통 평가, 구현 이해·검증·인계에 대한 경험. SK하이닉스 세부 배점의 근거로 사용하지 않음 |

문서 수, 프롬프트 길이, commit 수 자체에 정해진 점수가 있다는 근거는 확인하지 못했다. 공개 자료로 비공개 채점식·합격 기준·문항을 확정할 수 없다.

## SK하이닉스 공식 기술 자료

| 출처 | 짧은 준비용 요약 | 연결할 문제 유형 |
| --- | --- | --- |
| [Evolutionary Memory](https://research.skhynix.com/research-areas/future-memory-technologies/evolutionary-memory) | DRAM과 NAND의 구조·발전 방향을 구분해 이해할 출발점 | 메모리 제품·용어 이해 |
| [Next Gen. Memory & Storage Solution](https://research.skhynix.com/research-areas/memory-systems-research/next-gen-memory-storage-solution) | 대역폭·지연·용량·비용과 메모리 계층, 접근 패턴의 중요성 | 메모리 성능·시뮬레이션 |
| [Advanced Metrology & Inspection](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/advanced-metrology-inspection) | 미세화·적층에서 계측과 결함 분류의 중요성, AI·복합 측정의 활용 | 이미지 검사·가상 계측 |
| [Machine Engineering](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/machine-engineering) | 신기술 장비의 진단과 데이터 기반 품질 분석이라는 방향 | 설비 진단·이상 탐지 |
| [Frontier Analysis Technology](https://research.skhynix.com/research-areas/semiconductor-Infrastructure-technology/frontier-analysis-technology) | 구조·재료의 3차원 분석을 포함한 첨단 특성 분석 연구 | 이미지·다중 데이터 해석 |
| [Advanced Memory Package Architecture](https://research.skhynix.com/research-areas/advanced-package/advanced-memory-package-architecture) | 적층·인터커넥트·열·신뢰성을 함께 고려하는 패키지 연구 | 패키징·열·설계 trade-off |
| [Artificial Intelligence](https://research.skhynix.com/research-areas/memory-systems-research/artificial-intelligence) | 회사의 AI 관련 메모리 시스템 연구를 더 살펴볼 공식 진입점 | 추가 주제 탐색 |

공개 연구 방향은 회사 내부의 실제 공정 조건이나 내일 과제를 의미하지 않는다. 이 요약에 없는 숫자를 원문 확인 없이 제안서에 넣지 않는다.

## 제조·계측·통계와 공개 데이터

| 출처 | 용도 / 저장 상태 |
| --- | --- |
| [ASML 제조 공정 설명](https://www.asml.com/en/company/stories/2021/semiconductor-manufacturing-process-steps) | 증착·포토·식각 등의 공정 맥락. 요약·링크만 저장 |
| [NIST 공정 능력](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) | Cp/Cpk의 가정과 해석. 요약·링크만 저장 |
| [NIST Virtual Metrology 연구, 2025](https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic) | 적은 계측 데이터·drift·불확실성을 다루는 VM 연구. 공개 PDF 수집 대상 |
| [NIST Semiconductor Manufacturing 연구, 2026](https://www.nist.gov/publications/innovations-advanced-processes-and-systems-semiconductor-manufacturing) | 공정·장비·in-line 계측·운영 최적화 등의 연구 배경. 공개 PDF 수집 대상 |
| [UCI SECOM](https://archive.ics.uci.edu/dataset/179/secom) | 실제 공개 반도체 공정 데이터. CC BY 4.0. 작은 원본 ZIP과 출처·SHA 수집 대상 |
| [WM-811K 원출처 안내 / MIR Lab](http://mirlab.org/dataSet/public/) | 웨이퍼 맵 데이터 출발점. 원본 접근/조건 확인 필요, 미다운로드 |
| [WM-811K Kaggle 배포 페이지](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map) | 웨이퍼 맵 실습 후보. 계정·배포 조건 확인 필요, 미다운로드 |
| [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad) | 산업 영상 이상 탐지 benchmark. CC BY-NC-SA 4.0, 이용 목적 확인 후 별도 확보. 미다운로드 |
| [NASA Prognostics Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) | 설비 예지보전 실습 후보. 항목별 원출처·조건 확인, 미다운로드 |

SECOM은 1,567개 사례의 희소 불량·결측 처리 연습에 적합하다. UCI 페이지는 591개 feature로 표시하지만 `secom.data` 원본에는 센서 590열이 있고 시각은 라벨 파일에 있다. 다운로드 후 실제 행·열·라벨 분포는 `datasets/secom/PROVENANCE.json`으로 확인한다. SK하이닉스 내부 데이터가 아니다.

다운로드한 파일의 실제 성공 여부, byte 크기, SHA-256은 `../MATERIALS_STATUS.json`에 남는다. 다운로드하지 않은 데이터셋과 모델 가중치가 준비됐다고 가정하지 않는다.

## 레포 목록의 근거

`../repositories.json`은 GitHub REST API의 공식 메타데이터를 수집한 스냅샷이다. 정식 레포 주소, 공개 상태, star 수, 최근 push, 보관 여부, 라이선스 표시가 들어 있다. `../LOCAL_INDEX.json`과 `../CLONE_STATUS.json`은 실제 clone 결과와 commit SHA를 제공한다.

별 수는 유명한 후보를 찾는 참고 지표이며 구현 품질이나 적합성을 보장하지 않는다. “언제 사용할지” 설명과 P0/P1/P2는 이 키트를 위해 작성한 선택 가이드다. 해당 버전의 README와 라이선스를 읽고 필요한 코드만 활용한다. 문서·모델·데이터에는 레포의 대표 라이선스와 다른 조건이 있을 수 있다.
