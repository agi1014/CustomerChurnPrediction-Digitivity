import joblib
import xgboost as xgb

model = joblib.load('models/xgboost_model.pkl')
booster = model.get_booster()
booster.save_model('models/xgboost_native.json')
print("Model converted to xgboost_native.json successfully.")
