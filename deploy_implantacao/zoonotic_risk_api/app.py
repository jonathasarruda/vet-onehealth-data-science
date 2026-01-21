from fastapi import FastAPI

app = FastAPI()

predictions = {"Farm A": 0.85, "Farm B": 0.40, "Farm C": 0.65}

@app.get("/predict")
def get_predictions():
    return predictions
