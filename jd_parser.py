import re

# Central skill reference list — must match resume parser
SKILL_DB = [
    "python", "sql", "excel", "tableau", "power bi", "communication",
    "r", "aws", "snowflake", "machine learning", "data analysis",
    "a/b testing", "data cleaning", "statistics", "deep learning",
    "nlp", "hadoop", "spark", "azure", "java", "c++", "cv",
    "siem", "firewalls", "threat detection", "network protocols",
    "system hardening", "log analysis", "vulnerability scanning",
    "cloud security", "ceh", "security+"
]

def extract_jd_text_and_skills(jd_text):
    """
    Cleans and extracts job description skills from given text.

    Returns:
        cleaned_text (str): normalized JD text
        found_skills (list): matched skills from SKILL_DB
    """
    jd_text_cleaned = jd_text.lower()
    found_skills = set()

    for skill in SKILL_DB:
        # Use word boundaries to match complete skill names
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, jd_text_cleaned):
            found_skills.add(skill)

    # Fallback if no skills matched
    if not found_skills:
        found_skills.add("No recognizable skills found")

    return jd_text_cleaned, sorted(found_skills)
