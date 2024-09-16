import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('./Modelos_ML/random_forest_regressor.joblib')

# Cargar el dataset principal
df_costos = pd.read_csv('./Data/car_resale_prices_clean.csv')

# Asegurarse de que 'resale_price' sea numérico y sin valores nulos
df_costos['resale_price'] = pd.to_numeric(df_costos['resale_price'], errors='coerce')
df_costos.dropna(subset=['resale_price'], inplace=True)  # Eliminar filas con precios nulos

# Cargar el dataset de costos operacionales
df = pd.read_csv('./Data/costo_operacional_vehiculos_clean.csv', sep=',')

# Calcular umbrales de costos para clasificación
low_cost_threshold = df_costos['resale_price'].quantile(0.33)
high_cost_threshold = df_costos['resale_price'].quantile(0.66)

# Funciones de categorización de vehículos
def categorize_vehicle(row):
    if row['Fuel_Type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['Fuel_Type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    elif row['Fuel_Type'] == 'Hybrid':
        return 'Híbrido'
    else:
        return 'Otro'

def categorize_vehicle2(row):
    if row['fuel_type'] in ['Diesel', 'Petrol', 'Petrol/LPG']:
        return 'Convencional'
    elif row['fuel_type'] in ['Electricity', 'Electric']:
        return 'Eléctrico'
    elif row['fuel_type'] == 'Hybrid':
        return 'Híbrido'
    else:
        return 'Otro'

# Aplicar categorización a ambos dataframes
df['Vehicle_Type'] = df.apply(categorize_vehicle, axis=1)
df_costos['Vehicle_Type'] = df_costos.apply(categorize_vehicle2, axis=1)

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
        costo_promedio = datos['Fuel_Cost'].mean()
        contaminacion_sonora_promedio = datos['Noise_Level'].mean()
        return round(costo_promedio, 2), round(contaminacion_sonora_promedio, 2)
    return 0, 0

# Streamlit App
st.title('Evaluación de Autos')

# Entrada del presupuesto por parte del cliente
presupuesto_cliente = st.number_input('Ingresa tu presupuesto (en dólares):', min_value=0)

# Mostrar autos recomendados dentro del presupuesto
if presupuesto_cliente > 0:
    st.write(f'Autos recomendados dentro de tu presupuesto de ${presupuesto_cliente}:')

    # Filtrar los autos dentro del presupuesto
    autos_filtrados = df_costos[df_costos['resale_price'] <= presupuesto_cliente]

    # Ordenar y mostrar los 5 primeros
    autos_recomendados = autos_filtrados.sort_values(by='resale_price').head(5)

    # Mostrar los autos recomendados
    if not autos_recomendados.empty:
        st.write(autos_recomendados[['full_name', 'registered_year', 'Vehicle_Type', 'resale_price']].rename(
            columns={
                'full_name': 'Nombre Completo',
                'registered_year': 'Año',
                'Vehicle_Type': 'Tipo de Combustible',
                'resale_price': 'Precio en Dólares'
            }
        ).round({'Precio en Dólares': 2}))
    else:
        st.write('No se encontraron autos dentro de tu presupuesto.')

    # Ahora, mover la selección del auto debajo de las recomendaciones
    st.write('Selecciona un auto para ver más detalles:')
    autos_list = autos_recomendados['full_name'].unique()
    selected_auto = st.selectbox('Selecciona un auto:', autos_list)

    # Mostrar detalles del auto seleccionado
    if selected_auto:
        auto_data = df_costos[df_costos['full_name'] == selected_auto]
        st.write(auto_data[['full_name', 'registered_year', 'fuel_type', 'resale_price']].rename(
            columns={
                'full_name': 'Nombre Completo',
                'registered_year': 'Año',
                'fuel_type': 'Tipo de Combustible',
                'resale_price': 'Precio en Dólares'
            }
        ).round({'Precio en Dólares': 2}))

        # Mostrar si es caro, normal o económico
        categoria_costo = auto_data['Categoria_Costo'].values[0]
        st.write(f"Este auto está clasificado como: **{categoria_costo}**")

        # Calcular el costo operativo y la contaminación sonora
        tipo_combustible = auto_data['fuel_type'].values[0]
        costo_operativo, contaminacion_sonora = calcular_costo_operativo(tipo_combustible)

        st.write(f'Costo operativo estimado por cada 10,000 km para tipo de combustible "{tipo_combustible}": ${costo_operativo}')
        st.write(f'Contaminación sonora promedio para tipo de combustible "{tipo_combustible}": {contaminacion_sonora} Db')

else:
    st.write('Ingresa un presupuesto para ver recomendaciones de autos.')


