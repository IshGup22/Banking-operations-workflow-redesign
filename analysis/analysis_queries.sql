-- SQL illustration for a normalized import table (SQLite-compatible)
-- CSV import schema: reconciliation_cases(record_id, customer_id, payment_ref,
-- bank_amount, ledger_amount, age_days, duplicate_flag, seeded_scenario)
SELECT seeded_scenario, COUNT(*) AS case_count
FROM reconciliation_cases
GROUP BY seeded_scenario ORDER BY case_count DESC;

SELECT CASE
 WHEN duplicate_flag='Y' THEN 'DUPLICATE'
 WHEN COALESCE(TRIM(payment_ref),'')='' THEN 'MISSING_REFERENCE'
 WHEN ROUND(ABS(bank_amount-ledger_amount),2)>0.01 THEN 'AMOUNT_MISMATCH'
 WHEN age_days>7 THEN 'AGED_ITEM'
 ELSE 'MATCH' END AS reason, COUNT(*) AS n
FROM reconciliation_cases GROUP BY reason;

SELECT COUNT(*) AS total_records,
 SUM(CASE WHEN duplicate_flag='N' AND COALESCE(TRIM(payment_ref),'')<>''
 AND ROUND(ABS(bank_amount-ledger_amount),2)<=0.01 AND age_days<=7 THEN 1 ELSE 0 END) AS auto_clear_candidates
FROM reconciliation_cases;
