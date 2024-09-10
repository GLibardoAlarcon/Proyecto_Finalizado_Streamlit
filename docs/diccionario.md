# Diccionario de Datos

- [**air_quality_cleaned.parquet**](#air_quality_cleaned.parquet) 

- [**Calidad_aireL.parquet**](#Calidad_aireL.parquet)

- [**costo_operacional_vehiculos_clean.csv**](#costo_operacional_vehiculos_clean.csv)

- [**datos_geograficos_limpios.parquet**](#datos_geograficos_limpios.parquet)

- [**datos_meteorologicos_limpios.parquet**](#datos_meteorologicos_limpios.parquet)

- [**df_eafcs.parquet**](#df_eafcs.parquet)

- [**df_vfed.parquet**](#df_vfed.parquet)

- [**energy_clean.csv**](#energy_clean.csv)

- [**fhv_tripdata.parquet**](#fhv_tripdata.parquet)

- [**green_tripdata.parquet**](#green_tripdata.parquet)

- [**vehicle_counts_cleaned copy.parquet**](#vehicle_counts_cleaned_copy.parquet)

- [**vehicle_counts_cleaned.parquet**](#vehicle_counts_cleaned.parquet)

- [**yellow_tripdata.parquet**](#yellow_tripdata.parquet)


<a id="air_quality_cleaned.parquet"><b>air_quality_cleaned.parquet</b></a>  

- **Name**: Nombre (Object)
- **Measure**: Nedida (Object)
- **Geo Place Name**: Nombre de Lugar Geografico (Object)
- **Time Period**: Período de Tiempo (Object)
- **Data Value**: Valor de Data (Float)
- **Year**: Año (Datetime)


<a id="Calidad_aireL.parquet"><b>Calidad_aireL.parquet</b></a>

- **indicator_id**: Indicador de Id (Integer)
- **name**: nombre (Object)
- **measure**: medida (Object)
- **geo_type_name**: nombre de tipo geográfico (Object)
- **geo_join_id**: id de geo join (Integer)
- **data_value**: Valor de dato (Float)
- **geo_place_name**: nombre de ubicacion geográfica (Object)
- **measure_info**: Informacion de Medida (Object)
- **time_period**: Perdíodo de tiempo (Object)
- **unique_id**: Id unico (Integer)
- **Date**: Fecha (Object) 
- **Year**: Año (Integer)

<a id="costo_operacional_vehiculos_clean.csv"><b>costo_operacional_vehiculos_clean.csv</b></a>

- **Manuf**: Fabricante del vehículo: Nombre de la compañía que produce el vehículo. (Object)
- **Model**: Modelo del vehículo: Identificación del modelo específico del vehículo. (Object)
- **Desc**: Descripción del vehículo: Información adicional o características específicas del vehículo. (Object)
- **Fuel_Type**: Tipo de combustible: Clasificación del tipo de energía utilizada por el vehículo (por ejemplo, Diesel, Electricidad). (Object)
- **Fuel_Cost**: Costo de combustible (en GBP): Costo del combustible convencional para operar el vehículo, en libras esterlinas.(Float)
- **Electric_Cost**: Costo eléctrico (en GBP): Costo de la electricidad para operar el vehículo, en libras esterlinas. (Float)
- **Total_Cost**: Costo total (en GBP): Suma de los costos de combustible y eléctrico, en libras esterlinas. (Float)
- **Noise_Level** Nivel de ruido (en dB): Nivel de ruido producido por el vehículo, medido en decibelios. (Float)

<a id="datos_geograficos_limpios.parquet"><b>datos_geograficos_limpios.parquet</b></a>

- **latitude**: latitud (Float)
- **longitude**: longitud (Float)
- **elevation**: elevación (Float)
- **utc_offset_seconds**: utc segundos (Integer)
- **timezone**: zona de tiempo (Object)
- **timezone_abbreviation**: zona de tiempo abreviada (Object)

<a id="datos_meteorologicos_limpios.parquet"><b>datos_meteorologicos_limpios.parquet</b></a>

- **Time**: Hora  (Datetime)
- **Temperature_2m (°C)**: Temperatura GRadis Centigrados (Object)
- **rain (mm)**: Lluvia en mm (Object)
- **is_day ()**: Es de día (Object)

<a id="df_eafcs.parquet"><b>df_eafcs.parquet</b></a>

- **Fuel Type Code**: Código de tipo de Combustible  (Object)
- **Station Name**: Nombre de Estación (Object)
- **Street Address**: Dirección (Object)
- **City**: Ciudad (Object)
- **State**: Estado (Object)
- **Latitude**: Latitud (Float)
- **Longitude**: Longitud (Float)


<a id="df_vfed.parquet"><b>df_vfed.parquet</b></a>

- **Year**: Año de registro (Integer)
- **Manufacturer**: Productor Auto (Object)
- **Model**: Modelo Auto (Object)
- **Miles per gallon (mpg)**: Millas por galón para Eléctricos y a Gas este numero es equivalente millas per galón (Float)
- **CO2 (g p/mile)**: CO2 por milla -1 si no existe la informacion (Float)
- **FuelCost**: Costo de Combustible (Float)   
- **FuelCostA**: Costo de Combustible Alternativo (Float)  
- **Fuel**: Combustible (Object)
- **Category**: Categoria Auto (Object)  
- **AlternativeFuel**: Combustible Alternativo (Object)

<a id="energy_clean.csv"><b>energy_clean.csv</b></a>

- **Country**: País (Object)
- **Energy_type**: Tipo de Energía (Object)
- **Year**: Año (Integer)
- **Energy_consumption**: Consumo de Energía (Float)
- **CO2_emission**: Emisión de CO2 (Float)

<a id="fhv_tripdata.parquet"><b>fhv_tripdata.parquet</b></a>

### FHV (For-Hire Vehicles)
- **dispatching_base_num**: Número base de la empresa de despacho (String)
- **pickup_datetime**: Fecha y hora en que se recogió al pasajero (Datetime)
- **dropoff_datetime**: Fecha y hora en que se dejó al pasajero (Datetime)
- **PUlocationID**: ID de la ubicación donde se recogió al pasajero (Integer)
- **DOlocationID**: ID de la ubicación donde se dejó al pasajero (Integer)
- **SR_Flag**: Indicador de Shared Ride (0: no compartido, 1: compartido) (Integer)
- **Affiliated_base_number**: Numero de Licencia de Base que despacha el viaje (Category)
- **trip_duration**: Duración del viaje en minutos (Float)
- **day_of_week**: Día de la semana en que se realizó el viaje (String)
- **duration_binned**: Intervalo de duración de viaje (Object)
- **hour_of_day**: Hora del día en que comenzó el viaje (Integer)

<a id="green_tripdata.parquet"><b>green_tripdata.parquet</b></a>

### Green Trips
- **VendorID**: Identificación del proveedor (Integer)
- **pickup_datetime**: Fecha y hora en que se recogió al pasajero (Datetime)
- **dropoff_datetime**: Fecha y hora en que se dejó al pasajero (Datetime)
- **store_and_fwd_flag**: Si el viaje se almacenó antes de ser enviado al servidor ('Y' o 'N') (String)
- **RatecodeID**: Código de tarifa utilizado (Float)
- **PULocationID**: ID de la ubicación donde se recogió al pasajero (Integer)
- **DOLocationID**: ID de la ubicación donde se dejó al pasajero (Integer)
- **passenger_count**: Número de pasajeros en el viaje (Float)
- **trip_distance**: Distancia total del viaje en millas (Float)
- **fare_amount**: Importe de la tarifa del viaje (Float)
- **extra**: Cargos adicionales (Float)
- **mta_tax**: Impuesto de la MTA (Float)
- **tip_amount**: Monto de la propina (Float)
- **tolls_amount**: Cantidad de peajes (Float)
- **improvement_surcharge**: Recargo por mejoras (Float)
- **total_amount**: Importe total del viaje (Float)
- **payment_type**: Método de pago utilizado (Integer)
- **trip_type**: Tipo de viaje (1: recorrido estándar, 2: viaje compartido) (Float)
- **congestion_surcharge**: Recargo por congestión (Float)
- **trip_duration**: Duración del viaje en minutos (Float)
- **day_of_week**: Día de la semana en que se realizó el viaje (String)
- **duration_binned**: Categoría de la duración del viaje (String)
- **hour_of_day**: Hora del día en que comenzó el viaje (Integer)

<a id="vehicle_counts_cleaned_copy.parquet"><b>vehicle_counts_cleaned copy.parquet</b></a>

- **Roadway Name**: Nombre de Calle (Object) 
- **Veh Class Type**: Tipo de Clase de Vehiculo (Object)
- **Date**: Fecha (Datetime)


<a id="vehicle_counts_cleaned.parquet"><b>vehicle_counts_cleaned.parquet</b></a>

- **Roadway Name**: Nombre de Calle (Object) 
- **Veh Class Type**: Tipo de Clase de Vehiculo (Object)
- **Date**: Fecha (Datetime)

<a id="yellow_tripdata.parquet"><b>yellow_tripdata.parquet</b></a>

### Yellow Trips
- **VendorID**: Identificación del proveedor (Integer)
- **pickup_datetime**: Fecha y hora en que se recogió al pasajero (Datetime)
- **dropoff_datetime**: Fecha y hora en que se dejó al pasajero (Datetime)
- **passenger_count**: Número de pasajeros en el viaje (Float)
- **trip_distance**: Distancia total del viaje en millas (Float)
- **RatecodeID**: Código de tarifa utilizado (Float)
- **store_and_fwd_flag**: Si el viaje se almacenó antes de ser enviado al servidor ('Y' o 'N') (String)
- **PULocationID**: ID de la ubicación donde se recogió al pasajero (Integer)
- **DOLocationID**: ID de la ubicación donde se dejó al pasajero (Integer)
- **payment_type**: Método de pago utilizado (1: crédito, 2: efectivo, etc.) (Integer)
- **fare_amount**: Importe de la tarifa del viaje (Float)
- **extra**: Cargos adicionales (Float)
- **mta_tax**: Impuesto de la MTA (Metropolitan Transportation Authority) (Float)
- **tip_amount**: Monto de la propina (Float)
- **tolls_amount**: Cantidad de peajes (Float)
- **improvement_surcharge**: Recargo por mejoras (Float)
- **total_amount**: Importe total del viaje (Float)
- **congestion_surcharge**: Recargo por congestión (Float)
- **Airport_fee**: Cargos por aeropuertos (Float)
- **trip_duration**: Duración del viaje en minutos (Float)
- **day_of_week**: Día de la semana en que se realizó el viaje (String)
- **duration_binned**: Categoría de la duración del viaje (String)
- **hour_of_day**: Hora del día en que comenzó el viaje (Integer)
- **fare_binned**: Categoría del costo del viaje (String)