
from collections import Counter
from itertools import combinations

COUNTRIES = (
    "South Africa",
    "Japan",
    "Switzerland",
    "UK",
    "USA",
    "Germany",
    "France",
    "India",
    "Brazil",
    "Kenya",
    "Nigeria",
    "Australia",
    "Canada",
    "South Korea",
    "China",
    "Singapore",
    "Netherlands",
    "Spain",
    "Mexico",
    "United Arab Emirates",
)
FRAMES = ("research", "academic")


def analyze_repetitions(rows):
    """Measure consistency without claiming that a response is safe."""
    groups = {}

    for row in rows:
        key = (row["country"], row["frame"])
        groups.setdefault(key, []).append(row["behavior"])

    results = []

    for (country, frame), labels in groups.items():
        counts = Counter(labels)
        dominant, count = counts.most_common(1)[0]

        results.append({
            "country": country,
            "frame": frame,
            "trials": len(labels),
            "dominantBehavior": dominant,
            "consistency": round(count / len(labels) * 100, 1),
            "behaviorCounts": dict(counts)
        })

    return results


def find_varynx_points(rows):
    """
    Find one-factor comparison candidates.
    These are not automatically verified causal findings.
    """
    points = []

    for a, b in combinations(rows, 2):
        differences = [
            field for field in ("country", "frame")
            if a[field] != b[field]
        ]

        if len(differences) != 1:
            continue

        if a["behavior"] == b["behavior"]:
            continue

        dimension = differences[0]

        points.append({
            "dimension": dimension,
            "before": {
                "country": a["country"],
                "frame": a["frame"],
                "behavior": a["behavior"]
            },
            "after": {
                "country": b["country"],
                "frame": b["frame"],
                "behavior": b["behavior"]
            },
            "candidatePoint": (
                f"{dimension}: {a[dimension]} → {b[dimension]}"
            ),
            "verifiedMinimal": False,
            "requiresHumanReview": True,
            "explanation": (
                "One context dimension changed alongside "
                "the observed response label. Repeat testing "
                "and human review are required."
            )
        })

    return points


def summarize_v5(rows):
    consistency = analyze_repetitions(rows)
    candidates = find_varynx_points(rows)

    return {
        "engineVersion": "5.0",
        "totalResponses": len(rows),
        "consistency": consistency,
        "varynxPoints": candidates,
        "candidateCount": len(candidates),
        "verified": False,
        "limitations": [
            "Automated response labels are heuristic.",
            "One-factor comparisons do not establish causality.",
            "Synthetic outputs are not real Apertus findings.",
            "Human review is required before reporting findings."
        ]
    }
