# StillWrong

One fact changed. Find what's still wrong.

## Change

```text
{
  "entity": "Orion-1",
  "fact": "approved budget",
  "old": "USD 15000",
  "new": "USD 12000",
  "authority": "User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget."
}
```


## Findings

Stale: 5 · Derived: 1 · Needs review: 4


### Finding 1 · stale

```text
budget.xlsx — Summary!B7
```


Original:

```text
15000
```

Reason:

```text
Synthetic reference: current project budget input retains superseded amount.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
12000
```


### Finding 2 · needs_review

```text
budget.xlsx — Summary!B8
```


Original:

```text
=B7*0.2
```

Reason:

```text
Recalculate after updating the budget input; the cached result is missing and this helper does not evaluate spreadsheet formulas.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Review needed; no correction verified
```


### Finding 3 · stale

```text
proposal.docx — body/paragraph 1
```


Original:

```text
Orion-1 current proposal budget: USD 15000
```

Reason:

```text
Synthetic reference finding, authored from the known fixture answer key.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Orion-1 current proposal budget: USD 12000
```


### Finding 4 · needs_review

```text
proposal.docx — section 1/footer/paragraph 1
```


Original:

```text
Orion-1 current sales budget: USD 15k
```

Reason:

```text
Confirm whether sales budget is the approved project budget; identical numbers do not establish equivalence.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Review needed; no correction verified
```


### Finding 5 · stale

```text
proposal.md — line 1
```


Original:

```text
Orion-1 current proposal budget: USD 15000
```

Reason:

```text
Synthetic reference finding, authored from the known fixture answer key.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Orion-1 current proposal budget: USD 12000
```


### Finding 6 · needs_review

```text
proposal.md — line 2
```


Original:

```text
Orion-1 current sales budget: USD 15k
```

Reason:

```text
Confirm whether sales budget is the approved project budget; identical numbers do not establish equivalence.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Review needed; no correction verified
```


### Finding 7 · stale

```text
proposal.md — line 3
```


Original:

```text
Orion-1 current approved budget: USD 15,000
```

Reason:

```text
Synthetic reference finding, authored from the known fixture answer key.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Orion-1 current approved budget: USD 12,000
```


### Finding 8 · derived

```text
proposal.md — line 4
```


Original:

```text
Orion-1 current advance: USD 3000; advance is 20% of approved budget.
```

Reason:

```text
Synthetic reference finding, authored from the known fixture answer key.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Orion-1 current advance: USD 2400; advance is 20% of approved budget.
```

Calculation:

```text
12000 × 0.20 = 2400
```


### Finding 9 · stale

```text
proposal.pdf — page 1
```


Original:

```text
Orion-1 current proposal budget: USD 15000
```

Reason:

```text
Synthetic reference finding, authored from the known fixture answer key.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Orion-1 current proposal budget: USD 12000
```


### Finding 10 · needs_review

```text
sales.pptx — slide 1/shape 1/shape 1
```


Original:

```text
Orion-1 current sales budget: USD 15k
```

Reason:

```text
Confirm whether sales budget is the approved project budget; identical numbers do not establish equivalence.
```

Authority:

```text
User: current Orion-1 approved budget is USD 12000; advance remains 20% of approved budget.
```

Correction draft:

```text
Review needed; no correction verified
```


## Preserved references

```text
r5 · proposal.docx · body/table 1/row 1/cell 1/table 1/row 1/cell 1/paragraph 1
Original: Historical: Orion-1 approved budget was USD 15000 last year.
Reason: Historical, rejected, unrelated, or already correct reference.
```


```text
r11 · proposal.md · line 5
Original: Historical: Orion-1 approved budget was USD 15000 last year.
Reason: Historical, rejected, unrelated, or already correct reference.
```


```text
r12 · proposal.md · line 6
Original: Unrelated project Vega current budget: USD 15000
Reason: Historical, rejected, unrelated, or already correct reference.
```


```text
r13 · proposal.md · line 7
Original: Orion-1 rejected option: USD 15000
Reason: Historical, rejected, unrelated, or already correct reference.
```


```text
r14 · proposal.md · line 8
Original: Orion-1 current approved budget: USD 12000
Reason: Historical, rejected, unrelated, or already correct reference.
```


## Extraction coverage

```text
budget.xlsx: partial; Summary!B8: cached result missing; Summary!B8: formula not recalculated; Workbook charts, comments, drawings and external references not reviewed
```


```text
locked.pdf: unreadable; ValueError: Encrypted PDF; supply an unlocked copy
```


```text
proposal.docx: partial; Tracked revisions, textboxes or footnotes not reviewed; Word fields, comments, drawings and revision history not semantically reviewed
```


```text
proposal.md: extracted; 
```


```text
proposal.pdf: partial; PDF text order/table structure not visually verified
```


```text
REQUEST.md: extracted; 
```


```text
rules.txt: extracted; 
```


```text
sales.pptx: partial; Slide masters, layouts and speaker notes not reviewed
```


Evidence integrity validated; semantic judgments require review. No confirmed findings does not certify unreviewed content. Source files were not edited.