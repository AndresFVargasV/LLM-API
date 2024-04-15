import requests
import json

# Define the data to be sent in the POST request
data = {
    "carrera": "Ingeniería Informática",
    "temaEstudio": "Aprendizaje Automático",
    "tiempoDisponible": "10",
    "horaInicial_tiempoLibre": "18:00",
    "horaFinal_tiempoLibre": "20:00"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Make the POST request
response = requests.post("http://localhost:8000/study-plan", data=json_data, headers={"Content-Type": "application/json"})

# Check if the response was successful
if response.status_code == 200:
    # Assuming the server returns JSON
    print("Response from server:")
    try:
        print(response.text)  # Print formatted JSON
    except json.JSONDecodeError:
        print("Failed to decode JSON from response.")
else:
    print(f"Failed to receive valid response. Status code: {response.status_code}")
    print("Response text:", response.text)
