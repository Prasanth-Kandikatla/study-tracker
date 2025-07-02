# 📚 StudyTracker

A simple and effective application to **log**, **store**, and **analyze your study sessions** using Python, SQLite, and pandas. Optionally, visualize your progress with a Streamlit dashboard. I will be adding more features. 

Pull requests are welcome! Whether it's a bug fix, feature, or dashboard enhancement — feel free to contribute.

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
## ✅ Running The App
### 1. Streamlit Log Session Form
Use this to submit new study entries via a user-friendly UI:
```bash
streamlit run streamlit_log_session.py
```
#### You’ll be able to enter:

  Topic,
  Duration,
  Date,
  Notes

Automatically saves to study.db.

### 2. Streamlit Dashboard
View your study patterns
```bash
streamlit run dashboard.py
```
#### It will show:
Total study time per topic (bar chart)

Daily study duration over time (line chart)

### 3. Export the data
You can export the data by downloading the "Study Sessions" table for your review.


 
