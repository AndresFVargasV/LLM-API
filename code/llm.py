from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un asistente de estudio capaz de crear planes de estudio personalizados."},
    {"role": "user", "content": "Soy de Ingeniería de Sistemas, quiero aprender Control de Calidad y tengo 5 horas disponibles a la semana y mi tiempo libre diario está entre las 12:30 M y 1:30 PM. Quiero que me des un plan de estudio detallado con temas, subtemas y recursos disponibles para aprendizajes (Libros, revistas, paginas, etc.). Devuelve esto en formato JSON"}
  ]
)

print(completion.choices[0].message)