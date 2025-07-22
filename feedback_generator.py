import openai
import streamlit as st
from openai import OpenAI

# 1️⃣ Rule-Based Local Feedback (No API needed)
def generate_feedback(match_percent, must_have_matched, must_have_missing,
                      good_to_have_matched, good_to_have_missing, job_title):
    if match_percent >= 80:
        verdict = "🟢 Highly Suitable"
        tone = "Excellent work! You’re ready for this role."
    elif 60 <= match_percent < 80:
        verdict = "🟡 Moderately Suitable"
        missing_skills = ", ".join(must_have_missing[:2]) or "some core topics"
        tone = f"You're doing well. Consider brushing up on: {missing_skills}."
    else:
        verdict = "🔴 Not Suitable Yet"
        missing_skills = ", ".join(must_have_missing[:3]) or "essential foundations"
        tone = f"Start with learning: {missing_skills}."

    feedback = f"""
💬 Personalized Chat Feedback:

"Hi! Based on your resume, you're {match_percent:.1f}% aligned with the **{job_title}** role.

✅ Matched Core Skills: {', '.join(must_have_matched) or 'None'}
❌ Missing Core Skills: {', '.join(must_have_missing) or 'None'}

✅ Matched Good-to-Have Skills: {', '.join(good_to_have_matched) or 'None'}
❌ Missing Good-to-Have Skills: {', '.join(good_to_have_missing) or 'None'}

⭐ Recommendation: {tone}

🧾 Verdict: {verdict}."
"""
    return feedback


# 2️⃣ GPT-Based Feedback using OpenAI >= 1.0.0 API
def generate_llm_feedback(resume_text, jd_text):
    try:
        client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    except Exception:
        return "⚠️ OpenAI API key not configured. Skipping GPT feedback."

    prompt = f"""
You're a senior career coach. A candidate submitted this resume:

-----------------
{resume_text}
-----------------

They're applying for the following job:

-----------------
{jd_text}
-----------------

Provide clear, structured, and personalized feedback including:
- Suitability level (Strong, Average, Low)
- Strengths (Top skills they already have)
- Missing key skills
- Learning recommendations
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT feedback generation failed:\n{str(e)}"
