import sqlite3
import os

DB_PATH = "botdata.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            user_id INTEGER,
            reminder TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_reminder(user_id: int, reminder: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO reminders (user_id, reminder) VALUES (?, ?)", (user_id, reminder))
    conn.commit()
    conn.close()

def get_reminders(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT reminder FROM reminders WHERE user_id = ?", (user_id,))
    results = c.fetchall()
    conn.close()
    return [r[0] for r in results]

def delete_reminders(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM reminders WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
