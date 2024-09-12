import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo
model = joblib.load('./Modelos_ML/modelo_rf.joblib')

# Título de la app
st.title("Predicción del Tipo de Vehículo")

# Crear un formulario para los inputs del usuario
fuel_cost = st.number_input("Costo de combustible ($):", min_value=0.0, step=0.1)
electric_cost = st.number_input("Costo eléctrico ($):", min_value=0.0, step=0.1)
noise_level = st.number_input("Nivel de ruido (dB):", min_value=0.0, step=0.1)

# Cuando el usuario hace clic en el botón "Predecir"
if st.button('Predecir'):
    # Crear el dataframe con los inputs del usuario
    user_input = pd.DataFrame([[fuel_cost, electric_cost, noise_level]],
                              columns=['Fuel_Cost', 'Electric_Cost', 'Noise_Level'])

    # Hacer la predicción
    prediction = model.predict(user_input)
    
    # Mostrar el resultado
    st.write(f"El tipo de vehículo predicho es: {prediction[0]}")
