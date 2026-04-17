import sqlite3

conn = sqlite3.connect("database/history.db")
c = conn.cursor()

c.execute("SELECT * FROM history")
rows = c.fetchall()

print("\n📊 DB CONTENT:\n")

if len(rows) == 0:
    print("❌ No data found")
else:
    for row in rows:
        print(row)

conn.close()