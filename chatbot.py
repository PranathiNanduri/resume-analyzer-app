# components/chatbot.py
import streamlit as st
import openai

def chatbot_interface(resume_text, jd_text, match_summary):
    st.subheader("🤖 AI Chat Feedback (Beta)")

    # ✅ Check API key
    if "openai" not in st.secrets or "api_key" not in st.secrets["openai"]:
        st.warning("OpenAI API key not found. Please add it to Streamlit secrets.")
        return

    # ✅ Set up OpenAI client (new way)
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

    # ✅ Shorten content to avoid token limits
    resume_excerpt = resume_text[:1500].replace('\n', ' ')
    jd_excerpt = jd_text[:1500].replace('\n', ' ')

    # ✅ GPT prompt
    prompt = f"""
    Based on the following resume and job description, give personalized feedback:

    RESUME:
    {resume_excerpt}

    JOB DESCRIPTION:
    {jd_excerpt}

    SUMMARY:
    - Total JD Skills: {match_summary['total_skills']}
    - Matched: {match_summary['matched_skills']}
    - Missing: {match_summary['missing_skills']}
    - Match %: {match_summary['match_percent']}%
    - Weighted Score: {match_summary['weighted_score']}%
    - Verdict: {match_summary['verdict']}

    Provide clear, encouraging feedback like a career coach. Mention what is strong, what’s missing, and what to focus on next.
    """

    with st.spinner("Generating smart feedback..."):
        try:
            # ✅ New API call structure
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6
            )

            feedback = response.choices[0].message.content
            st.success("✅ Feedback ready!")
            st.markdown("#### 📬 Personalized Suggestions:")
            st.markdown(feedback)

        except Exception as e:
            st.error(f"❌ Error generating feedback: {str(e)}")
