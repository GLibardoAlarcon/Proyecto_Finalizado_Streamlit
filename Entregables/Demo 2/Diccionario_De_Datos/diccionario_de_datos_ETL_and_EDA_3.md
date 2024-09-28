
### 1. Yellow Trips
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

### 2. Green Trips
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

### 3. FHV (For-Hire Vehicles)
- **dispatching_base_num**: Número base de la empresa de despacho (String)
- **pickup_datetime**: Fecha y hora en que se recogió al pasajero (Datetime)
- **dropoff_datetime**: Fecha y hora en que se dejó al pasajero (Datetime)
- **SR_Flag**: Indicador de Shared Ride (0: no compartido, 1: compartido) (Integer)
- **PUlocationID**: ID de la ubicación donde se recogió al pasajero (Integer)
- **DOlocationID**: ID de la ubicación donde se dejó al pasajero (Integer)
- **trip_duration**: Duración del viaje en minutos (Float)
- **day_of_week**: Día de la semana en que se realizó el viaje (String)
- **hour_of_day**: Hora del día en que comenzó el viaje (Integer)

Este diccionario de datos proporciona una descripción clara de cada campo para cada dataset.