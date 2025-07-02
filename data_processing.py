# data_processing.py
import sqlite3
import pandas as pd

def load_sessions():
    conn = sqlite3.connect("study.db")
    df = pd.read_sql_query("SELECT * FROM study_sessions", conn)
    conn.close()
    df['study_date'] = pd.to_datetime(df['study_date'])
    return df

def get_summary_by_topic(df):
    return df.groupby("topic")["duration_minutes"].sum().sort_values(ascending=False)

def get_daily_totals(df):
    return df.groupby("study_date")["duration_minutes"].sum()
