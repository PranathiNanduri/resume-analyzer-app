# components/jd_input_handler.py

import streamlit as st
import os

def jd_input_component():
    st.subheader("📥 Provide Job Description")
    input_method = st.radio(
        "Select input method:",
        ("Paste JD Text", "Upload JD Folder")
    )

    jd_texts = []

    if input_method == "Paste JD Text":
        jd_text = st.text_area("Paste job description here")
        if jd_text:
            jd_texts.append(jd_text)

    elif input_method == "Upload JD Folder":
        jd_files = st.file_uploader(
            "Upload JD files (txt only)",
            type=["txt"],
            accept_multiple_files=True
        )
        for file in jd_files:
            content = file.read().decode("utf-8")
            jd_texts.append(content)

    return jd_texts
