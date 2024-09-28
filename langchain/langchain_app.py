import streamlit as st
import requests
import os
import fitz  # PyMuPDF
from langchain_modulo import generate_response

# Configuramos la interfaz de Streamlit
st.title("Asistente de Uber")

# URL del archivo PDF en GitHub (enlace directo)
pdf_url = "https://raw.githubusercontent.com/David-I-X/ETL-P/tree/main/langchain/respuestas_uber.pdf"

# Ruta temporal para guardar el PDF
pdf_path = "respuestas_uber.pdf"

# Descargar el PDF si no existe
if not os.path.exists(pdf_path):
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        st.success("PDF descargado correctamente.")
    else:
        st.error(f"Error al descargar el PDF. Código de estado: {response.status_code}")

# Comprobar si el PDF existe y se puede abrir
if os.path.exists(pdf_path):
    try:
        # Intentar abrir el PDF para verificar su integridad
        with fitz.open(pdf_path) as pdf_document:
            st.success("PDF abierto correctamente.")
    except Exception as e:
        st.error(f"Error al abrir el PDF: {e}")

# Selección de tipo de usuario
user_type = st.selectbox(
    "Selecciona tu rol:",
    ("Pasajero", "Conductor")
)

# Preguntas predefinidas en función del usuario
if user_type == "Pasajero":
    question_options = [
        "¿Cuál es el impacto ambiental de mis últimos 5 viajes?",
        "¿Hay un vehículo eléctrico disponible cerca de mi ubicación?"
    ]
elif user_type == "Conductor":
    question_options = [
        "¿Cuál es la mejor zona para trabajar hoy con mi auto eléctrico?",
        "¿Cuánto podría ahorrar si reemplazo mi auto actual por un híbrido?"
    ]

# Mostramos las preguntas
question = st.selectbox("Elige una pregunta:", question_options)

# Botón para enviar la pregunta al modelo de LangChain
if st.button("Preguntar"):
    response = generate_response(user_type, question, pdf_path)
    st.write(response)
