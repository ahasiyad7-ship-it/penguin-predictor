# 🐧 Penguin Species Predictor - 5 Species

Predict the species of a penguin from its body measurements with photo and accuracy.

### 🔴 Live Demo
**Try the app here:** https://ahasiyad7-ship-it-penguin-predictor-app-atftwx.streamlit.app/

### 💻 GitHub Code
https://github.com/ahasiyad7-ship-it/penguin-predictor

---

## ✨ Features
- Predicts 5 Penguin Species: Adelie, Chinstrap, Gentoo, Macaroni, Emperor
- Interactive sliders for Bill Length, Bill Depth, Flipper Length, Body Mass
- Shows penguin photo for predicted species
- Shows prediction confidence
- Clean and simple Streamlit UI

## 🛠️ Tech Stack
- **Python**
- **Streamlit** - For web app
- **Scikit-learn** - For Machine Learning model
- **Pandas, NumPy** - For data handling

## 🧠 How It Works
1. User enters penguin measurements using sliders
2. Trained ML model (Random Forest) predicts the species
3. App displays species name, photo, and confidence score

## 🚀 Run Locally
```bash
git clone https://github.com/ahasiyad7-ship-it/penguin-predictor.git
cd penguin-predictor
pip install -r requirements.txt
streamlit run app.py
