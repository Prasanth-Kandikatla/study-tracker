# db_utils.py

import sqlite3


def create_db():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()

    # Study sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            duration_minutes INTEGER,
            study_date TEXT,
            notes TEXT
        )
    """)

    # Subjects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()

def insert_subject(subject_name):
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (name) VALUES (?)", (subject_name,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Ignore if subject already exists
    finally:
        conn.close()

def get_all_subjects():
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM subjects ORDER BY name")
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subjects

def insert_study_session(topic, duration, date, notes):
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO study_sessions (topic, duration_minutes, study_date, notes)
        VALUES (?, ?, ?, ?)
    """, (topic, duration, date, notes))
    conn.commit()
    conn.close()