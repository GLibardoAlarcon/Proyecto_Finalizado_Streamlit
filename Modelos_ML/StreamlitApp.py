import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('./Modelos_ML/random_forest_regressor.joblib')

# Cargar el dataset principal
df_costos = pd.read_csv('./Data/car_resale_prices_clean.csv', sep=',')

# Cargar el dataset de costos operacionales
df = pd.read_csv('./Data/costo_operacional_vehiculos_clean.csv', sep=',')

# Asegurarnos de que resale_price sea numérico
df_costos['resale_price'] = pd.to_numeric(df_costos['resale_price'], errors='coerce')

# Verificar si hay valores nulos o incorrectos en resale_price
df_costos = df_costos.dropna(subset=['resale_price'])

# Cargar el dataset de costos operacionales
df = pd.read_csv('./Data/costo_operacional_vehiculos_clean.csv', sep=',')

# Calcular umbrales de costos para clasificación
low_cost_threshold = df_costos['resale_price'].quantile(0.33)
high_cost_threshold = df_costos['resale_price'].quantile(0.66)

# Revisa la función de categorización de vehículos
def categorize_vehicle(row):
    if row['fuel_type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['fuel_type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    else:
        return 'Híbrido'
    
# Revisa la función de categorización de vehículos
def categorize_vehicle2(row):
    if row['Fuel_Type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['Fuel_Type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    else:
        return 'Híbrido'

# Aplicar la función al dataframe
df_costos['Vehicle_Type'] = df_costos.apply(categorize_vehicle, axis=1)

# Aplicar la función al dataframe
df['Vehicle_Type'] = df_costos.apply(categorize_vehicle2, axis=1)

# Streamlit App
st.title('Evaluación de Autos')

# Entrada del presupuesto por parte del cliente
presupuesto_cliente = st.number_input('Ingresa tu presupuesto (en dólares):', min_value=0)

# Mostrar autos recomendados dentro del presupuesto
if presupuesto_cliente > 0:
    st.write(f'Autos recomendados dentro de tu presupuesto de ${presupuesto_cliente}:')
    
    # Filtrar los autos dentro del presupuesto
    autos_recomendados = df_costos[df_costos['resale_price'] <= presupuesto_cliente].sort_values(by='resale_price', ascending=False).head(5)
    
    # Si hay autos que cumplen el criterio
    if not autos_recomendados.empty:
        st.write(autos_recomendados[['full_name', 'registered_year', 'fuel_type', 'resale_price', 'Vehicle_Type']].rename(
            columns={
                'full_name': 'Nombre Completo',
                'registered_year': 'Año',
                'fuel_type': 'Tipo de Combustible',
                'resale_price': 'Precio en Dólares',
                'Vehicle_Type': 'Clasificación de Combustible'
            }
        ).round({'Precio en Dólares': 2}))
    else:
        st.write('No se encontraron autos dentro de tu presupuesto.')

# Mostrar detalles del auto seleccionado
st.write('Detalles del auto seleccionado:')
autos_list = df_costos['full_name'].unique()
selected_auto = st.selectbox('Selecciona un auto:', autos_list)

if selected_auto:
    auto_data = df_costos[df_costos['full_name'] == selected_auto]
    st.write(auto_data[['full_name', 'registered_year', 'fuel_type', 'resale_price', 'Vehicle_Type']].rename(
        columns={
            'full_name': 'Nombre Completo',
            'registered_year': 'Año',
            'fuel_type': 'Tipo de Combustible',
            'resale_price': 'Precio en Dólares',
            'Vehicle_Type': 'Clasificación de Combustible'
        }
    ).round({'Precio en Dólares': 2}))
