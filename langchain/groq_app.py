from groq import Groq
import streamlit as st

# Inicializo el cliente de Groq
client = Groq(api_key="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")

def get_ai_response(messages, max_words=500):
    """Función que hace una llamada a la API de Groq para obtener la respuesta."""
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.5,
        max_tokens=1024
    )


    # Accedo a la respuesta del modelo ajustado al formato que devuelve la API)
    try:
        # Si 'choices' es una lista, intentamos acceder al primer mensaje
        response = completion.choices[0].message.content
    except AttributeError:
        # Si el formato es diferente, revisamos la estructura con un bloque de except
        response = "Error al procesar la respuesta, formato inesperado."

    # Limito la respuesta a 'max_words' palabras
    words = response.split()  # Divide la respuesta en una lista de palabras
    if len(words) > max_words:
        response = ' '.join(words[:max_words]) + "..."  # Limita y añade "..." al final

    return response

def generate_response(user_type, question, use_ai=False):
    """
    Genera respuestas predefinidas si `use_ai` es False.
    Si `use_ai` es True, llama a la API de Groq para generar una respuesta dinámica.
    """
    if not use_ai:
        # Respuestas predefinidas
        if user_type == "Pasajero":
            if question == "¿Cuál es el impacto ambiental de mis últimos 5 viajes?":
                return "Gracias por tu consulta. Para evaluar el impacto ambiental de tus últimos cinco viajes, consideramos varios factores, incluyendo la distancia recorrida y el tipo de vehículo utilizado. En general, los viajes en vehículos eléctricos o híbridos tienen un menor impacto en términos de emisiones de carbono. Podemos proporcionarte un desglose detallado, que incluya la huella de carbono estimada de cada viaje, así como sugerencias para minimizar tu impacto ambiental en futuros desplazamientos. Por lo tanto el impacto ambiental de tus últimos 5 viajes ha sido de 20 kg de CO2 emitidos."
            elif question == "¿Hay un vehículo eléctrico disponible cerca de mi ubicación?":
                return "Sí, hay un vehículo eléctrico a 5 cuadras de tu ubicación. Aún así estamos trabajando para aumentar la disponibilidad de vehículos eléctricos en nuestra plataforma. Para saber si hay un vehículo eléctrico cerca de ti, puedes consultar la app de Uber, donde podrás ver las opciones disponibles en tu área. Si no hay vehículos eléctricos disponibles en este momento, te recomendamos estar atento a futuras actualizaciones, ya que seguimos ampliando nuestra flota de opciones sostenibles."
        
        elif user_type == "Conductor":
            if question == "¿Cuál es la mejor zona para trabajar hoy con mi auto eléctrico?":
                return "La mejor zona para trabajar hoy es el centro de la ciudad, donde hay más demanda para autos eléctricos. Para maximizar tus ingresos con un auto eléctrico, te sugerimos que trabajes en zonas de alta demanda, especialmente aquellas donde los pasajeros suelen buscar opciones sostenibles. Te recomendamos áreas cercanas a centros comerciales, estaciones de transporte público y eventos locales. Además, puedes usar la función de 'demanda en tiempo real' en la app de Uber para identificar las zonas más activas durante el día."
            elif question == "¿Cuánto podría ahorrar si reemplazo mi auto actual por un híbrido?":
                return "Reemplazar tu vehículo actual por un auto híbrido puede resultar en un ahorro significativo en combustible y mantenimiento. En promedio, los autos híbridos son más eficientes en combustible que los vehículos de gasolina tradicionales. Además, muchos gobiernos ofrecen incentivos fiscales y subsidios para conductores de vehículos híbridos, lo que podría aumentar aún más tus ahorros. Para una estimación más precisa, podemos revisar tu consumo actual de combustible y los costos operativos de ambos tipos de vehículos. En resumen, podrías ahorrar hasta un 30% en combustible si cambias a un auto híbrido."
        
        return "Estamos trabajando para brindarte una respuesta a tu pregunta."
    
    else:
        # Lógica para llamada a la IA (Groq)
        messages = [{"role": "system", "content": f"Eres un asistente para un {user_type} de Uber."}]
        
        # Añadir el historial de conversación al mensaje
        for message in st.session_state['messages']:
            messages.append({"role": "user", "content": message['user']})
            messages.append({"role": "assistant", "content": message['response']})

        # Agregar la pregunta actual del usuario
        messages.append({"role": "user", "content": question})

        return get_ai_response(messages)

def chat():
    st.title("Asistente para Uber")
    st.write("¡Bienvenido al asistente virtual by Arcope!")

    # Inicializo el historial de mensajes en el estado de la sesión si no existe
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

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

    # Mostra preguntas basadas en el rol seleccionado
    question = st.selectbox("Elige una pregunta:", question_options)

    # Campo para pregunta personalizada
    custom_question = st.text_input("O escribe una pregunta nueva:")
    
    # Selección para usar la IA de Groq (solo activarlo cuando sea necesario)
    use_ai = st.checkbox("Usar IA para generar la respuesta", value=False)

    # Botón para enviar la pregunta
    if st.button("Preguntar"):
        # Usa la pregunta personalizada si está llena, de lo contrario, usar la seleccionada
        selected_question = custom_question if custom_question else question
        response = generate_response(user_type, selected_question, use_ai)

        # Agrega la pregunta y respuesta al estado de la sesión
        st.session_state['messages'].append({"user": selected_question, "response": response})

        # Muestra la respuesta
        st.write(response)

    # Muestra el historial de preguntas y respuestas
    st.write("#### Historial de la conversación:")
    for message in st.session_state['messages']:
        st.write(f"**Vos:** {message['user']}")
        st.write(f"**Asistente:** {message['response']}")

if __name__ == "__main__":
    chat()