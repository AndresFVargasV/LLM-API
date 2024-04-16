from fastapi import FastAPI
from pydantic import BaseModel
import llm
import uvicorn

app = FastAPI()

# Definir el modelo de datos
class Item(BaseModel):
    carrera: str
    temaEstudio: str
    horaInicial_tiempoLibre: str
    horaFinal_tiempoLibre: str
    diasEstudio: str

@app.get("/")
async def root():
    return {"message": "The services are running!"}

@app.post("/study-plan")
async def study_plan(item: Item):
    response = llm.response(item.carrera, item.temaEstudio, item.horaInicial_tiempoLibre, item.horaFinal_tiempoLibre, item.diasEstudio)
    return response

if __name__ == "__main__":
    uvicorn.run(app, port=8000)