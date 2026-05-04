import pdfplumber
import docx
import re
from database import save_history
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_resume(resume_text):
    prediction = model.predict([resume_text])[0]
    return prediction

SKILLS_DB = [
    "python", "java", "flask", "react", "sql", "javascript", "html", "css",
    "machine learning", "deep learning", "nlp", "aws", "docker", "kubernetes",
    "django", "c++", "c#", "ruby"
]

# --- 1. Parser ---
def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([p.extract_text() or "" for p in pdf.pages])
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

# --- 2. NLP Extractors ---
def extract_skills(text):
    text = text.lower()
    return list({skill for skill in SKILLS_DB if skill in text})

def extract_email(text):
    email = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    return email.group(0) if email else None

def extract_phone(text):
    phone = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return phone.group(0) if phone else None

def extract_name(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if lines:
        return lines[0][:100]  # Take first line, max 100 chars
    return "Unknown"

# --- 3. ML / Similarity ---
def similarity(resume_text, job_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())

    if len(job_words) == 0:
        return 0.0

    match = len(resume_words.intersection(job_words))
    total = len(job_words)

    score = (match / total) * 100
    return round(score, 2)

# --- 4. Main Pipeline ---
def run_pipeline(file_path, job_text):
    print("🔥 PIPELINE STARTED")
    
    # Extract text
    resume_text = extract_text(file_path)
    
    # Details
    extracted_email = extract_email(resume_text)
    extracted_name = extract_name(resume_text)
    extracted_phone = extract_phone(resume_text)
    
    # Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    
    # Scoring
    score = similarity(resume_text, job_text)
    
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    
    # Save to history
    save_history(extracted_name, extracted_email, extracted_phone, score, matched, missing)
    
    return {
        "match_percentage": round(score, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "extracted_info": {
            "name": extracted_name,
            "email": extracted_email,
            "phone": extracted_phone
        }
    }
