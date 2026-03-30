from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import model_code
import os

app = FastAPI(title="Customer Churn Prediction API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Custom Scaler values extracted to avoid loading scikit-learn
SCALER_MEAN = [39.37315349157956, 31.25633574695122, 15.80749355763647, 3.6044366107723578, 12.965721635452962, 631.6162227787459, 14.480867995063878, 0.567681112078978, 0.3372668045876887, 0.3382876016260163, 0.19759001161440184, 0.4004473359465738]
SCALER_SCALE = [12.442355378487592, 17.255707813258432, 8.586231906503338, 3.0702143953875822, 8.258053151045662, 240.80272799709104, 8.596197933037589, 0.4953980894873868, 0.4727768047513526, 0.4731269387935271, 0.3981811132193772, 0.4899890479182832]

class CustomerData(BaseModel):
    age: float
    gender: str
    tenure: float
    usage_frequency: float
    support_calls: float
    payment_delay: float
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: float

@app.post("/predict")
async def predict_churn(data: CustomerData):
    try:
        # 1. Extract features into a raw list in the exact expected order
        features = [
            data.age,
            data.tenure,
            data.usage_frequency,
            data.support_calls,
            data.payment_delay,
            data.total_spend,
            data.last_interaction,
            1.0 if data.gender.lower() == 'male' else 0.0,
            1.0 if data.subscription_type.lower() == 'premium' else 0.0,
            1.0 if data.subscription_type.lower() == 'standard' else 0.0,
            1.0 if data.contract_length.lower() == 'monthly' else 0.0,
            1.0 if data.contract_length.lower() == 'quarterly' else 0.0
        ]
        
        # 2. Scale features manually using standard Python math
        X_scaled = [(f - m) / s for f, m, s in zip(features, SCALER_MEAN, SCALER_SCALE)]
        
        # 3. Predict via pure Python model (Zero dependencies!)
        probability = model_code.score(X_scaled)
        
        prediction = 1 if probability[1] > 0.5 else 0
        
        churn_status = "CHURN" if prediction == 1 else "RETAINED"
        confidence = float(max(probability) * 100)
        
        return {
            "prediction": int(prediction),
            "status": churn_status,
            "confidence": round(confidence, 2)
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Mount static files to serve the frontend UI
static_dir = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_dir):
    try:
        os.makedirs(static_dir)
    except Exception:
        pass
    
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
