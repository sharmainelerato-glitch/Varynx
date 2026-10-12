# VARYNX v2 — Light & Navy

A red-team research workbench for controlled contextual comparison and candidate behavioral-boundary discovery. **Demo fixtures and imported examples are not verified Apertus findings.**

## Run (Windows PowerShell)

```powershell
py -m pip install -r requirements.txt
py app.py
```
Open http://127.0.0.1:5000.

## What is new
- Cross-country and within-country one-dimension flip candidates
- Persistent SQLite evidence library (`data/varynx.sqlite3`)
- Import manually captured responses with JSON and provenance warning
- JSON/Markdown evidence exports
- Explicit opt-in to live model calls to avoid accidental charges

## Optional live endpoint
Copy `.env.example` to `.env` and supply an OpenAI-compatible inference endpoint and credentials. Live calls may incur charges. HF_TOKEN alone is **not** read by this application; use `LLM_API_KEY` for a compatible endpoint.

## Manual import format
See `data/import_example.json`. Keep the exact actual prompts and responses. Imported rows are **not automatically verified**.

## Limitations
The classifier is a simple refusal-string heuristic. One-dimensional contrasts are candidate points, not proven minimal causes. Human review, repeated trials, model version, temperature, seed, and controlled language/context are necessary for reproducible claims.

## Submission
Check official Track 1A requirements and submit only genuine Apertus findings. This package is a functional research prototype, not a complete validated submission.


## V3 visual edition
Includes original SVG VARYNX brand mark, contextual comparison illustration, redesigned Light & Navy hero, navigation and analytics cards. No external image assets are required; optional Google Fonts gracefully fall back to system fonts. The engine and API remain the V2 prototype.
