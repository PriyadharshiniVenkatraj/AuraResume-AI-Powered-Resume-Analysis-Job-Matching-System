# AuraResume – AI-Powered Resume Analysis & Job Matching System

## 📌 Overview
AuraResume is an intelligent web application that analyzes resumes and matches them against job descriptions using Natural Language Processing (NLP) techniques.

The system provides a match score, extracts candidate details, identifies matched skills, and highlights missing skills.

---

## 🚀 Features
- Upload resumes in PDF/DOCX format
- Input job descriptions for comparison
- TF-IDF based text vectorization
- Cosine similarity scoring for job matching
- Extract candidate details (Name, Email, Phone)
- Skill extraction and matching
- Missing skill identification
- History tracking using SQLite database
- Clean and modern UI dashboard

---

## 🧠 Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- SQLite
- HTML, CSS, JavaScript

---

## ⚙️ How it Works
1. Resume and job description are uploaded
2. Text is extracted and preprocessed
3. TF-IDF converts text into numerical vectors
4. Cosine similarity calculates match score
5. Skills are extracted and compared
6. Results are displayed with:
   - Match percentage
   - Matched skills
   - Missing skills
   - Candidate details

---

## 💻 Installation & Setup

```bash
git clone https://github.com/PriyadharshiniVenkatraj/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer
pip install -r requirements.txt
python app.py
