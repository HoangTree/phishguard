# PhishGuard — AI Phishing Detector (Hackathon-ready)

A complete, minimal project that trains a phishing detector and serves it via a Flask API,
with a clean HTML/CSS/JS front-end for demo.

## ✨ Features
- Trainable model (TF‑IDF + Logistic Regression, class_weight balanced)
- Flask API (`/predict`, `/health`) with CORS enabled
- Front-end (vanilla HTML/CSS/JS) that calls the API and shows results
- Sample dataset included (`sample_data.csv`)
- Single-command packaging (zip) ready for submission

## 📦 Requirements (local)
- Python 3.10+
- `pip install -r requirements.txt`

## 🚀 Quick Start
1) **Train the model**
```bash
cd phishguard
pip install -r requirements.txt
python train.py   # produces phishguard_pipeline.joblib
```

2) **Run the API**
```bash
python app.py
# API at http://127.0.0.1:5000
```

3) **Open the Front-end**
Open `frontend/index.html` in your browser (double-click).
- The front-end calls `http://127.0.0.1:5000/predict` by default.
- If you deploy the API elsewhere, change `API_BASE` in `frontend/script.js`.

## 🧪 Test Payloads
Try pasting texts like:
- "Urgent: Your account will be locked. Verify password at http://short.link/reset"
- "Team meeting at 2pm — see you!"

## 🛠️ Customize / Improve
- Replace `sample_data.csv` with your dataset (columns: `text,label` where label ∈ {phishing, legit})
- Tune `TfidfVectorizer` and `LogisticRegression`
- Add URL/domain features (length, suspicious TLDs, presence of IP, `@`, etc.)
- Switch to a transformer model (BERT) when you have more data
- Add explainability (e.g., highlight top TF‑IDF terms)

## 🌐 Deployment Hints
- Use `gunicorn` to serve Flask in production
- Host API on Render/Fly.io/HF Spaces; host front-end on Vercel/Netlify/GitHub Pages
- Set `API_BASE` in `frontend/script.js` to your deployed API URL

## 📁 Project Structure
```
phishguard/
  ├─ app.py                 # Flask API
  ├─ train.py               # Training script
  ├─ requirements.txt
  ├─ sample_data.csv
  └─ frontend/
      ├─ index.html
      ├─ style.css
      └─ script.js
```

Good luck and have fun at your hackathon! 🏆
