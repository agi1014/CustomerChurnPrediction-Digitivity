from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(title="Customer Churn Prediction API")

# Load model and scaler
try:
    scaler = joblib.load('models/scaler.pkl')
    model = joblib.load('models/xgboost_model.pkl')
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    scaler, model = None, None

# Expected order of features based on training
EXPECTED_COLUMNS = [
    'Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 
    'Total Spend', 'Last Interaction', 'Gender_Male', 
    'Subscription Type_Premium', 'Subscription Type_Standard', 
    'Contract Length_Monthly', 'Contract Length_Quarterly'
]

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
    if not model or not scaler:
        raise HTTPException(status_code=500, detail="Model is not loaded.")
        
    try:
        # 1. Transform input JSON into a dictionary
        input_dict = {
            'Age': data.age,
            'Tenure': data.tenure,
            'Usage Frequency': data.usage_frequency,
            'Support Calls': data.support_calls,
            'Payment Delay': data.payment_delay,
            'Total Spend': data.total_spend,
            'Last Interaction': data.last_interaction,
            
            # One-hot encoding logic matching training
            'Gender_Male': 1 if data.gender.lower() == 'male' else 0,
            'Subscription Type_Premium': 1 if data.subscription_type.lower() == 'premium' else 0,
            'Subscription Type_Standard': 1 if data.subscription_type.lower() == 'standard' else 0,
            'Contract Length_Monthly': 1 if data.contract_length.lower() == 'monthly' else 0,
            'Contract Length_Quarterly': 1 if data.contract_length.lower() == 'quarterly' else 0
        }
        
        # 2. Convert to DataFrame to ensure correct column order
        df = pd.DataFrame([input_dict], columns=EXPECTED_COLUMNS)
        
        # Fill any missing with 0 (failsafe)
        df = df.fillna(0)
        
        # 3. Scale features
        X_scaled = scaler.transform(df)
        
        # 4. Predict
        prediction = model.predict(X_scaled)[0]
        probability = model.predict_proba(X_scaled)[0]
        
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
if not os.path.exists('static'):
    os.makedirs('static')
    
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
