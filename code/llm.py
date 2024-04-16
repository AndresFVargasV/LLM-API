from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('..\\.env')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_NEW"))

def response(carrera, temaEstudio, horaInicial_tiempoLibre, horaFinal_tiempoLibre, diasEstudio):

    # Define the hours available for study
    tiempoDisponible = int(diferencia_horas(horaInicial_tiempoLibre, horaFinal_tiempoLibre))

    # Define the user input content
    user_input_content = f"Soy estudiante de {carrera}, quiero aprender {temaEstudio} y tengo {str(tiempoDisponible)} horas disponibles a la semana para estudiar este tema durante los días {diasEstudio}. Mi tiempo libre diario es entre las {horaInicial_tiempoLibre} y {horaFinal_tiempoLibre}. "

    # Send the user input to the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Por favor, crea un plan de estudio semanal para el usuario basado en la información proporcionada. Quiero que me des temas claros para estudiar, recursos como libros, cursos en internet, revistas, etc, y devuelve la respuesta en el siguiente formato JSON: {'carrera': '', 'temaEstudio': '', 'tiempoDisponible': 0, 'horarioLibre': {'horaInicio': '', 'horaFin': ''}, 'planEstudio': [{'dia': '', 'actividades': ['']: 'recursos':['']}]}."},
            {"role": "user", "content": user_input_content}
        ]
    )

    # Extract and decode the JSON content from the response
    return completion.choices[0].message.content



def diferencia_horas(hora_inicio, hora_fin):
    formato = "%H:%M"  # Formato de hora: hora:minuto

    # Convertir las horas de cadena a objetos datetime
    inicio = datetime.strptime(hora_inicio, formato)
    fin = datetime.strptime(hora_fin, formato)
    
    # Calcular la diferencia de tiempo
    diferencia = fin - inicio
    
    # Extraer las horas de la diferencia de tiempo
    horas = diferencia.total_seconds() / 3600  # 3600 segundos en una hora
    
    return horas

