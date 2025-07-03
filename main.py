from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    temperature: float
    humidity: float
    
@app.post("/predict")
def predict(data: InputData):
    if data.temperature > 20 and data.humidity >70:
        result = "Poor air quality"
    else:
        result = "Good air quality"
    return {"result": result}