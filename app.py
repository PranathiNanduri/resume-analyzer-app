import streamlit as st
import os
import re
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from utils.resume_parser import extract_resume_text, extract_skills_from_text
from utils.jd_parser import extract_jd_text_and_skills
from utils.skill_classifier import classify_skills
from utils.matcher import calculate_match
from utils.recommender import recommend_courses
from utils.feedback_generator import generate_feedback, generate_llm_feedback
from components.resume_uploader import resume_upload_component
from components.jd_input_handler import jd_input_component
from components.output_renderer import render_output

# Page setup
st.set_page_config(
    page_title="🔍 Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>📄 Resume Analyzer with AI Feedback</h1>", unsafe_allow_html=True)

# Show logo if present
if os.path.exists("assets/logo.png"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/logo.png", width=140)

# Upload resume and get text
uploaded_file, resume_text = resume_upload_component()

# Input JD text (either paste or folder)
jd_input = jd_input_component()
jd_text = "\n".join(jd_input) if isinstance(jd_input, list) else jd_input

# Extract job title from JD
def extract_job_title(text):
    match = re.search(r"(?:Job Title|Position):?\s*(.+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip().split('\n')[0]
    lines = text.split('\n')
    for line in lines:
        if len(line.split()) <= 5 and any(word[0].isupper() for word in line.split()):
            return line.strip()
    return "Unknown Role"

# Process once both inputs are ready
if resume_text and jd_text:
    resume_skills = extract_skills_from_text(resume_text)
    _, jd_skills = extract_jd_text_and_skills(jd_text)
    must_have, good_to_have = classify_skills(jd_skills)
    results = calculate_match(resume_skills, must_have, good_to_have)
    learning_paths = recommend_courses(results['missing_must_have'] + results['missing_good_to_have'])
    job_title = extract_job_title(jd_text)

    # Rule-based feedback
    feedback = generate_feedback(
        match_percent=results['match_percent'],
        must_have_matched=results['matched_must_have'],
        must_have_missing=results['missing_must_have'],
        good_to_have_matched=results['matched_good_to_have'],
        good_to_have_missing=results['missing_good_to_have'],
        job_title=job_title
    )

    # LLM feedback only if OpenAI key available
    gpt_feedback = None
    if st.secrets.get("openai", {}).get("api_key"):
        gpt_feedback = generate_llm_feedback(resume_text, jd_text)

    # Render output UI
    render_output(results, {
        "matched_core": results['matched_must_have'],
        "matched_secondary": results['matched_good_to_have'],
        "missing_core": results['missing_must_have'],
        "missing_secondary": results['missing_good_to_have']
    }, learning_paths, gpt_feedback or feedback)

    # PDF export logic
    def generate_pdf_output():
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 40

        def write_line(text, y_pos, max_width=500):
            lines = []
            while len(text) > 0:
                if len(text) <= 80:
                    lines.append(text)
                    break
                else:
                    idx = text.rfind(' ', 0, 80)
                    if idx == -1:
                        idx = 80
                    lines.append(text[:idx])
                    text = text[idx+1:]
            for line in lines:
                p.drawString(30, y_pos, line)
                y_pos -= 15
            return y_pos

        p.setFont("Helvetica-Bold", 14)
        p.drawString(30, y, f"Resume Analysis Report - {job_title}")
        y -= 30
        p.setFont("Helvetica", 12)

        for label, val in [
            ("Match %", f"{results['match_percent']:.2f}%"),
            ("Weighted Score", f"{results['weighted_score']:.2f}%"),
            ("Matched Must-Have", ", ".join(results['matched_must_have']) or "None"),
            ("Matched Good-to-Have", ", ".join(results['matched_good_to_have']) or "None"),
            ("Missing Must-Have", ", ".join(results['missing_must_have']) or "None"),
            ("Missing Good-to-Have", ", ".join(results['missing_good_to_have']) or "None"),
        ]:
            y = write_line(f"{label}: {val}", y)
            y -= 10
            if y < 80:
                p.showPage()
                y = height - 40

        y -= 20
        p.setFont("Helvetica-Bold", 12)
        p.drawString(30, y, "Career Coach Feedback:")
        y -= 30
        p.setFont("Helvetica", 11)

        feedback_text = gpt_feedback or feedback or "No feedback available."
        for line in feedback_text.split("\n"):
            y = write_line(line.strip(), y)
            if y < 80:
                p.showPage()
                y = height - 40

        p.save()
        pdf_bytes = buffer.getvalue()
        buffer.close()
        return pdf_bytes

    pdf_data = generate_pdf_output()
    b64_pdf = base64.b64encode(pdf_data).decode()

    st.download_button(
        label="📄 Download Analysis PDF",
        data=pdf_data,
        file_name="resume_analysis.pdf",
        mime="application/pdf"
    )

else:
    st.warning("📂 Please upload a resume and paste/provide a job description to begin analysis.")
