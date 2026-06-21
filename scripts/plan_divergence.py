from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLANS_DIR = ROOT / "wiki" / "plans"
FEATURE_COVERAGE = ROOT / "wiki" / "features" / "feature-coverage.md"

KEY_TERMS = [
    "Foundry Agent",
    "knowledge base",
    "file search",
    "Azure Blob Storage",
    "Azure AI Search",
    "evaluations",
    "monitoring",
    "tracing",
]


def main() -> None:
    plan_text = "\n".join(path.read_text(encoding="utf-8") for path in sorted(PLANS_DIR.glob("*.md")))
    feature_text = FEATURE_COVERAGE.read_text(encoding="utf-8")
    missing = [term for term in KEY_TERMS if term.lower() in plan_text.lower() and term.lower() not in feature_text.lower()]

    print("Plan divergence report")
    print("======================")
    print(f"Plans scanned: {len(list(PLANS_DIR.glob('*.md')))}")
    print(f"Key terms checked: {len(KEY_TERMS)}")
    if missing:
        print("Terms planned but not reflected in feature coverage:")
        for term in missing:
            print(f"- {term}")
    else:
        print("No advisory divergence found.")


if __name__ == "__main__":
    main()
