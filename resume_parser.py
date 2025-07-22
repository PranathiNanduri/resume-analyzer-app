import re
from io import BytesIO
from PyPDF2 import PdfReader

# Define a reusable skill database
SKILL_DB = [
    "python", "sql", "excel", "tableau", "power bi", "communication",
    "r", "aws", "snowflake", "machine learning", "data analysis",
    "a/b testing", "data cleaning", "statistics", "deep learning",
    "nlp", "hadoop", "spark", "azure", "java", "c++", "cv"
]

def extract_resume_text(file_bytes):
    """
    Extracts and lowercases text from a PDF resume file.
    """
    text = ""
    try:
        reader = PdfReader(BytesIO(file_bytes))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    except Exception as e:
        print("❌ Error extracting resume text:", e)
    return text.lower()

def extract_skills_from_text(text):
    """
    Extracts matching skills from the resume text.
    Returns a sorted list of unique skills.
    """
    found_skills = set()
    for skill in SKILL_DB:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)
    
    # Optional fallback (for empty case)
    if not found_skills:
        found_skills.add("No recognizable skills found")  # or you can return an empty list

    return sorted(found_skills)
