from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

vehicle_map = {
    "bike": 0,
    "car": 1,
    "van": 2
}

@app.get("/")
def home():
    return {"message": "Fuel Cost API running"}

@app.get("/predict")
def predict(distance: float, vehicle: str, fuel_price: float):

    v = vehicle_map[vehicle]

    base_cost = model.predict(np.array([[distance, v]]))[0]

    # adjust using fuel price
    adjusted_cost = base_cost * (fuel_price / 300)

    weekly_cost = adjusted_cost * 7

    # suggestion
    suggestion = "Looks good"
    if adjusted_cost > 1500:
        suggestion = "Try reducing travel or using a bike to save cost 💡"

    return {
        "daily_cost": round(adjusted_cost, 2),
        "weekly_cost": round(weekly_cost, 2),
        "suggestion": suggestion
    }