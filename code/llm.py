import re
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('..\\.env')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_NEW"))

def response(carrera, temaEstudio, tiempoDisponible, horaInicial_tiempoLibre, horaFinal_tiempoLibre):
    user_input_content = f"Soy estudiante de {carrera}, quiero aprender {temaEstudio} y tengo {tiempoDisponible} horas disponibles a la semana para estudiar este tema. Mi tiempo libre diario es entre las {horaInicial_tiempoLibre} y {horaFinal_tiempoLibre}. Me gustaría recibir un plan de estudio que incluya recursos como libros, cursos y sitios web."

    # Schedule generation logic
    days_of_week = ["Monday", "Wednesday", "Friday"]
    study_sessions = ["Read Chapter 1", "Exercise Set A", "Review and Summary"]
    schedule = [{day: f"Study session: {session}"} for day, session in zip(days_of_week, study_sessions)]

    # Personalized recommendation
    recommendation = f"Start with a general overview of {temaEstudio}, focusing on key concepts."

    # Generate the dynamic JSON response based on user information
    json_response_content = {
        "plan": {
            "total_hours": f"{tiempoDisponible} per week",
            "daily_free_time": f"{horaInicial_tiempoLibre} to {horaFinal_tiempoLibre}",
            "week_schedule": schedule,
            "subjects": [
                {
                    "name": temaEstudio,
                    "description": recommendation, 
                    "resources": ["libros", "cursos", "sitios web"]
                }
            ]
        }
    }

    assistant_message = {
        "role": "assistant",
        "content": json.dumps(json_response_content) 
    }

    # Create the chat completion request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Please respond with a structured JSON."},
            {"role": "user", "content": user_input_content},
            assistant_message
        ]
    )

    # Return a compact JSON string without newlines
    return  completion.choices[0].message


