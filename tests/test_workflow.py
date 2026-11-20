import csv,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'analysis'))
from workflow_engine import decide,analyze,INPUT

def case(**overrides):
 r=dict(payment_ref='PAY-100',bank_amount='100.00',ledger_amount='100.00',duplicate_flag='N',age_days='0',record_id='T-1')
 r.update(overrides);return r
class TestWorkflow(unittest.TestCase):
 def test_clean_auto_clear(self):self.assertEqual(decide(case()),('MATCH','Auto Clear'))
 def test_mismatch(self):self.assertEqual(decide(case(ledger_amount='90.00'))[0],'AMOUNT_MISMATCH')
 def test_one_cent_tolerance(self):self.assertEqual(decide(case(bank_amount='100.00',ledger_amount='100.01'))[0],'MATCH')
 def test_beyond_cent_tolerance(self):self.assertEqual(decide(case(bank_amount='100.00',ledger_amount='100.02'))[0],'AMOUNT_MISMATCH')
 def test_duplicate(self):self.assertEqual(decide(case(duplicate_flag='Y'))[0],'DUPLICATE')
 def test_duplicate_priority(self):self.assertEqual(decide(case(duplicate_flag='Y',payment_ref=''))[0],'DUPLICATE')
 def test_missing_reference(self):self.assertEqual(decide(case(payment_ref=''))[0],'MISSING_REFERENCE')
 def test_age_eight_days(self):self.assertEqual(decide(case(age_days='8'))[0],'AGED_ITEM')
 def test_age_seven_days(self):self.assertEqual(decide(case(age_days='7'))[0],'MATCH')
 def test_review_route(self):self.assertEqual(decide(case(payment_ref=''))[1],'Manual Review')
 def test_full_input_counts(self):
  with INPUT.open(newline='') as f:rows=list(csv.DictReader(f))
  routed,metrics=analyze(rows)
  self.assertEqual(metrics['records'],500)
  self.assertEqual(metrics['matched_auto_cleared'],350)
  self.assertEqual(metrics['manual_review'],150)
  self.assertEqual(len(routed),500)
 def test_estimated_effort(self):
  with INPUT.open(newline='') as f:rows=list(csv.DictReader(f))
  _,metrics=analyze(rows)
  self.assertEqual(metrics['baseline_manual_minutes'],2000)
  self.assertEqual(metrics['future_estimated_minutes'],785)
  self.assertEqual(metrics['estimated_time_reduction_pct'],60.75)
 def test_every_seeded_scenario(self):
  with INPUT.open(newline='') as f:rows=list(csv.DictReader(f))
  routed,_=analyze(rows)
  self.assertTrue(all(r['seeded_scenario']==r['rule_result'] for r in routed))
if __name__=='__main__':unittest.main()
