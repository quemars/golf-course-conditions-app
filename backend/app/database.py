import sqlite3

conn = sqlite3.connect("golf.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course TEXT,
    greens INTEGER,
    fairways INTEGER,
    pace INTEGER,
    notes TEXT
)
""")

conn.commit()