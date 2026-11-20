# UAT summary — demonstration evidence
**Scope:** 20 documented scenarios, 12 user stories, 25 acceptance criteria, 12 business/functional rule groups

The CSV contains 20 scenarios and expected outcomes. The Python unit-test suite exercises routing boundaries, rule precedence, deterministic metrics, and dataset completeness. This is **simulation-based validation**, not user sign-off by a bank or client.

- Functional scenarios: `uat/uat_test_scenarios.csv`
- Automated regression results: run `python -m unittest discover -s tests -v`
- Manual acceptance / document reviews: verify BRD, FRD, RTM, process diagrams, and metrics
- Decision: simulation is suitable as a portfolio demonstration; **no production go-live approval exists**

## Remaining UAT work for a real deployment
Confirm signed requirements, access controls, genuine source interfaces, exception handling ownership, sample size, processing performance, and signed business acceptance.
