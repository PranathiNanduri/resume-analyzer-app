# components/resume_uploader.py
import streamlit as st
from PyPDF2 import PdfReader

def resume_upload_component():
    st.subheader("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose your resume (PDF format only)",
        type=["pdf"]
    )

    resume_text = ""

    if uploaded_file:
        st.success("Resume uploaded successfully!")

        # Extract text from PDF using PyPDF2
        try:
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                resume_text += page.extract_text() or ""
        except Exception as e:
            st.error(f"Could not read the PDF: {e}")

    return uploaded_file, resume_text
