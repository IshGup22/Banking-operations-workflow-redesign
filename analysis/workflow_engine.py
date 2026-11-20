"""Deterministic BA case-study rule engine, using SYNTHETIC cases.
Run from repository root: python analysis/workflow_engine.py
No external Python dependencies.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
from collections import Counter
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'data'/'synthetic_reconciliation_cases.csv'
OUTPUT=ROOT/'reports'

def decide(record):
    # Priority order is explicit and traceable to BR-02 / FR-02 through FR-06.
    if record['duplicate_flag']=='Y': return 'DUPLICATE','Manual Review'
    if not record['payment_ref'].strip(): return 'MISSING_REFERENCE','Manual Review'
    if abs(Decimal(str(record['bank_amount']))-Decimal(str(record['ledger_amount'])))>Decimal('0.01'):
        return 'AMOUNT_MISMATCH','Manual Review'
    if int(record['age_days'])>7: return 'AGED_ITEM','Manual Review'
    return 'MATCH','Auto Clear'

def analyze(records):
    classified=[]
    for r in records:
        reason,queue=decide(r)
        classified.append({**r,'rule_result':reason,'routing':queue})
    counts=Counter(r['rule_result'] for r in classified)
    n=len(classified)
    manual=sum(r['routing']=='Manual Review' for r in classified)
    automatic=n-manual
    # Modeled labor assumptions, NOT observed timings:
    # baseline 4 min manual review per record;
    # redesigned 5 min per flagged record + 0.1 min oversight per auto cleared record.
    baseline_minutes=round(4*n,2)
    future_minutes=round(5*manual+0.1*automatic,2)
    savings=baseline_minutes-future_minutes
    return classified,{
        'records':n,'matched_auto_cleared':automatic,'manual_review':manual,
        'baseline_manual_minutes':baseline_minutes,'future_estimated_minutes':future_minutes,
        'estimated_minutes_saved':round(savings,2),
        'estimated_time_reduction_pct':round(savings/baseline_minutes*100,2) if n else 0,
        'auto_clear_rate_pct':round(automatic/n*100,2) if n else 0,
        'scenario_counts':dict(sorted(counts.items())),'assumption_note':'Synthetic sample; duration figures are scenario estimates, not production outcomes'
    }

def main():
    with INPUT.open(newline='',encoding='utf-8') as f: source=list(csv.DictReader(f))
    routed,metrics=analyze(source)
    OUTPUT.mkdir(exist_ok=True)
    with (OUTPUT/'classified_cases.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(routed[0]));writer.writeheader();writer.writerows(routed)
    (OUTPUT/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(metrics,indent=2))
if __name__=='__main__':main()
