import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('./Modelos_ML/random_forest_regressor.joblib')

# Cargar el dataset principal
df_costos = pd.read_csv('./Data/car_resale_prices_clean.csv')

# Cargar el dataset de costos operacionales
df = pd.read_csv('./Data/costo_operacional_vehiculos_clean.csv', sep=',')

# Calcular umbrales de costos para clasificación
low_cost_threshold = df_costos['resale_price'].quantile(0.33)
high_cost_threshold = df_costos['resale_price'].quantile(0.66)

# Función para categorizar los vehículos en df
def categorize_vehicle(row):
    if row['Fuel_Type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['Fuel_Type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    else:
        return 'Híbrido'
    
# Función para categorizar los vehículos en df
def categorize_vehicle2(row):
    if row['fuel_type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['fuel_type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    else:
        return 'Híbrido'

# Aplicar la función al dataframe
df['Vehicle_Type'] = df.apply(categorize_vehicle, axis=1)

# Aplicar la función al dataframe
df['Vehicle_Type'] = df_costos.apply(categorize_vehicle2, axis=1)

# Función para clasificar el costo
def clasificar_costo(total_cost):
    if total_cost <= low_cost_threshold:
        return 'Económico'
    elif total_cost <= high_cost_threshold:
        return 'Normal'
    else:
        return 'Caro'

# Agregar la columna de categoría de costo al dataset de costos
df_costos['Categoria_Costo'] = df_costos['resale_price'].apply(clasificar_costo)

# Función para calcular el costo operativo estimado
def calcular_costo_operativo(tipo_combustible):
    tipo_combustible = tipo_combustible.capitalize()
    if tipo_combustible in df['Fuel_Type'].unique():
        datos = df[df['Fuel_Type'] == tipo_combustible]
        costo_promedio = df['Fuel_Cost'].mean()
        contaminacion_sonora_promedio = df['Noise_Level'].mean()
        return round(costo_promedio, 2), round(contaminacion_sonora_promedio, 2)
    return 0, 0

# Streamlit App
st.title('Evaluación de Autos')

# Selección del tipo de auto
auto_type = st.selectbox('Selecciona el tipo de auto:', ['Convencional', 'Híbrido', 'Eléctrico'])

# Mostrar detalles del auto seleccionado
if not df.empty:
    st.write('Detalles del auto seleccionado:')
    autos_list = df_costos['full_name'].unique()
    selected_auto = st.selectbox('Selecciona un auto:', autos_list)

    if selected_auto:
        auto_data = df_costos[df_costos['full_name'] == selected_auto]
        st.write(auto_data[['full_name', 'registered_year', 'fuel_type', 'resale_price']].rename(
            columns={
                'full_name': 'Nombre Completo',
                'registered_year': 'Año',
                'fuel_type': 'Tipo de Combustible',
                'resale_price': 'Precio en Dolares'
            }
        ).round({'Precio en Dolares': 2}))

        # Obtener el tipo de combustible del auto seleccionado
        tipo_combustible = auto_data['fuel_type'].values[0]

        # Calcular el costo operativo y la contaminación sonora
        costo_operativo, contaminacion_sonora = calcular_costo_operativo(tipo_combustible)

        st.write(f'Costo operativo estimado por cada 10,000 km para tipo de combustible "{tipo_combustible}": ${costo_operativo}')
        st.write(f'Contaminación sonora promedio para tipo de combustible "{tipo_combustible}": {contaminacion_sonora} Db')

        # Mostrar la clasificación de costos
        st.write('Clasificación de costos:')
        clasificacion_costo = df[df_costos['Vehicle_Type'] == tipo_combustible]['Categoria_Costo'].value_counts()
        st.write(clasificacion_costo)
else:
    st.write('No hay autos disponibles para el tipo seleccionado.')

