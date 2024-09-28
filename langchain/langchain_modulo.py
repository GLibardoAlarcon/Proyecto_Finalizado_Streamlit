import fitz  # PyMuPDF
import requests
from transformers import pipeline

# Cargamos el modelo de lenguaje (puedes elegir uno adecuado)
model_name = "gpt2"  # Cambia esto por el modelo que prefieras
llm = pipeline("text-generation", model=model_name)

def download_pdf(url):
    """Función para descargar un archivo PDF desde una URL."""
    response = requests.get(url)
    with open("respuestas_uber.pdf", "wb") as f:
        f.write(response.content)
    return "respuestas_uber.pdf"

def read_pdf(file_path):
    """Función para leer el contenido de un archivo PDF."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def search_answer_in_pdf(pdf_content, question):
    """Función para buscar la respuesta en el contenido del PDF."""
    if question.lower() in pdf_content.lower():
        start_index = pdf_content.lower().index(question.lower())
        end_index = start_index + 200  # Extraer un fragmento de 200 caracteres
        return pdf_content[start_index:end_index]
    else:
        return "No se encontró una respuesta directa en el PDF."

def generate_response(user_type, question, pdf_url):
    """Genera una respuesta basada en el tipo de usuario y la pregunta."""
    pdf_file = download_pdf(pdf_url)
    pdf_content = read_pdf(pdf_file)

    if user_type == "pasajero":
        prompt = f"Soy un asistente de Uber para pasajeros. Respondo a la pregunta seleccionada: {question}"
    elif user_type == "conductor":
        prompt = f"Soy un asistente de Uber para conductores. Respondo a la pregunta seleccionada: {question}"
    
    # Buscamos la respuesta en el contenido del PDF
    pdf_answer = search_answer_in_pdf(pdf_content, question)

    # Si no se encontró una respuesta en el PDF, usamos el modelo LLM
    if pdf_answer == "Momentaneamente no se encontró una respuesta acorde.":
        response = llm(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
        return response
    else:
        return pdf_answer
