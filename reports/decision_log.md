# Project decision log (simulation)
| Decision | Rationale | Owner persona | Status |
|---|---|---|---|
| Use CSV for MVP | Reduces dependency on integration | Product Owner | Proposed |
| Allow $0.01 amount difference | Demonstration tolerance | Finance lead | Requires real approval |
| Flag age > 7 days | Provides aged-item prioritization | Operations lead | Requires real approval |
| Prioritize duplicate flag | Avoid auto-clearing flagged duplicates | Risk / QA | Proposed |
| Keep manual-review audit export | Enables reproducibility | Business Analyst | Implemented in simulation |

## Example sprint plan (not actual ceremonies)
**Sprint 1:** discovery, AS-IS mapping, BRD, synthetic source design  
**Sprint 2:** FRD, Python routing rules, criteria, tests  
**Sprint 3:** UAT rehearsal, impact analysis, decision log, presentation  

**Sprint retrospective (simulated):** Explicit rule precedence and boundary cases should be documented earlier; effort assumptions should be validated with real time-and-motion data before any operational recommendation.
