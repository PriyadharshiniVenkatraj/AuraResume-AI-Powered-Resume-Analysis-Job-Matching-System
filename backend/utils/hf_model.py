from sklearn.metrics.pairwise import cosine_similarity

def similarity(resume_text, job_text):
    # SIMPLE TEXT-BASED SIMULATION (NO TORCH)
    
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())

    if len(job_words) == 0:
        return 0.0

    match = len(resume_words.intersection(job_words))
    total = len(job_words)

    score = (match / total) * 100
    return round(score, 2)