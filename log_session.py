# log_session.py
import streamlit as st
import datetime
from db_utils import create_db, insert_study_session, insert_subject, get_all_subjects

st.title("📚 Study Session Logger")

create_db()

# Section: Add new subject
with st.expander("➕ Add a New Subject"):
    new_subject = st.text_input("Enter a new subject name")
    if st.button("Add Subject"):
        if new_subject.strip():
            insert_subject(new_subject.strip())
            st.success(f"Subject '{new_subject}' added.")
        else:
            st.warning("Please enter a valid subject name.")

# Get subjects dynamically from DB
subjects = get_all_subjects()
if not subjects:
    st.warning("No subjects found. Add at least one subject first.")
    st.stop()

# Section: Log a study session
st.subheader("📝 Log Your Study Session")

with st.form("study_form", clear_on_submit=True):
    topic = st.selectbox("Select a Subject", subjects)
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=480)
    date = st.date_input("Study Date", datetime.date.today())
    notes = st.text_area("Notes (optional)")

    submitted = st.form_submit_button("➕ Log Session")
    if submitted:
        insert_study_session(topic, duration, str(date), notes)
        st.success(f"✅ Logged {duration} mins of {topic} on {date}")
