# app.py

from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import joblib
import random

app = Flask(__name__)

# Load the trained model
model_data = joblib.load('model.joblib')
model = model_data['model']
features = model_data['features']

# Function to generate random system metrics (simulating live data)
def generate_live_metrics():
    cpu = random.uniform(20, 95)
    mem = random.uniform(30, 90)
    db_conn = random.uniform(10, 150)
    return {'cpu': cpu, 'mem': mem, 'db_conn': db_conn}

# Function to predict if failure is likely soon
def predict_failure(cpu, mem, db_conn):
    df = pd.DataFrame([{
        'cpu_1': cpu,
        'mem_1': mem,
        'db_conn_1': db_conn,
        'db_conn_roll5': db_conn,
        'db_conn_slope': 0,
        'minute_mod': random.randint(0, 59)
    }])
    pred = model.predict(df[features])[0]
    return int(pred)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/metrics')
def metrics():
    data = generate_live_metrics()
    prediction = predict_failure(data['cpu'], data['mem'], data['db_conn'])
    data['failure_predicted'] = prediction
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
