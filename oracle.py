import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def bag_count(lawn, coverage):
    if not (lawn > 0):
        raise ValueError("the lawn size must be above zero")
    if not (coverage > 0):
        raise ValueError("the claimed coverage must be above zero")
    return math.ceil(lawn / coverage)

def bag_truth(lawn, coverage):
    bags = bag_count(lawn, coverage)
    if bags <= 1:
        verdict = "one bag and done"
    elif bags <= 3:
        verdict = "a couple of bags honestly"
    elif bags <= 8:
        verdict = "a shelf of bags"
    else:
        verdict = "a pallet plan"
    return f"The bag claims {coverage} square feet; your {lawn}-square-foot lawn is {bags} {plural(bags, 'bag', 'bags')} - {verdict}."

def total_pounds(lawn, rate):
    if not (lawn > 0):
        raise ValueError("the lawn size must be above zero")
    if not (rate > 0):
        raise ValueError("the rate must be above zero")
    return lawn / 1000 * rate

def refill_truth(lawn, rate, hopper):
    if not (hopper > 0):
        raise ValueError("the hopper size must be above zero")
    pounds = total_pounds(lawn, rate)
    fills = math.ceil(pounds / hopper)
    if fills <= 1:
        verdict = "one pour and done"
    elif fills <= 3:
        verdict = "a few trips to the bag"
    elif fills <= 6:
        verdict = "a sleeve of refills honestly"
    else:
        verdict = "the bag will outlive the hopper"
    return f"{lawn} square feet at {rate} pounds a thousand is {fixed1(pounds)} pounds - {fills} {plural(fills, 'fill', 'fills')} of the {hopper}-pound hopper, {verdict}."

def walk_truth(lawn, swath, speed):
    if not (lawn > 0):
        raise ValueError("the lawn size must be above zero")
    if not (swath > 0):
        raise ValueError("the swath must be above zero")
    if not (speed > 0):
        raise ValueError("the pace must be above zero")
    minutes = lawn / (swath * speed)
    if minutes <= 10:
        verdict = "done before the kettle"
    elif minutes <= 25:
        verdict = "a working loop"
    elif minutes <= 60:
        verdict = "a long lap honestly"
    else:
        verdict = "a podcast of laps"
    return f"{lawn} square feet at {swath} feet a pass and {speed} feet a minute is {fixed1(minutes)} minutes of walking - {verdict}."

FNS = {"bagTruth": bag_truth, "refillTruth": refill_truth, "walkTruth": walk_truth}

cases = [
 {"fn":"bagTruth","args":[5000,2500]},
 {"fn":"bagTruth","args":[2000,2500]},
 {"fn":"bagTruth","args":[7000,2500]},
 {"fn":"bagTruth","args":[20000,2500]},
 {"fn":"bagTruth","args":[40000,2500]},
 {"fn":"bagTruth","args":[2500,2500]},
 {"fn":"bagTruth","args":[2501,2500]},
 {"fn":"bagTruth","args":[0,2500]},
 {"fn":"bagTruth","args":[5000,0]},
 {"fn":"refillTruth","args":[5000,4,20]},
 {"fn":"refillTruth","args":[10000,4,20]},
 {"fn":"refillTruth","args":[15000,4,20]},
 {"fn":"refillTruth","args":[25000,4,20]},
 {"fn":"refillTruth","args":[50000,4,20]},
 {"fn":"refillTruth","args":[1000,4,20]},
 {"fn":"refillTruth","args":[8000,3,12]},
 {"fn":"refillTruth","args":[0,4,20]},
 {"fn":"refillTruth","args":[5000,0,20]},
 {"fn":"refillTruth","args":[5000,4,0]},
 {"fn":"walkTruth","args":[5000,8,200]},
 {"fn":"walkTruth","args":[2000,8,200]},
 {"fn":"walkTruth","args":[20000,8,200]},
 {"fn":"walkTruth","args":[80000,8,200]},
 {"fn":"walkTruth","args":[200000,8,200]},
 {"fn":"walkTruth","args":[5000,6,150]},
 {"fn":"walkTruth","args":[0,8,200]},
 {"fn":"walkTruth","args":[5000,0,200]},
 {"fn":"walkTruth","args":[5000,8,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
