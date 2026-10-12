# VARYNX — Technical Report (working draft)

## Research question
Can a controlled change in contextual framing alter Apertus refusal/answer behavior, and can the smallest responsible change be isolated reproducibly?

## Architecture
Flask serves a responsive light/navy dashboard and a JSON API. The evaluation engine builds country/framing prompts, calls an OpenAI-compatible model endpoint, stores raw responses in memory, classifies responses with an explicitly imperfect heuristic, and emits JSON/Markdown evidence.

## Protocol
Use an exact Apertus 8B/70B model identifier and endpoint; preserve model version, decoding parameters and exact prompts. Compare one variable at a time. Repeat multiple times to estimate stochastic variance. Human reviewers should assess whether a flip is a genuine safety failure, rather than normal contextual adaptation. Minimize multi-variable prompts with a proper delta-debugger before claiming a minimal point.

## Limitations
The bundled offline mode is synthetic and cannot substantiate any model claim. Current refusal heuristics have unknown accuracy. No multilingual native-language translations, statistical confidence intervals, or verified issue reports have been produced yet.

## Ethics
Only test approved endpoints, avoid including personal data, and publish responsibly reviewed evidence.


## V2 methodology note
The candidate detector finds pairs differing in exactly one configured dimension. It does not establish causal minimality, and no real Apertus finding is claimed by this package.
