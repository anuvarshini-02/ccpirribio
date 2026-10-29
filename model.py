"""Synthetic demonstration of soil-moisture regression; not a field-validated model."""
import random
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split

MODEL_PATH=Path(__file__).resolve().parent.parent/'models'/'synthetic_irrigation_model.joblib'
FEATURES=['microbial_activity_index','soil_temperature_c','humidity_pct','rainfall_mm','previous_moisture_pct']

def generate(n=1200,seed=42):
    rng=random.Random(seed); X=[];y=[]
    for _ in range(n):
        micro=rng.uniform(0,100);temp=rng.uniform(15,42);humid=rng.uniform(20,95)
        rain=rng.uniform(0,25);prev=rng.uniform(10,80)
        # Illustrative simulated relationship, not an agronomic equation
        moisture=max(0,min(100,0.64*prev+0.13*humid+0.55*rain-0.36*(temp-25)+0.025*micro+rng.gauss(0,2.5)))
        X.append([micro,temp,humid,rain,prev]);y.append(moisture)
    return X,y

def train(seed=42):
    X,y=generate(seed=seed)
    xtr,xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=seed)
    model=RandomForestRegressor(n_estimators=120,random_state=seed,min_samples_leaf=2)
    model.fit(xtr,ytr)
    preds=model.predict(xte)
    MODEL_PATH.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,MODEL_PATH)
    return {'MAE':mean_absolute_error(yte,preds),'R2':r2_score(yte,preds)}

def get_model():
    if not MODEL_PATH.exists():train()
    return joblib.load(MODEL_PATH)

def recommendation(predicted_moisture:float,low=35,high=60):
    if not 0<=predicted_moisture<=100:raise ValueError('Moisture must be between 0 and 100.')
    if predicted_moisture < low:return 'Consider irrigation (simulation only)'
    if predicted_moisture > high:return 'Avoid additional irrigation (simulation only)'
    return 'Monitor soil moisture (simulation only)'

if __name__=='__main__':print('Synthetic holdout performance ONLY:',train())
