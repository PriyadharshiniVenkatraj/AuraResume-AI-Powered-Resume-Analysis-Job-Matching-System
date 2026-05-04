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
        name TEXT,
        email TEXT,
        phone TEXT,
        match_score REAL,
        matched TEXT,
        missing TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(name, email, phone, score, matched, missing):
    print("🧠 SAVE_HISTORY CALLED")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    INSERT INTO history (name, email, phone, match_score, matched, missing)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, phone, score, str(matched), str(missing)))

    conn.commit()
    conn.close()

    print("✅ DATA SAVED SUCCESSFULLY")
    
def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(ix) for ix in rows]
