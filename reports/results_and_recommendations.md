# Case Study Results & Recommendations

## Executive findings — simulated only
- **500** synthetic reconciliation cases processed
- **350** clean matches eligible for automatic clearance (**70.0%**)
- **150** exceptions retained for manual review, including **60** amount mismatches, **35** duplicates, **30** missing references and **25** aged records
- Manual baseline scenario: **2,000 minutes**
- Proposed routing scenario: **785.0 minutes**
- Estimated workload savings: **1,215.0 minutes (20.25 hours)**, or **60.75%** under defined assumptions

## What the result means
The engine routes clean synthetic items to an auto-clear candidate list and preserves all seeded anomalies in an exception queue. These findings demonstrate decision rules and traceability; they do not establish real-world time savings, fraud prevention, false-positive performance, or production readiness.

## Recommendations
1. Obtain Finance sign-off on tolerances and controls before applying to actual business records
2. Pilot on historical de-identified transactions and measure true handling times by scenario
3. Design duplicate detection based on transaction keys and settlement rules, not a simulation flag
4. Use an RTM and boundary UAT cases to keep revised rules testable
5. Monitor queue aging and false-positive rates during a controlled rollout

## Decision gate
**Status: portfolio demonstration complete; production deployment not approved**
