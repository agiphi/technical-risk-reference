from .models import RiskSignal
def classify(score): return "HIGH" if score>=70 else "MEDIUM" if score>=35 else "LOW"
def assess(signals:list[RiskSignal]):
 if not signals:return {"score":0.0,"level":"LOW","signals":[]}
 score=sum(max(0,min(100,s.severity)) for s in signals)/len(signals)
 return {"score":round(score,2),"level":classify(score),"signals":[s.__dict__ for s in signals]}