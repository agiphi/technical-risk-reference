from technical_risk.classifier import assess, classify
from technical_risk.models import RiskSignal
from technical_risk.report import build_report


def test_classification_boundaries():
    assert classify(0) == "LOW"
    assert classify(35) == "MEDIUM"
    assert classify(70) == "HIGH"


def test_assessment_is_deterministic():
    signals=[
        RiskSignal("module_size","code",80,"large module"),
        RiskSignal("tests","quality",20,"tests present"),
    ]
    result=assess(signals)
    assert result["score"] == 50.0
    assert result["level"] == "MEDIUM"


def test_empty_assessment_is_safe():
    assert assess([]) == {"score":0.0,"level":"LOW","signals":[]}


def test_report_contains_count():
    signals=[RiskSignal("ops","infrastructure",60,"missing readiness check")]
    assert build_report(signals)["signal_count"] == 1
