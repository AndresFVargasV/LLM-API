from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
import llm

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
    respuesta = llm.get_response(item.carrera, item.tema, item.horaInicial_tiempoLibreL, item.horaFinal_tiempoLibreL, 
                             item.horaInicial_tiempoLibreM, item.horaFinal_tiempoLibreM, 
                             item.horaInicial_tiempoLibreW, item.horaFinal_tiempoLibreW, 
                             item.horaInicial_tiempoLibreJ, item.horaFinal_tiempoLibreJ, 
                             item.horaInicial_tiempoLibreV, item.horaFinal_tiempoLibreV, 
                             item.horaInicial_tiempoLibreS, item.horaFinal_tiempoLibreS, 
                             item.horaInicial_tiempoLibreD, item.horaFinal_tiempoLibreD)
    
    print(respuesta)
    
    # Aquí podrías llamar a una función de procesamiento y devolver la respuesta
    return respuesta

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)