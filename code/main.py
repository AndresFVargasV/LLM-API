from fastapi import FastAPI
from pydantic import BaseModel
import llm
import uvicorn

app = FastAPI()

# Definir el modelo de datos
class Item(BaseModel):
    carrera: str
    temaEstudio: str
    tiempoDisponible: str
    horaInicial_tiempoLibre: str
    horaFinal_tiempoLibre: str

@app.get("/")
async def root():
    return {"message": "The services are running!"}

@app.post("/study-plan")
async def study_plan(item: Item):
    response = llm.response(item.carrera, item.temaEstudio, item.tiempoDisponible, item.horaInicial_tiempoLibre, item.horaFinal_tiempoLibre)
    return {"plan": response}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)