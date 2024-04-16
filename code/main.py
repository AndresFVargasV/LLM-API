from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origines
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

class Item(BaseModel):
    carrera: str
    tema: str
    horaInicial_tiempoLibreL: Optional[str] = None
    horaFinal_tiempoLibreL: Optional[str] = None
    horaInicial_tiempoLibreM: Optional[str] = None
    horaFinal_tiempoLibreM: Optional[str] = None
    horaInicial_tiempoLibreW: Optional[str] = None
    horaFinal_tiempoLibreW: Optional[str] = None
    horaInicial_tiempoLibreJ: Optional[str] = None
    horaFinal_tiempoLibreJ: Optional[str] = None
    horaInicial_tiempoLibreV: Optional[str] = None
    horaFinal_tiempoLibreV: Optional[str] = None
    horaInicial_tiempoLibreS: Optional[str] = None
    horaFinal_tiempoLibreS: Optional[str] = None
    horaInicial_tiempoLibreD: Optional[str] = None
    horaFinal_tiempoLibreD: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "The services are running!"}

@app.post("/study-plan")
async def study_plan(item: Item):
    print(item.carrera)  # Debugging: imprimir la carrera para verificación
    # Aquí podrías llamar a una función de procesamiento y devolver la respuesta
    return {"status": "Success", "data": item.dict()}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
