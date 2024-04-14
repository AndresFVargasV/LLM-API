import re
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar el cliente de OpenAI con la clave API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Función para extraer datos del prompt del usuario
def extract_user_data(content):
    patterns = {
        "hours": r"(\d+) horas disponibles a la semana",
        "time": r"tiempo libre diario es entre las ([\d:]+ ?[AP]M) y ([\d:]+ ?[AP]M)",
        "subject": r"quiero aprender (\w+)",
        "resources": r"incluya recursos como (.+)"
    }

    data = {}
    for key, pattern in patterns.items():
        found = re.search(pattern, content)
        if found:
            if key == "time":
                data["start_time"] = found.group(1)
                data["end_time"] = found.group(2)
            elif key == "resources":
                resources = found.group(1).split(',')
                data[key] = [resource.strip() for resource in resources]
            else:
                data[key] = found.group(1)
        else:
            data[key] = "Unknown"

    return data

user_input_content = "Soy estudiante de Ingeniería de Sistemas, quiero aprender Control de Calidad y tengo 3 horas disponibles a la semana para estudiar este tema. Mi tiempo libre diario es entre las 5:00 PM y 6:00 PM. Me gustaría recibir un plan de estudio que incluya recursos como libros y sitios web."
user_data = extract_user_data(user_input_content)

# Schedule generation logic (simplified for example)
days_of_week = ["Monday", "Wednesday", "Friday"]
study_sessions = ["Read Chapter 1", "Exercise Set A", "Review and Summary"]
schedule = [{day: f"Study session: {session}"} for day, session in zip(days_of_week, study_sessions)]

# Personalized recommendation
recommendation = f"Start with a general overview of {user_data['subject']}, focusing on key concepts."

# Generate the dynamic JSON response based on user information
json_response_content = {
    "plan": {
        "total_hours": f"{user_data['hours']} per week",
        "daily_free_time": f"{user_data['start_time']} to {user_data['end_time']}",
        "week_schedule": schedule,
        "subjects": [
            {
                "name": user_data['subject'],
                "description": recommendation,
                "resources": user_data['resources']
            }
        ]
    }
}

assistant_message = {
    "role": "assistant",
    "content": json.dumps(json_response_content, indent=4)
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

# Print the model response
print(completion.choices[0].message)
