"""Import CSV into SQLite and execute example SQL analysis, stdlib only."""
from pathlib import Path
import csv,sqlite3
ROOT=Path(__file__).resolve().parents[1]
cn=sqlite3.connect(':memory:')
cn.execute('CREATE TABLE reconciliation_cases(record_id TEXT,customer_id TEXT,payment_ref TEXT,bank_amount REAL,ledger_amount REAL,age_days INTEGER,duplicate_flag TEXT,seeded_scenario TEXT)')
with (ROOT/'data'/'synthetic_reconciliation_cases.csv').open(newline='') as f:
 data=list(csv.DictReader(f))
cn.executemany('INSERT INTO reconciliation_cases VALUES(?,?,?,?,?,?,?,?)',[(r['record_id'],r['customer_id'],r['payment_ref'],float(r['bank_amount']),float(r['ledger_amount']),int(r['age_days']),r['duplicate_flag'],r['seeded_scenario']) for r in data])
for sql in (ROOT/'analysis'/'analysis_queries.sql').read_text().split(';'):
 statement=sql.strip()
 if statement and 'SELECT' in statement.upper():
  print('QUERY RESULT:',cn.execute(statement).fetchall())
