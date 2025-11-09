# model_training.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


print("🚀 Script started successfully...")
# To get consistent results every time
np.random.seed(42)

# Function to generate fake system metrics (like CPU, memory, database connections)
def generate_series(n_steps=5000):
    time = np.arange(n_steps)
    
    # Simulate system metrics
    cpu = 20 + 10*np.sin(time/50) + np.random.normal(0, 3, n_steps)  # CPU usage %
    mem = 30 + 5*np.sin(time/80) + np.random.normal(0, 2, n_steps)   # Memory usage %
    db_conn = np.random.poisson(20, n_steps).astype(float)            # DB connections
    
    # Introduce random spikes (failures)
    for i in range(100, n_steps, 500):
        spike_len = np.random.randint(5, 50)
        db_conn[i:i+spike_len] += np.linspace(0, np.random.randint(40, 200), spike_len)
    
    # Ensure realistic bounds
    cpu = np.clip(cpu, 0, 100)
    mem = np.clip(mem, 0, 100)
    
    return pd.DataFrame({'cpu': cpu, 'mem': mem, 'db_conn': db_conn})

# Label points where a failure will occur soon
def label_failures(df, lookahead=10, conn_threshold=120):
    labels = []
    for i in range(len(df)):
        window = df['db_conn'].iloc[i+1:i+1+lookahead]
        labels.append(1 if (window > conn_threshold).any() else 0)
    labels += [0] * lookahead  # For last few rows, assume safe
    return labels[:len(df)]

# Create ML-friendly features
def create_features(df):
    df = df.copy()
    df['cpu_1'] = df['cpu']
    df['mem_1'] = df['mem']
    df['db_conn_1'] = df['db_conn']
    df['db_conn_roll5'] = df['db_conn'].rolling(5, min_periods=1).mean()
    df['db_conn_slope'] = df['db_conn'].diff().fillna(0)
    df['minute_mod'] = (np.arange(len(df)) % 60)
    return df.dropna()

# Main training process
def main():
    print("🔧 Generating system data...")
    df = generate_series(5000)
    df.to_csv('metrics_data.csv', index=False)
    
    df = create_features(df)
    df['label'] = label_failures(df, lookahead=10, conn_threshold=120)
    
    features = ['cpu_1','mem_1','db_conn_1','db_conn_roll5','db_conn_slope','minute_mod']
    X = df[features]
    y = df['label']
    
    print("🤖 Training AI model to predict system failures...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print("\n📊 Model Performance:\n")
    print(classification_report(y_test, preds))
    
    joblib.dump({'model': model, 'features': features}, 'model.joblib')
    print("\n✅ Model saved as 'model.joblib' and data saved as 'metrics_data.csv'")

if __name__ == "__main__":
    main()
