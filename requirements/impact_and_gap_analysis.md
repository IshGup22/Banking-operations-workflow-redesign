# Gap and Impact Analysis

| Dimension | AS-IS workflow | TO-BE design | Stakeholder impact |
|---|---|---|---|
| Intake | 500 records manually opened | All 500 batch-classified | Operations: less repetitive inspection |
| Exception identification | All items treated as review work | 150 exceptions routed by rule | Finance: clearer follow-up priorities |
| Clean cases | Manual clearance | 350 auto-clear candidates | Controls: formal validation needed before live use |
| Traceability | Spreadsheet notes | Linked RTM, stories and acceptance criteria | QA: easier requirement verification |
| Reporting | Counts assembled manually | Exportable summary + categorized queue | Product / project manager: visibility |
| Time (assumed) | 2000 review minutes | 785 modeled minutes | Estimated reduction 60.75% |

## Change impact and risks
- Incorrect tolerance could misroute small mismatches; require Product Owner / Finance approval
- In production, duplicate logic requires an actual transaction-key policy, not a supplied simulation flag
- Real process time varies by case complexity; estimate is for scenario comparison only
- No real project manager or client was involved; personas are instructional

## Mitigations
- Test boundary values and rule priority
- Maintain explicit exception reason and original values
- Pilot on an approved, de-identified dataset before any actual deployment
