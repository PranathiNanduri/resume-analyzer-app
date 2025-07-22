# utils/skill_classifier.py
import json
import os

DEFAULT_WEIGHTS_PATH = os.path.join("config", "weights.json")

def load_skill_weights(weights_path=DEFAULT_WEIGHTS_PATH):
    """Load skill weight configuration from JSON"""
    with open(weights_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    must_have = [skill.lower() for skill in data.get("must_have", [])]
    good_to_have = [skill.lower() for skill in data.get("good_to_have", [])]
    return must_have, good_to_have

def classify_skills(jd_skills, weights_path=DEFAULT_WEIGHTS_PATH):
    """Classify job description skills into must-have and good-to-have categories"""
    must_have_ref, good_to_have_ref = load_skill_weights(weights_path)

    jd_skills = [s.lower() for s in jd_skills]

    must_have = [skill for skill in jd_skills if skill in must_have_ref]
    good_to_have = [skill for skill in jd_skills if skill in good_to_have_ref and skill not in must_have]
    
    return must_have, good_to_have
