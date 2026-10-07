from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class RiskSignal:
    name: str
    category: str
    severity: int
    evidence: str

@dataclass(frozen=True)
class RiskFinding:
    name: str
    category: str
    severity: int
    evidence: str
    level: str

    def to_dict(self):
        return asdict(self)
