# 🧠 Predictive System Monitoring Dashboard  
### 🚀 AI-Powered System Health Prediction & Visualization  

**🌐 Live Demo:**  
🔗 [https://predictive-system-monitor.onrender.com](https://predictive-system-monitor.onrender.com)

---

## 📖 Overview  
The **Predictive System Monitoring Dashboard** is an AI-driven web application that predicts potential system failures **before they happen**.  
It continuously monitors simulated **CPU usage**, **memory consumption**, and **database connections**, displaying real-time data through an interactive dashboard.  

This project demonstrates **machine learning**, **real-time visualization**, and **Flask-based web integration** — ideal for showcasing full-stack AI skills.

---

## ✨ Features  
✅ Real-time system metrics visualization  
✅ AI model predicts upcoming system failures  
✅ Beautiful Chart.js dashboard  
✅ Dynamic status indicator – 🟢 *Healthy* or ⚠️ *Failure Predicted*  
✅ Responsive and visually appealing UI  
✅ Fully deployed and live on Render 🌐  

---

## 🛠️ Tech Stack  

| Area | Technologies Used |
|------|--------------------|
| **Frontend** | HTML, CSS, Chart.js |
| **Backend** | Flask (Python) |
| **Machine Learning** | scikit-learn, pandas, numpy |
| **Deployment** | Render (Cloud Hosting) |
| **Visualization** | Chart.js |

---

## ⚙️ How It Works  

1. **Data Simulation** 🧩  
   - The system generates sample CPU, memory, and DB metrics.  

2. **AI Model Training** 🤖  
   - `model_training.py` trains a model to detect failure patterns.  
   - The trained model is saved as `model.joblib`.  

3. **Prediction & Monitoring** 📊  
   - `app.py` loads the model and updates metrics live.  
   - The dashboard (`dashboard.html`) refreshes automatically every few seconds.  

4. **Deployment** ☁️  
   - Hosted using **Render**, accessible to anyone through a live URL.  

---

## 🧱 Project Structure  

