from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "evals" / "datasets" / "support_questions.jsonl"
RESULTS_DIR = ROOT / "evals" / "results"


def load_dataset() -> list[dict[str, object]]:
    return [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    dataset = load_dataset()
    result = {
        "status": "scaffolded",
        "dataset": str(DATASET),
        "question_count": len(dataset),
        "note": "Wire this script to the running API, then to Microsoft Foundry evaluators.",
    }
    (RESULTS_DIR / "latest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (RESULTS_DIR / "latest.md").write_text(
        "# Latest Evaluation\n\n"
        f"- Status: {result['status']}\n"
        f"- Questions: {result['question_count']}\n"
        f"- Note: {result['note']}\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
