import json
from .classifier import assess

def build_report(signals):
    result=assess(signals)
    result["signal_count"]=len(signals)
    return result

def to_json(signals):
    return json.dumps(build_report(signals),sort_keys=True,indent=2)
