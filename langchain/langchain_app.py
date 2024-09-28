import streamlit as st
from langchain_modulo import generate_response

# Configuramos la interfaz de Streamlit
st.title("Asistente de Uber")

# URL del archivo PDF en GitHub
pdf_url = "https://github.com/David-I-X/ETL-P/tree/main/langchain"  # Cambia esto a tu URL

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
if st.button("Hacer pregunta"):
    response = generate_response(user_type, question, pdf_url)
    st.write(response)

