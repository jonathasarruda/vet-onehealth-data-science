from fastapi import FastAPI, Query

app = FastAPI()

predictions = {"Farm A": 0.85, "Farm B": 0.40, "Farm C": 0.65}

@app.get("/predict")
def get_predictions(farm: str = Query(default=None, description="Farm name")):
    if farm:
        if farm in predictions:
            return {farm: predictions[farm]}
        else:
            return {"error": f"Farm '{farm}' not found"}
    return predictions

@app.get("/")
def root():
    return {
        "message_en": "Zoonotic Risk API is running",
        "message_pt": "API de Risco Zoonótico está em execução"
    }
