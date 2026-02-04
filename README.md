# Zuber-S8-project
S8 tripleten Pyhton / SQL project

# Análisis de Datos de Taxis en Chicago - Sprint 8

## Descripción del Proyecto

Este proyecto forma parte del Sprint 8 del curso de Análisis de Datos, donde se realiza un análisis exploratorio de datos sobre el mercado de taxis en Chicago para la empresa Zuber, una nueva compañía de viajes compartidos que se está lanzando en la ciudad.

## Objetivos

- Analizar patrones en los datos de viajes de taxi en Chicago
- Identificar las principales empresas de taxis y su participación en el mercado
- Determinar los barrios más populares como destinos de viajes
- Probar hipótesis sobre el impacto del clima en la duración de los viajes

Datos Utilizados
### Dataset 1: Empresas de Taxis (project_sql_result_01.csv)
- company_name: Nombre de la empresa de taxis
- trips_amount: Número de viajes de cada compañía (15-16 noviembre 2017)

### Dataset 2: Destinos por Barrio (project_sql_result_04.csv)
- dropoff_location_name: Barrios de Chicago donde finalizaron los viajes
- average_trips: Promedio de viajes que terminaron en cada barrio (noviembre 2017)

### Dataset 3: Viajes Loop-Aeropuerto (project_sql_result_07.csv)
- start_ts: Fecha y hora de inicio del viaje
- weather_conditions: Condiciones climáticas al inicio del viaje
- duration_seconds: Duración del viaje en segundos

Metodología
### 1. Análisis Exploratorio de Datos
- Importación y exploración inicial de los datasets
- Validación de tipos de datos y estructura
- Identificación de las top 10 empresas de taxis
- Análisis de los 10 barrios principales por destinos

### 2. Visualización de Datos
- Gráfico de barras: Empresas de taxis y número de viajes
- Gráfico de barras: Top 10 barrios por número de destinos
- Análisis visual de patrones y tendencias

### 3. Prueba de Hipótesis
- Hipótesis Nula (H₀): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia los sábados lluviosos
- Hipótesis Alternativa (H₁): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare SÍ cambia los sábados lluviosos
- Nivel de significación: α = 0.05
- Método: Prueba t de Student para muestras independientes

Librerías Utilizadas
pandas: Manipulación y análisis de datos
matplotlib: Creación de visualizaciones
scipy: Pruebas estadísticas
numpy: Operaciones numéricas
math: Operaciones matemáticas básicas
Principales Hallazgos
### Empresas de Taxis
- Flash Cab lidera el mercado con ~20,000 viajes en el período analizado
- Taxi Affiliation Services ocupa el segundo lugar con ~11,400 viajes
- Existe una brecha signific

## Estructura del Proyecto

```
taxi-analysis-chicago/
│
├── notebook.ipynb          # Notebook principal con el análisis
├── README.md              # Este archivo
└── datasets/              # Archivos de datos (no incluidos en el repositorio)
    ├── project_sql_result_01.csv
    ├── project_sql_result_04.csv
    └── project_sql_result_07.csv
```
## Autor
[Julián De La Garza Lepe]
