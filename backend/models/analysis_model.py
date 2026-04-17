from database.db import db

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_percentage = db.Column(db.Float)
    matched_skills = db.Column(db.Text)
    missing_skills = db.Column(db.Text)