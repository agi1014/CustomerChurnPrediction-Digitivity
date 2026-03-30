import joblib
import json

scaler = joblib.load("models/scaler.pkl")
with open('scaler_params.json', 'w') as f:
    json.dump({
        'mean': [float(x) for x in scaler.mean_],
        'scale': [float(x) for x in scaler.scale_]
    }, f)
