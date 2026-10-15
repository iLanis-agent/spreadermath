# Spreader Math

Honest lawn-spreading arithmetic. The bag claims a whole lawn; Spreader Math divides, multiplies
and tells you how many trips back to the bag the afternoon really holds.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The bag truth** - your lawn vs. the claimed coverage per bag: the honest bag count.
- **The refill truth** - label rate times lawn into pounds, pounds into hopper fills.
- **The walk truth** - lawn, swath width and pace into honest minutes of walking.

## The boundary

Spreader Math keeps bag, refill and walking arithmetic only. It gives no verdicts about dial
settings or what any spreader should be set to - that call belongs to the spreader's manual and
the bag's label. Follow the product label exactly; the label is the law of the lawn. Every figure
is hypothetical arithmetic on labeled norms, not a statement about any real product or spreader.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 28 cases / 28 checks
```

Live at https://ilanis-agent.github.io/spreadermath/
