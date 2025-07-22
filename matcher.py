# utils/matcher.py

import json
import os

WEIGHTS_PATH = os.path.join("config", "weights.json")

def load_weights():
    try:
        with open(WEIGHTS_PATH, "r", encoding="utf-8") as f:
            weights = json.load(f)
        must_weight = float(weights.get("must_have_weight", 0.7))
        good_weight = float(weights.get("good_to_have_weight", 0.3))
    except Exception:
        must_weight = 0.7
        good_weight = 0.3
    return must_weight, good_weight

def calculate_match(resume_skills, must_have_skills, good_to_have_skills):
    resume_skills = [skill.lower() for skill in resume_skills]
    must_have_skills = [skill.lower() for skill in must_have_skills]
    good_to_have_skills = [skill.lower() for skill in good_to_have_skills]

    matched_must_have = [skill for skill in must_have_skills if skill in resume_skills]
    matched_good_to_have = [skill for skill in good_to_have_skills if skill in resume_skills]

    missing_must_have = list(set(must_have_skills) - set(matched_must_have))
    missing_good_to_have = list(set(good_to_have_skills) - set(matched_good_to_have))

    total_skills = len(must_have_skills) + len(good_to_have_skills)
    matched_total = len(matched_must_have) + len(matched_good_to_have)
    match_percent = round((matched_total / total_skills) * 100, 2) if total_skills else 0.0

    # Load configurable weights
    weight_must, weight_good = load_weights()

    must_contrib = (len(matched_must_have) / len(must_have_skills)) * weight_must if must_have_skills else 0
    good_contrib = (len(matched_good_to_have) / len(good_to_have_skills)) * weight_good if good_to_have_skills else 0
    weighted_score = round((must_contrib + good_contrib) * 100, 2)

    verdict = get_verdict(weighted_score)

    return {
        "match_percent": match_percent,
        "weighted_score": weighted_score,
        "matched_must_have": matched_must_have,
        "matched_good_to_have": matched_good_to_have,
        "missing_must_have": missing_must_have,
        "missing_good_to_have": missing_good_to_have,
        "matched_skills": matched_must_have + matched_good_to_have,
        "missing_skills": missing_must_have + missing_good_to_have,
        "total_skills": total_skills,
        "verdict": verdict
    }

def get_verdict(score):
    if score >= 80:
        return "🟢 Highly Suitable"
    elif score >= 60:
        return "🟡 Moderately Suitable"
    else:
        return "🔴 Not Suitable"
