# 📚 StudyTracker

A simple and effective application to **log**, **store**, and **analyze your study sessions** using Python, SQLite, and pandas. Optionally, visualize your progress with a Streamlit dashboard.

---

## 🚀 Features

- 📅 Log study sessions with topic, duration, date, and notes
- 🗃️ Store session data in a local SQLite database
- 📊 Analyze total study time by topic and by day
- 📈 Extendable with Streamlit for interactive dashboards

---

## 🛠️ Project Structure

study-tracker/

├── venv/ # Virtual environment

├── db_utils.py # SQLite setup and insertion logic

├── data_processing.py # Data loading and summary functions

├── log_session.py # Script to add new study sessions

├── study.db # SQLite database file (auto-created)

├── requirements.txt # Python dependencies

└── README.md # You're here!



---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Prasanth-Kandikatla/study-tracker.git
cd study-tracker
```

### 2. Create python virtual environment
```bash
python -m venv venv
```

### 3. Activate the environment
#### Windows
```bash
venv\Scripts\activate
```
#### macOS/Linux
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
