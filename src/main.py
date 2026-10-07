from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True)
class RiskSignal:
    category: str
    severity: str
    evidence: str


def classify(signals: list[RiskSignal]) -> str:
    weights = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}
    score = sum(weights[s.severity] for s in signals)

    if score >= 7:
        return "HIGH"
    if score >= 4:
        return "MEDIUM"
    return "LOW"


def assess(signals: list[RiskSignal]) -> dict:
    return {
        "risk_level": classify(signals),
        "signal_count": len(signals),
        "signals": [asdict(s) for s in signals],
    }


def main() -> None:
    signals = [
        RiskSignal("architecture", "MEDIUM", "multiple responsibilities in one module"),
        RiskSignal("testing", "HIGH", "critical path has no automated tests"),
        RiskSignal("operations", "LOW", "health endpoint is present"),
    ]
    print(json.dumps(assess(signals), indent=2))


if __name__ == "__main__":
    main()
