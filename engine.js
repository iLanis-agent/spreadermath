// Spreader Math engine - hypothetical arithmetic on labeled norms only.
// No verdicts about dial settings or what any spreader should be set to:
// the manual and the bag label own that call.

function plural(n, one, many) { return n === 1 ? one : many; }

function bagCount(lawn, coverage) {
  if (!(lawn > 0)) throw new Error("the lawn size must be above zero");
  if (!(coverage > 0)) throw new Error("the claimed coverage must be above zero");
  return Math.ceil(lawn / coverage);
}

function bagTruth(lawn, coverage) {
  const bags = bagCount(lawn, coverage);
  let verdict;
  if (bags <= 1) verdict = "one bag and done";
  else if (bags <= 3) verdict = "a couple of bags honestly";
  else if (bags <= 8) verdict = "a shelf of bags";
  else verdict = "a pallet plan";
  return `The bag claims ${coverage} square feet; your ${lawn}-square-foot lawn is ${bags} ${plural(bags, "bag", "bags")} - ${verdict}.`;
}

function totalPounds(lawn, rate) {
  if (!(lawn > 0)) throw new Error("the lawn size must be above zero");
  if (!(rate > 0)) throw new Error("the rate must be above zero");
  return lawn / 1000 * rate;
}

function refillTruth(lawn, rate, hopper) {
  if (!(hopper > 0)) throw new Error("the hopper size must be above zero");
  const pounds = totalPounds(lawn, rate);
  const fills = Math.ceil(pounds / hopper);
  let verdict;
  if (fills <= 1) verdict = "one pour and done";
  else if (fills <= 3) verdict = "a few trips to the bag";
  else if (fills <= 6) verdict = "a sleeve of refills honestly";
  else verdict = "the bag will outlive the hopper";
  return `${lawn} square feet at ${rate} pounds a thousand is ${pounds.toFixed(1)} pounds - ${fills} ${plural(fills, "fill", "fills")} of the ${hopper}-pound hopper, ${verdict}.`;
}

function walkTruth(lawn, swath, speed) {
  if (!(lawn > 0)) throw new Error("the lawn size must be above zero");
  if (!(swath > 0)) throw new Error("the swath must be above zero");
  if (!(speed > 0)) throw new Error("the pace must be above zero");
  const minutes = lawn / (swath * speed);
  let verdict;
  if (minutes <= 10) verdict = "done before the kettle";
  else if (minutes <= 25) verdict = "a working loop";
  else if (minutes <= 60) verdict = "a long lap honestly";
  else verdict = "a podcast of laps";
  return `${lawn} square feet at ${swath} feet a pass and ${speed} feet a minute is ${minutes.toFixed(1)} minutes of walking - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { bagCount, bagTruth, totalPounds, refillTruth, walkTruth };
}
