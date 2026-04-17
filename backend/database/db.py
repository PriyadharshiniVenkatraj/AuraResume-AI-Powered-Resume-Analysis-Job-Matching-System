import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "history.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        match_score REAL,
        matched TEXT,
        missing TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(email, score, matched, missing):
    print("🧠 SAVE_HISTORY CALLED")
    print("📍 DB PATH:", DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    INSERT INTO history (email, match_score, matched, missing)
    VALUES (?, ?, ?, ?)
    """, (email, score, str(matched), str(missing)))

    conn.commit()
    conn.close()

    print("✅ DATA SAVED SUCCESSFULLY")