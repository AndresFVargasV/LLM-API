from fastapi import FastAPI
from pydantic import BaseModel
import llm
import uvicorn

app = FastAPI()

# Definir el modelo de datos
class Item(BaseModel):
    carrera: str
    temaEstudio: str
    horaInicial_tiempoLibreL: str
    horaFinal_tiempoLibreL: str
    horaInicial_tiempoLibreM: str
    horaFinal_tiempoLibreM: str
    horaInicial_tiempoLibreW: str
    horaFinal_tiempoLibreW: str
    horaInicial_tiempoLibreJ: str
    horaFinal_tiempoLibreJ: str
    horaInicial_tiempoLibreV: str
    horaFinal_tiempoLibreV: str
    horaInicial_tiempoLibreS: str
    horaFinal_tiempoLibreS: str
    horaInicial_tiempoLibreD: str
    horaFinal_tiempoLibreD: str


@app.get("/")
async def root():
    return {"message": "The services are running!"}

@app.post("/study-plan")
async def study_plan(item: Item):
    print(item)
    response = llm.response(item.carrera, item.temaEstudio, item.horaInicial_tiempoLibre, item.horaFinal_tiempoLibre, item.diasEstudio)
    return response

if __name__ == "__main__":
    uvicorn.run(app, port=8000)