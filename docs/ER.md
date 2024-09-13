 modelo de entidad-relación (ER), utilizando tablas para detallar las entidades, sus atributos y las relaciones entre ellas. 

### 1. **Entidad: Air Quality Measurement**
| Atributo          | Tipo de dato   | Descripción                                          |
|-------------------|----------------|------------------------------------------------------|
| `indicator_id`     | Integer        | Identificador único del indicador                    |
| `name`             | Object         | Nombre del indicador                                 |
| `measure`          | Object         | Medida del indicador                                 |
| `geo_join_id`      | Integer        | Identificador del área geográfica                    |
| `geo_place_name`   | Object         | Nombre del barrio                                    |
| `data_value`       | Float          | Valor real del indicador                             |
| `time_period`      | Object         | Período de tiempo al que aplican los datos           |
| `year`             | Integer        | Año en el que se tomaron los datos                   |
| **Relaciones**     |                |                                                      |
| `geo_join_id` → `Geographic Data`   | Relación con la entidad geográfica                   |

---

### 2. **Entidad: Vehicles**
| Atributo         | Tipo de dato   | Descripción                                           |
|------------------|----------------|-------------------------------------------------------|
| `manuf`          | Object         | Fabricante del vehículo                               |
| `model`          | Object         | Modelo del vehículo                                   |
| `fuel_type`      | Object         | Tipo de combustible                                   |
| `fuel_cost`      | Float          | Costo anual del combustible (en GBP)                  |
| `electric_cost`  | Float          | Costo anual eléctrico (en GBP)                        |
| `total_cost`     | Float          | Costo total anual (en GBP)                            |
| `noise_level`    | Float          | Nivel de ruido del vehículo (en dB)                   |
| **Relaciones**   |                |                                                       |
| `model` → `Trips`| Relación con la entidad `Trips` mediante el vehículo usado en el viaje |

---

### 3. **Entidad: Trips (Yellow, Green, FHV)**
| Atributo            | Tipo de dato   | Descripción                                         |
|---------------------|----------------|-----------------------------------------------------|
| `vendor_id`         | Integer        | Identificación del proveedor                        |
| `pickup_datetime`   | Datetime       | Fecha y hora de recogida                            |
| `dropoff_datetime`  | Datetime       | Fecha y hora de entrega                             |
| `passenger_count`   | Float          | Número de pasajeros                                 |
| `trip_distance`     | Float          | Distancia total del viaje                           |
| `total_amount`      | Float          | Importe total del viaje                             |
| `PULocationID`      | Integer        | ID de la ubicación de recogida                      |
| `DOLocationID`      | Integer        | ID de la ubicación de entrega                       |
| `payment_type`      | Integer        | Método de pago utilizado                            |
| `congestion_surcharge`| Float        | Recargo por congestión                              |
| **Relaciones**      |                |                                                     |
| `PULocationID` → `Geographic Data` | Relación con la ubicación geográfica de recogida     |
| `DOLocationID` → `Geographic Data` | Relación con la ubicación geográfica de entrega      |
| `pickup_datetime` → `Meteorological Data` | Relación con el clima durante el viaje              |

---

### 4. **Entidad: Geographic Data**
| Atributo              | Tipo de dato   | Descripción                                          |
|-----------------------|----------------|------------------------------------------------------|
| `geo_join_id`          | Integer        | Identificador geográfico                             |
| `latitude`             | Float          | Latitud                                              |
| `longitude`            | Float          | Longitud                                             |
| `elevation`            | Float          | Elevación                                            |
| `timezone`             | Object         | Zona horaria                                         |
| **Relaciones**         |                |                                                      |
| `geo_join_id` → `Air Quality Measurement` | Relación con mediciones de calidad del aire          |
| `geo_join_id` → `Trips`| Relación con viajes realizados en la ubicación                  |

---

### 5. **Entidad: Meteorological Data**
| Atributo             | Tipo de dato   | Descripción                                          |
|----------------------|----------------|------------------------------------------------------|
| `time`               | Datetime       | Hora                                                 |
| `temperature_2m`     | Float          | Temperatura a 2m de altura                           |
| `rain`               | Float          | Lluvia en mm                                         |
| `is_day`             | Object         | Indica si es de día                                  |
| **Relaciones**       |                |                                                      |
| `time` → `Trips`     | Relación con viajes en función del clima durante el trayecto        |

---

### 6. **Entidad: Fuel Stations**
| Atributo             | Tipo de dato   | Descripción                                          |
|----------------------|----------------|------------------------------------------------------|
| `station_name`       | Object         | Nombre de la estación                                |
| `street_address`     | Object         | Dirección                                            |
| `city`               | Object         | Ciudad                                               |
| `state`              | Object         | Estado                                               |
| `fuel_type_code`     | Object         | Código de tipo de combustible                        |
| **Relaciones**       |                |                                                      |
| `fuel_type_code` → `Vehicles` | Relación con el tipo de combustible de los vehículos    |

---

### 7. **Entidad: Fuel Economy Data**
| Atributo             | Tipo de dato   | Descripción                                          |
|----------------------|----------------|------------------------------------------------------|
| `manufacturer`       | Object         | Productor del vehículo                               |
| `model`              | Object         | Modelo del vehículo                                  |
| `miles_per_gallon`   | Float          | Millas por galón                                     |
| `co2_per_mile`       | Float          | Emisiones de CO2 por milla                           |
| `fuel_cost`          | Float          | Costo de combustible anual                           |
| **Relaciones**       |                |                                                      |
| `model` → `Vehicles` | Relación con datos de vehículos                                    |

---

Este es el informe estructurado del modelo ER. Cada tabla representa una entidad, sus atributos y las relaciones más importantes con otras entidades dentro de la base de datos.

---
---

Para describir de manera clara las relaciones entre las entidades del modelo de entidad-relación (ER) podemos apoyarnos en una explicación escrita detallada que simule la representación gráfica. A continuación, explico cómo las entidades están relacionadas entre sí y cómo fluyen los datos entre ellas.

### Relación 1: **Ubicaciones Geográficas y Viajes (Trips - Geographic Data)**

**Descripción:**
Cada viaje (Trips) tiene una **ubicación de recogida** y una **ubicación de entrega** representada por los campos `PULocationID` y `DOLocationID`. Estas ubicaciones están relacionadas con la entidad **Geographic Data**, que contiene información detallada como latitud, longitud y zona horaria.

**Gráficamente:**
- **Trips.PULocationID** ───► **Geographic Data.geo_join_id** (Relación 1:N)
- **Trips.DOLocationID** ───► **Geographic Data.geo_join_id** (Relación 1:N)

**Explicación:**
Un viaje puede tener solo una ubicación de recogida y una de entrega, pero una ubicación geográfica (un barrio, por ejemplo) puede tener varios viajes asociados, ya sea como punto de inicio o destino. Esta relación es de **uno a muchos**.

---

### Relación 2: **Viajes y Clima (Trips - Meteorological Data)**

**Descripción:**
Los viajes (Trips) están influenciados por las condiciones climáticas en el momento del trayecto. La entidad **Meteorological Data** contiene información como la temperatura, la cantidad de lluvia, y si es de día o de noche, que se registra en el campo `pickup_datetime` en Trips y está relacionado con el campo `time` en la tabla de datos meteorológicos.

**Gráficamente:**
- **Trips.pickup_datetime** ───► **Meteorological Data.time** (Relación 1:1)

**Explicación:**
Un viaje tiene solo un momento de recogida, y este momento puede coincidir con un registro meteorológico. Cada registro meteorológico cubre un único momento, por lo que esta relación es de **uno a uno**.

---

### Relación 3: **Indicadores de Calidad del Aire y Ubicación (Air Quality Measurement - Geographic Data)**

**Descripción:**
Las mediciones de la calidad del aire (Air Quality Measurement) están vinculadas a una ubicación geográfica específica representada por el campo `geo_join_id`. Esta información está relacionada con los datos de ubicación almacenados en la entidad **Geographic Data**.

**Gráficamente:**
- **Air Quality Measurement.geo_join_id** ───► **Geographic Data.geo_join_id** (Relación 1:N)

**Explicación:**
Una medición de calidad del aire está asociada a una única ubicación geográfica, pero una ubicación puede tener múltiples mediciones de calidad del aire en diferentes momentos. Esta relación es de **uno a muchos**.

---

### Relación 4: **Vehículos y Viajes (Vehicles - Trips)**

**Descripción:**
Cada viaje (Trips) está asociado a un vehículo específico, ya sea un taxi amarillo, verde o un vehículo FHV (For-Hire Vehicle). El modelo del vehículo utilizado en cada viaje está registrado en el campo `model`, que está relacionado con la información del vehículo en la entidad **Vehicles**.

**Gráficamente:**
- **Trips.model** ───► **Vehicles.model** (Relación N:1)

**Explicación:**
Muchos viajes pueden estar asociados al mismo modelo de vehículo, pero un viaje específico utiliza un único modelo de vehículo. Esta relación es de **muchos a uno**.

---

### Relación 5: **Vehículos y Estaciones de Combustible (Vehicles - Fuel Stations)**

**Descripción:**
La entidad **Vehicles** también está relacionada con las estaciones de combustible a través del tipo de combustible (`fuel_type`) que utilizan los vehículos. La entidad **Fuel Stations** contiene las estaciones que suministran el tipo de combustible (`fuel_type_code`), y ambas tablas están conectadas por este código.

**Gráficamente:**
- **Vehicles.fuel_type** ───► **Fuel Stations.fuel_type_code** (Relación N:1)

**Explicación:**
Un vehículo utiliza un único tipo de combustible, pero varias estaciones pueden suministrar el mismo tipo de combustible. Esta relación es de **muchos a uno**.

---

### Relación 6: **Economía de Combustible y Vehículos (Fuel Economy Data - Vehicles)**

**Descripción:**
La economía de combustible (Fuel Economy Data) está vinculada a los vehículos por su **fabricante** y **modelo**. Esta información incluye datos como millas por galón, emisiones de CO2 y costos anuales de combustible. La entidad **Fuel Economy Data** contiene estos datos y está relacionada con la entidad **Vehicles**.

**Gráficamente:**
- **Fuel Economy Data.model** ───► **Vehicles.model** (Relación 1:N)

**Explicación:**
Un modelo de vehículo tiene un único registro en la economía de combustible, pero varios vehículos del mismo modelo pueden estar en servicio. Esta relación es de **uno a muchos**.

---

### Relación 7: **Viajes y Tarifas (Trips - Congestion, Surcharges, Payments)**

**Descripción:**
Cada viaje tiene un conjunto de tarifas y recargos (como el recargo por congestión o tarifas de mejora), que están relacionados directamente con cada registro de viaje. Estos campos (`congestion_surcharge`, `improvement_surcharge`, `payment_type`) forman parte de la entidad **Trips**.

**Gráficamente:**
- **Trips.congestion_surcharge** (Valor)
- **Trips.improvement_surcharge** (Valor)
- **Trips.payment_type** (Valor)

**Explicación:**
Las tarifas y recargos son atributos directos del viaje y están asociados a cada viaje de manera individual. Aquí no hay una relación explícita con otras tablas, pero estas columnas son críticas para el análisis de costos y eficiencia operativa.

---

### Resumen Gráfico Simulado:

- **Viajes (Trips)** están relacionados con:
  - **Ubicaciones Geográficas (PULocationID y DOLocationID)**.
  - **Clima durante el viaje (Meteorological Data)**.
  - **Vehículos usados (Vehicles)**.
  - **Tarifas y recargos asociados (Congestion, Surcharges)**.
  
- **Vehículos (Vehicles)** están relacionados con:
  - **Estaciones de combustible (Fuel Stations)**.
  - **Economía de combustible (Fuel Economy Data)**.

- **Ubicaciones Geográficas** están relacionadas con:
  - **Mediciones de calidad del aire (Air Quality Measurement)**.
  - **Viajes (Trips)** que ocurren en esa ubicación.

Estas relaciones definen el flujo de datos clave entre diferentes entidades para realizar análisis complejos sobre transporte, sostenibilidad, eficiencia y costo en la ciudad de Nueva York.
