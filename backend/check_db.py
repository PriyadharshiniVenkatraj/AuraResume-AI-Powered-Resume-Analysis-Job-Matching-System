import sqlite3
import os

DB_PATH = os.path.join("database", "history.db")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("SELECT * FROM history")
rows = c.fetchall()

print("\n📊 ROWS IN DB:\n")

if len(rows) == 0:
    print("❌ No data found")
else:
    for row in rows:
        print(row)

conn.close()