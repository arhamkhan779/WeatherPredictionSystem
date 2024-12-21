import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

sk=StandardScaler()

model=joblib.load("artifacts\\training\\model.pkl")
input=joblib.load("artifacts\\data_preprocessing\\input_processor.pkl")

def predict(mint,maxt,wind):
    input_features=[[mint,maxt,wind]]
    # input_features=np.array(input_features)
    X=input.transform(input_features)
    pred=model.predict_proba(X)
    return pred

print(predict(20,5,5))