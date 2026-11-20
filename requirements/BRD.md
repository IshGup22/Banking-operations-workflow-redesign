# Business Requirements Document (BRD)
**Project:** Banking Operations Workflow Redesign  
**Version:** 1.0 | **Status:** Case-study baseline | **Data:** Synthetic

## 1. Business problem
A hypothetical banking operations team manually reviews every account-to-ledger record, including records with exact matches. The workflow creates unnecessary handling effort, inconsistent triage and slow access to exception-level reporting.

## 2. Objectives
- Retain a complete auditable record of every input item
- Reduce modeled manual handling effort without automatically clearing genuine exceptions
- Surface amount mismatches, duplicates, missing references and aged items
- Document requirements, expected behavior and UAT coverage

## 3. Scope
**In scope:** 500 synthetic reconciliation records, deterministic routing rules, exception queue CSV, before/after effort scenario, test evidence, reporting pack.  
**Out of scope:** Live banking integration, customer data, actual production deployment, real stakeholder sign-off, regulatory determination, fraud detection or bank-approved controls.

## 4. Stakeholders (hypothetical personas)
- Finance lead: accuracy, signed-off totals, exception visibility
- Operations reviewer: usable work queue and explicit reason for each flag
- Product Owner: prioritization and scope tradeoffs
- Developer: source-field mapping, routing logic, export requirements
- QA tester: observable outcomes and traceable UAT cases
- Project manager: milestone, risk and decision tracking

## 5. Business requirements
| ID | Requirement | Priority |
|---|---|---|
| BR-01 | All ledger records must remain accounted for | Must |
| BR-02 | Automatically separate clean matches from exceptions | Must |
| BR-03 | Detect mismatched monetary amounts | Must |
| BR-04 | Block duplicate auto-clearance | Must |
| BR-05 | Require traceable payment references | Must |
| BR-06 | Escalate aged records | Must |
| BR-07 | Provide review work queues | Should |
| BR-08 | Quantify expected process efficiency | Should |
| BR-09 | Maintain requirements traceability | Must |
| BR-10 | Support scenario-based UAT | Must |
| BR-11 | Maintain stakeholder decisions | Should |
| BR-12 | Deliver audit-ready exports | Must |

## 6. Success criteria (model estimates, not real operational results)
- 500/500 records classified, no records discarded
- Seeded exception categories routed to manual review
- Complete record-to-reason trace in CSV
- Effort calculation uses stated baseline/to-be assumptions
- 12 user stories, 25 acceptance criteria, 20 illustrative UAT scenarios and 12-row RTM

## 7. Assumptions & constraints
- Synthetic data encodes mutually exclusive scenarios for reviewability
- A record is amount-matched when the absolute difference is no more than $0.01
- Review records with age > 7 days; flag duplicate and missing reference records
- The 60.75% processing-time reduction is a **scenario estimate** based on hypothetical per-case minutes, not a field observation

## 8. Approvals / change history
No external stakeholder approvals were obtained. This document is a portfolio simulation; the case-study author acts as the analyst. A simulated sign-off checklist is provided in `reports/decision_log.md`.
