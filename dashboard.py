# dashboard.py
import streamlit as st
import altair as alt
from data_processing import load_sessions, get_summary_by_topic, get_daily_totals

st.title("📊 Study Productivity Dashboard")

df = load_sessions()

if df.empty:
    st.info("No data yet. Log some study sessions first!")
    st.stop()

st.subheader("Total Time Spent by Topic")
topic_summary = get_summary_by_topic(df)
st.bar_chart(topic_summary)

st.subheader("Study Time Over Time")
daily_summary = get_daily_totals(df)
st.line_chart(daily_summary)

st.subheader("Recent Study Sessions")
st.dataframe(df.sort_values("study_date", ascending=False).head(10))
