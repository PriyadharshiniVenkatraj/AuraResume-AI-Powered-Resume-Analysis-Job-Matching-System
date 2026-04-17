SKILLS_DB = [
    "python", "java", "flask", "react", "sql",
    "machine learning", "deep learning", "nlp", "aws"
]

def extract_skills(text):
    text = text.lower()
    return list({skill for skill in SKILLS_DB if skill in text})