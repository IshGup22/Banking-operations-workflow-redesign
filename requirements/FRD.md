# Functional Requirements Document (FRD)
**Version:** 1.0 | **Status:** Demonstration design | **Environment:** Local Python simulation

## Source-to-target mapping
| Input field | Type | Description | Output mapping |
|---|---|---|---|
| record_id | Text | Unique case ID | Preserved |
| customer_id | Text | Synthetic customer key | Preserved |
| payment_ref | Text | Payment reference | Preserved + checked |
| bank_amount | Decimal | Bank-side amount (USD) | Preserved + compared |
| ledger_amount | Decimal | Ledger-side amount (USD) | Preserved + compared |
| age_days | Integer | Days outstanding | Preserved + evaluated |
| duplicate_flag | Y/N | Seeded duplicate marker | Preserved + evaluated |
| seeded_scenario | Text | Synthetic ground-truth class | Preserved for test evidence |

## Functional rules
| ID | Logic | Reference |
|---|---|---|
| FR-01 | Preserve every unique input record and produce a classification | BR-01 |
| FR-02 | Auto-clear only when all validations pass | BR-02 |
| FR-03 | Flag absolute amount difference greater than $0.01 | BR-03 |
| FR-04 | Duplicate flag takes precedence over other rules | BR-04 |
| FR-05 | Blank payment reference triggers manual review | BR-05 |
| FR-06 | Age greater than 7 days triggers manual review | BR-06 |
| FR-07 | Output reason code and Auto Clear / Manual Review routing | BR-07 |
| FR-08 | Generate baseline and proposed effort model | BR-08 |
| FR-09 | Link rules to stories, criteria and test evidence in RTM | BR-09 |
| FR-10 | Provide repeatable functional UAT scenarios | BR-10 |
| FR-11 | Document assumptions and open sign-off decisions | BR-11 |
| FR-12 | Export classified records, summary metrics, and validation findings | BR-12 |

### Rule precedence
1. Duplicate -> `DUPLICATE`
2. Empty payment reference -> `MISSING_REFERENCE`
3. Amount difference > $0.01 -> `AMOUNT_MISMATCH`
4. Outstanding age > 7 -> `AGED_ITEM`
5. Otherwise -> `MATCH` / `Auto Clear`

### Calculations
- Baseline workload = 500 cases × **4.0 min** per manual review
- Proposed workload = manual exceptions × **5.0 min** + automatic matches × **0.1 min** of oversight
- Reduction (%) = (baseline − proposed) / baseline × 100

These values are hypothetical business-case assumptions. They are not measured processing speeds in a production bank.

### Non-functional expectations
Reproducible outputs, no sensitive personal data, straightforward CSV export, documented dependencies and deterministic case generation.
