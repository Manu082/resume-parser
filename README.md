# Automated Resume Scanner

A Python-based tool to **parse resumes (PDF/DOCX)**, **match them to a Job Description**, and **rank candidates** based on keyword relevance.  
Includes an optional **Streamlit web interface** for easy uploading, scanning, and downloading results.

---

## 🚀 Features

✅ Upload multiple resumes at once (PDF/DOCX)  
✅ Limit upload to 50 resumes per batch (with warning)  
✅ Keyword matching with Job Description  
✅ Automatic candidate ranking by relevance score  
✅ Export results to CSV  
✅ Streamlit Web UI with progress bar and user-friendly controls  

---

## 🧩 Technology Used

- **Python 3.x**
- **Natural Language Processing** (NLP) with basic keyword extraction
- Libraries:
  - pdfminer.six
  - python-docx
  - pandas
  - streamlit

*(Optional Advanced)*  
- spaCy (for better NLP matching with lemmatization, optional extension)

---

## 📂 Project Structure
AutomatedResumeScanner/
│
├── main.py # Command-line batch scanner
├── parser.py # Resume parsing logic (PDF/DOCX)
├── matcher.py # Keyword matching and scoring
├── exporter.py # CSV exporting
├── app.py # Streamlit web interface
├── requirements.txt # List of required libraries
├── README.md # Project documentation
├── job_description.txt # Example Job Description text
└── resumes/ # Folder for resumes to scan

---

## ⚙️ Setup Instructions

1️⃣ Clone the repository or download the folder:

git clone https://github.com/Manu082/AutomatedResumeScanner.git

cd AutomatedResumeScanner


2️⃣ Install dependencies:

pip install -r requirements.txt


3️⃣ (Optional Advanced) Install spaCy model:

python -m spacy download en_core_web_sm


---

## 💻 Usage

### 1️⃣ Command-line batch scanning

- Place your **resumes** in the `resumes/` folder (PDF/DOCX).  
- Write your **job description** in `job_description.txt`.  
- Run:python main.py

✅ Output:

ranked_candidates.csv

Contains filenames and relevance scores.

---

### 2️⃣ Streamlit Web Interface

streamlit run app.py


✅ Features:
- Enter or paste Job Description text.
- Upload up to 50 resumes at once (with limit warning).
- View ranked results in a table.
- Progress bar while scanning.
- Download CSV of results.

---

## 📝 Example Job Description

We are looking for an AI Engineer with experience in Python, Machine Learning, NLP, and Deep Learning. Must be skilled in TensorFlow, PyTorch, spaCy, and NLTK. The role requires designing and deploying AI models and working with large datasets.


---

## 📜 Example Resume (for High Score)

MANAS DIDWANIA
AI Engineer

Summary:
Experienced AI Engineer with strong skills in Python, Machine Learning, and Deep Learning. Developed NLP applications using spaCy and NLTK. Built models in TensorFlow and PyTorch for text classification and large-scale data analysis


---

##  Limitations

- Basic keyword matching by default.
- NLP features can be improved with lemmatization (spaCy/NLTK).
- Processing speed depends on number and size of resumes.

---

##  Future Improvements

- Advanced NLP (lemmatization, synonyms)
- Semantic similarity matching
- Resume entity extraction (Name, Email, Skills)
- Database integration for storing results

---

##  Acknowledgements

- [Streamlit](https://streamlit.io/)
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- [python-docx](https://python-docx.readthedocs.io/)
- [spaCy](https://spacy.io/)

---

## 📌 Author

Manas Didwania  

---

