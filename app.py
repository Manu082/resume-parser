import streamlit as st
from parser import ResumeParser
from matcher import KeywordMatcher
import pandas as pd
import time
import os

st.title("Automated Resume Scanner")

st.markdown("""
This app scans uploaded resumes (PDF/DOCX), matches them with a given Job Description, 
and ranks candidates by relevance score.
""")

# Text area for Job Description
jd_text = st.text_area("Enter Job Description", height=200, placeholder="Paste your job description here...")

# Upload multiple files
uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", accept_multiple_files=True)

# Limit check
if uploaded_files and len(uploaded_files) > 50:
    st.warning("⚠️ You can upload a maximum of 50 resumes at once. Please remove some files and try again.")
    uploaded_files = []  # Clear list so button won't work
else:
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} resume(s) uploaded.")

if st.button("Scan Resumes"):

    if not jd_text:
        st.error("❌ Please enter a Job Description first.")
    elif not uploaded_files:
        st.error("❌ Please upload at least one resume (max 50).")
    else:
        matcher = KeywordMatcher(jd_text)
        parser = ResumeParser()
        results = []

        # Progress bar
        progress_bar = st.progress(0)
        total_files = len(uploaded_files)

        for i, file in enumerate(uploaded_files):
            with open(file.name, 'wb') as f:
                f.write(file.read())

            text = parser.parse_resume(file.name)
            score = matcher.match_score(text)
            results.append({'FileName': file.name, 'Score': score})

            # Update progress
            progress_bar.progress((i + 1) / total_files)

            time.sleep(0.1)  # Optional delay for smoother progress animation

        # Results table
        df = pd.DataFrame(results).sort_values(by='Score', ascending=False)
        st.success("✅ Scanning complete. Ranked candidates below:")
        st.dataframe(df)

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Results as CSV", csv, "results.csv", "text/csv")
