#!/usr/bin/env python3
"""Render the Korean catalog from the verified repository manifest."""

from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "01-agent-skills": "에이전트 스킬·작업 지침",
    "02-llm-agents": "LLM 에이전트·워크플로",
    "03-rag-search": "RAG·임베딩·검색",
    "04-document-ocr": "문서 처리·OCR",
    "05-web-ui": "웹앱·데모 UI",
    "06-api-backend": "API·백엔드",
    "07-tabular-ml": "정형 데이터·머신러닝",
    "08-timeseries-anomaly": "시계열·이상 탐지",
    "09-industrial-vision": "산업 비전·영상 검사",
    "10-manufacturing-optimization": "제조 최적화·통계·인과",
    "11-local-llm": "로컬 모델·추론·미세조정",
    "12-eval-observability": "평가·실험·관측",
    "13-automation-mcp": "브라우저 자동화·MCP",
    "14-visualization-presentation": "시각화·발표",
    "15-cookbooks-learning": "공식 예제·학습 자료",
    "16-semiconductor-data": "반도체 데이터·웨이퍼 검사",
    "17-memory-storage-simulation": "DRAM·HBM·SSD 시뮬레이션",
    "18-eda-hardware": "EDA·하드웨어 검증",
    "19-industrial-integration": "산업 센서·장비 연동",
}


def main():
    manifest = json.loads((ROOT / "repositories.json").read_text())
    repos = manifest["repositories"]
    lines = [
        "# 해커톤 공개 레포 카탈로그",
        "",
        f"GitHub 메타데이터 확인: {manifest['verified_at']} · 레포 {len(repos)}개 · {len(set(r['category'] for r in repos))}개 분야.",
        "",
        "P0: 먼저 살펴볼 후보 / P1: 상황별 대안 / P2: 전문 연구·학습 또는 도입 비용이 큰 참조. 공식 순위가 아닌 준비용 분류다.",
        "별 수·라이선스 표시는 스냅샷이며, 혼합 라이선스와 모델·데이터의 개별 조건은 원본에서 확인한다. NOASSERTION/UNKNOWN은 사용 허가를 뜻하지 않는다.",
        "로컬 링크는 기본 설치 루트 ~/hackathon-reference/ 기준이다. 실제 README·예제 경로와 clone한 commit은 LOCAL_INDEX.json, 실패 여부는 CLONE_STATUS.json에 있다.",
        "",
        "| 분야 | 개수 |",
        "| --- | --- |",
    ]
    counts = Counter(r["category"] for r in repos)
    for category, count in sorted(counts.items()):
        lines.append(f"| {category}: {LABELS[category]} | {count} |")
    for category in sorted(counts):
        lines += [
            "",
            f"## {category} — {LABELS[category]}",
            "",
            "| 레포 / 로컬 폴더 | 우선 | 언제 볼 것인가 | stars | 라이선스 표시 | 상태 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for r in (r for r in repos if r["category"] == category):
            status = "보관(archived)" if r["archived"] else "공개"
            summary = r["summary"].replace("|", "\\|")
            lines.append(
                f"| [{r['repo']}]({r['url']}) · [로컬]({r['directory']}/) | {r['priority']} | {summary} | {r['stars']:,} | {r['license']} | {status} |"
            )
        lines += [
            "",
            "먼저 해당 레포 README를 읽고, 실제 존재하는 docs/examples 진입점은 LOCAL_INDEX.json에서 찾는다.",
        ]
    lines += [
        "",
        "## 데이터와 별도 파일",
        "",
        "SECOM과 공개 NIST PDF는 scripts/fetch_materials.py로 수집한다. 원문·데이터셋의 배포와 실습 조건은 guides/SOURCES.md에 있다.",
        "레포 clone은 shallow이며 모델 가중치·LFS 객체·submodule·의존성 설치는 포함하지 않는다.",
    ]
    (ROOT / "CATALOG.md").write_text("\n".join(lines) + "\n")
    print(f"Catalog: {len(repos)} repositories / {len(counts)} categories")


if __name__ == "__main__":
    main()
