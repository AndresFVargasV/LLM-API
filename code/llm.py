import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('..\\.env')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def response(carrera, temaEstudio, tiempoDisponible, horaInicial_tiempoLibre, horaFinal_tiempoLibre):
    user_input_content = f"Soy estudiante de {carrera}, quiero aprender {temaEstudio} y tengo {tiempoDisponible} horas disponibles a la semana para estudiar este tema. Mi tiempo libre diario es entre las {horaInicial_tiempoLibre} y {horaFinal_tiempoLibre}."


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Por favor, crea un plan de estudio semanal para el usuario basado en la información proporcionada. Quiero que me des temas claros para estudiar, recursos como libros, cursos en internet, revistas, etc, y devuelve la respuesta en el siguiente formato JSON: {'carrera': '', 'temaEstudio': '', 'tiempoDisponible': 0, 'horarioLibre': {'horaInicio': '', 'horaFin': ''}, 'planEstudio': [{'dia': '', 'actividades': ['']: 'recursos':['']}]}."},
            {"role": "user", "content": user_input_content}
        ]
    )

    # Extract and decode the JSON content from the response
    return completion.choices[0].message.content
    

print(response("Ingeniería de Sistemas", "Aprendizaje Automático", 10, "18:00", "21:00"))
