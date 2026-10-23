"""Score a reviewed pack against synthetic labels. Never pass the key to the reviewer."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('pack', help='e.g. pack-01')
parser.add_argument('evidence')
parser.add_argument('findings')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
key = next(p for p in json.loads((root/'examples/answer-key.json').read_text(encoding='utf-8')) if p['pack']==args.pack)
evidence = json.loads(Path(args.evidence).read_text(encoding='utf-8'))
findings = json.loads(Path(args.findings).read_text(encoding='utf-8'))
index = {r['id']:r for r in evidence['records']}
reported = {index[f['record_id']]['text'] for f in findings['findings']}
positives, negatives = set(key['positive_quotes']), set(key['negative_quotes'])
tp, fp = len(positives & reported), len(negatives & reported)
print(json.dumps({'pack':args.pack,'labelled_true_positives':tp,'labelled_false_positives':fp,'labelled_false_negatives':len(positives-reported),'recall_on_labelled_targets':tp/len(positives),'precision_on_labelled_controls':tp/(tp+fp) if tp+fp else None,'unscored_reported_records':len(reported-positives-negatives),'note':'Only labelled statements are scored. Extra-format claims require independent adjudication; not an overall semantic precision metric.'},indent=2))
