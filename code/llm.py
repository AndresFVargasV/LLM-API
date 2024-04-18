from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('..\\.env')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_NEW"))

def get_response(carrera, tema, horaInicial_tiempoLibreL, horaFinal_tiempoLibreL, horaInicial_tiempoLibreM, horaFinal_tiempoLibreM, horaInicial_tiempoLibreW, horaFinal_tiempoLibreW, horaInicial_tiempoLibreJ, horaFinal_tiempoLibreJ, horaInicial_tiempoLibreV, horaFinal_tiempoLibreV, horaInicial_tiempoLibreS, horaFinal_tiempoLibreS, horaInicial_tiempoLibreD, horaFinal_tiempoLibreD):



    day_hours = {f"Lunes": {horaInicial_tiempoLibreL, horaFinal_tiempoLibreL}, f"Martes": {horaInicial_tiempoLibreM, horaFinal_tiempoLibreM}, f"Miércoles": {horaInicial_tiempoLibreW, horaFinal_tiempoLibreW}, f"Jueves": {horaInicial_tiempoLibreJ, horaFinal_tiempoLibreJ}, f"Viernes": {horaInicial_tiempoLibreV, horaFinal_tiempoLibreV}, f"Sábado": {horaInicial_tiempoLibreS, horaFinal_tiempoLibreS}, f"Domingo": {horaInicial_tiempoLibreD, horaFinal_tiempoLibreD}}
    
    response = call_api(carrera, tema, day_hours)
    
    if response:
        return response
    else:
        response = "No se pudo obtener una respuesta con el servicio LLM. Por favor, intenta de nuevo."
        return response


def call_api(carrera, tema, day_hours):
    # Define the user input content
    user_input_content = f"Soy estudiante de {carrera}, quiero aprender {tema}, tengo disponible estos días y horas durante la semana {day_hours} para estudiar este tema."

    # Send the user input to the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Por favor, crea un plan de estudio semanal para el usuario basado en la información proporcionada. Que tu respuesta sea totalmente completa. Quiero que me des temas claros para estudiar, recursos como libros, cursos en internet, revistas, etc. También, si algunas de las horas de los días es un valor nulo o no un tiempo suficiente de media hora o mas, no tengas en cuenta esa hora ni ese día. Da una respuesta valida y sin tantas equivocaciones. Finalmente, devuelve la respuesta en el siguiente formato JSON: {'planEstudio': [{'dia': '','hora_inicio_estudio_dia': '','hora_final_estudio_dia': '', 'actividades': ['']: 'recursos':['']}]}. (SOLO EL JSON)"},
            {"role": "user", "content": user_input_content}
        ]
    )
    
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
    
