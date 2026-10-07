from src.main import RiskSignal, assess, classify


def test_classification():
    signals = [
        RiskSignal("code", "HIGH", "large module"),
        RiskSignal("tests", "MEDIUM", "partial coverage"),
    ]
    assert classify(signals) == "MEDIUM"


def test_report():
    result = assess([RiskSignal("ops", "LOW", "health check")])
    assert result["risk_level"] == "LOW"
    assert result["signal_count"] == 1
