import m2cgen as m2c
import joblib

model = joblib.load('models/xgboost_model.pkl')
if getattr(model, 'base_score', None) is None:
    model.base_score = 0.5
    
code = m2c.export_to_python(model)

with open('model_code.py', 'w') as f:
    f.write(code)

print("Exported model to pure python code successfully!")
