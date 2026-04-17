from utils.parser import extract_text
from utils.nlp import extract_skills
from utils.hf_model import similarity
from database.db import save_history

def run_pipeline(file_path, job_text, email=None):

    print("🔥 PIPELINE STARTED")
    print("EMAIL RECEIVED:", email)

    # STEP 1
    resume_text = extract_text(file_path)

    # STEP 2
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    # STEP 3
    score = similarity(resume_text, job_text)

    # STEP 4
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    print("📊 MATCH SCORE:", score)

    # STEP 5 — FORCE CHECK
    if email is None or email == "":
        print("❌ EMAIL IS EMPTY → SKIPPING SAVE")
    else:
        print("💾 SAVING TO DATABASE...")
        save_history(email, round(score, 2), matched, missing)
        print("✅ SAVED SUCCESSFULLY")

    # STEP 6
    return {
        "match_percentage": round(score, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }