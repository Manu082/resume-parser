import streamlit as st
from parser import ResumeParser
from matcher import KeywordMatcher
import pandas as pd
import os
import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Model is not present, so download it
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


st.title("Automated Resume Scanner")

jd_text = st.text_area("Enter Job Description", height=200)

uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", accept_multiple_files=True)

if st.button("Scan Resumes") and jd_text and uploaded_files:
    matcher = KeywordMatcher(jd_text)
    parser = ResumeParser()
    results = []

    for file in uploaded_files:
        with open(file.name, 'wb') as f:
            f.write(file.read())

        text = parser.parse_resume(file.name)
        score = matcher.match_score(text)
        results.append({'FileName': file.name, 'Score': score})

    df = pd.DataFrame(results).sort_values(by='Score', ascending=False)
    st.write("Ranked Candidates")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results as CSV", csv, "results.csv", "text/csv")

