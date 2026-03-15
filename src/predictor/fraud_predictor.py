import pickle
import pandas as pd

model = pickle.load(open("../model/fraud_model.pkl"))

def predict_transaction(transaction):
    df = pd.DataFrame([transaction])
    prediction = model.predict(df)[0]
    if prediction == -1:
        return "FRAUD"
    else:
        return "NORMAL"