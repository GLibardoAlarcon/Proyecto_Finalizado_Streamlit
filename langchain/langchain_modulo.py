import fitz  # PyMuPDF
import requests
from transformers import pipeline

# Cargamos el modelo de lenguaje (puedes elegir uno adecuado)
model_name = "gpt2"  # Cambia esto por el modelo que prefieras
llm = pipeline("text-generation", model=model_name)

def download_pdf(url):
    """Función para descargar un archivo PDF desde una URL."""
    response = requests.get(url)
    if response.status_code == 200:
        with open("respuestas_uber.pdf", "wb") as f:
            f.write(response.content)
        print("PDF descargado correctamente.")
    else:
        print(f"Error al descargar el PDF: {response.status_code}")
    
    # Verifica si el archivo se descargó correctamente
    if os.path.exists("respuestas_uber.pdf"):
        return "respuestas_uber.pdf"
    else:
        raise FileNotFoundError("El archivo PDF no se pudo descargar.")

def read_pdf(file_path):
    """Función para leer el contenido de un archivo PDF."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def search_answer_in_pdf(pdf_content, question):
    """Función para buscar la respuesta en el contenido del PDF."""
    # Aquí puedes ajustar la lógica de búsqueda para que sea más robusta
    if question.lower() in pdf_content.lower():
        start_index = pdf_content.lower().index(question.lower())
        end_index = start_index + 200  # Extraer un fragmento de 200 caracteres
        return pdf_content[start_index:end_index]
    else:
        return "No se encontró una respuesta directa."

def generate_response(user_type, question, pdf_path):
    """Función para generar una respuesta basada en el tipo de usuario y la pregunta."""
    # Leer el contenido del PDF
    pdf_content = read_pdf(pdf_path)
    
    # Buscar respuesta en el contenido del PDF
    answer = search_answer_in_pdf(pdf_content, question)
    
    # Procesar la respuesta con el modelo de lenguaje
    if user_type == 'Pasajero':
        prompt = f"Respuesta a la pregunta del pasajero: {question}. {answer}"
    else:
        prompt = f"Respuesta a la pregunta del conductor: {question}. {answer}"

    # Generar respuesta final usando el modelo
    generated_response = llm(prompt, max_length=200)[0]['generated_text']
    return generated_response

# Ejemplo de uso (esto sería dentro de tu aplicación Streamlit)
if __name__ == "__main__":
    # URL del PDF (asegúrate de que sea un enlace directo)
    pdf_url = "https://raw.githubusercontent.com/David-I-X/ETL-P/tree/main/langchain/respuestas_uber.pdf"
    pdf_path = download_pdf(pdf_url)
    
    user_type = "Pasajero"  # O "Conductor"
    question = "¿Cuál es el impacto ambiental de mis últimos 5 viajes?"
    
    response = generate_response(user_type, question, pdf_path)
    print(response)
