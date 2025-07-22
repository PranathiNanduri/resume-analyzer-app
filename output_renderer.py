import streamlit as st

def render_summary(summary):
    st.subheader("📊 Skill Analysis Summary")

    total_skills = summary.get('total_skills', 0)
    matched = summary.get('matched_skills', [])
    missing = summary.get('missing_skills', [])
    match_percent = summary.get('match_percent', 0.0)
    weighted_score = summary.get('weighted_score', 0.0)
    verdict = summary.get('verdict', "N/A")

    st.markdown(f"""
    | **Category** | **Result** |
    |--------------|------------|
    | Total JD Skills | {total_skills} |
    | Matched Skills | {", ".join(matched) if matched else "None"} |
    | Missing Skills | {", ".join(missing) if missing else "None"} |
    | Skill Match % | {match_percent:.2f}% |
    | Weighted Suitability Score | {weighted_score:.2f}% |
    | Verdict | {verdict} |
    """)


def render_skill_details(details):
    st.subheader("🔧 Skill Match Details")

    st.markdown("**✅ Matched Must-Have Skills:**")
    matched_core = details.get('matched_core', [])
    st.write("• " + "\n• ".join(matched_core) if matched_core else "None")

    st.markdown("**✅ Matched Good-to-Have Skills:**")
    matched_secondary = details.get('matched_secondary', [])
    st.write("• " + "\n• ".join(matched_secondary) if matched_secondary else "None")

    st.markdown("**❌ Missing Must-Have Skills:**")
    missing_core = details.get('missing_core', [])
    st.write("• " + "\n• ".join(missing_core) if missing_core else "None")

    st.markdown("**❌ Missing Good-to-Have Skills:**")
    missing_secondary = details.get('missing_secondary', [])
    st.write("• " + "\n• ".join(missing_secondary) if missing_secondary else "None")


def render_recommendations(recommendations):
    st.subheader("📘 Recommended Learning Paths")
    if not recommendations:
        st.write("No specific recommendations at the moment.")
    else:
        for skill, course in recommendations.items():
            st.markdown(f"**{skill.title()}**: [{course['title']}]({course['url']})")


def render_chat_feedback(feedback):
    st.subheader("💬 Personalized Chat Feedback")
    if feedback:
        st.info(feedback)
    else:
        st.write("No AI feedback available.")


# ✅ Wrapper to render all output
def render_output(summary, details, recommendations, feedback):
    st.markdown("---")
    render_summary(summary)

    st.markdown("---")
    render_skill_details(details)

    st.markdown("---")
    render_recommendations(recommendations)

    st.markdown("---")
    render_chat_feedback(feedback)
