#!/usr/bin/env python
# coding: utf-8

# # S8 Proyecto
# ## parte 1

# In[5]:


# S8 Proyecto p1

"""
Escribe un código para analizar los datos sobre el clima en Chicago en noviembre de 2017 desde el sitio web:
[https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html)
El nombre del DataFrame debe ser weather_records y tienes que especificarlo cuando buscas: attrs={"id": "weather_records"} . Imprime el DataFrame completo.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd 

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html' #guardamos el sitio del clima de chicago en 'Nov-2017'
req = requests.get(URL) # llamamos el sitio
soup = BeautifulSoup(req.text, 'lxml') # convertimos en texto 

table = soup.find('table',attrs={"id": "weather_records"})
# aplicando el método de búsqueda a la etiqueta de la tabla
# especificando el atributo de la primera tabla: weather_records

heading_table = []  # Lista donde se almacenarán los nombres de las columnas
for row in table.find_all(
    'th'
):  # Los nombres de las columnas están dentro de los elementos <th>,
    # así que encontraremos todos los elementos <th> en la tabla y los ejecutaremos en un bucle
    heading_table.append(
        row.text
    )  # Agrega el contenido de la etiqueta <th> a la lista heading_table usando append()

content = []  # lista donde se almacenarán los datos de la tabla
for row in table.find_all('tr'):
    # Cada fila está envuelta en una etiqueta <tr>, necesitamos recorrer todas las filas
    if not row.find_all('th'):
        # Necesitamos esta condición para ignorar la primera fila de la tabla, con encabezados
        content.append([element.text for element in row.find_all('td')])

weather_records = pd.DataFrame(content, columns=heading_table)
print(weather_records)


# ## Parte 2

# # S8 Proyecto p2
# 
# Instruccion: 
# Imprime el campo company_name. Encuentra la cantidad de viajes en taxi para cada compañía de taxis para el 15 y 16 de noviembre de 2017, asigna al campo resultante el nombre trips_amount e imprímelo también. Ordena los resultados por el campo trips_amount en orden descendente.

# #SQL 
# 
# ###ej 1
# 
# SELECT 
#     cabs.company_name AS company_name,
#     COUNT(trips.trip_id) AS trips_amount
# FROM
#     trips
#         LEFT JOIN cabs ON cabs.cab_id = trips.cab_id                  
# WHERE 
#     CAST(start_ts AS date) BETWEEN '2017-11-15' AND '2017-11-16'
# GROUP BY 
#     cabs.company_name
# ORDER BY 
#     trips_amount DESC

# ###ej 2 
# 
# 
# Encuentra la cantidad de viajes para cada empresa de taxis cuyo nombre contenga las palabras "Yellow" o "Blue" del 1 al 7 de noviembre de 2017. Nombra la variable resultante trips_amount. Agrupa los resultados por el campo company_name
# 
# # SQL
# 
# SELECT 
#     cabs.company_name AS company_name,
#     COUNT(trips.trip_id) AS trips_amount
# FROM
#     cabs
#         INNER JOIN trips ON cabs.cab_id = trips.cab_id                  
# WHERE 
#    cabs.company_name LIKE '%Yellow%'  AND CAST(start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
# OR 
#     cabs.company_name LIKE '%Blue%' AND CAST(start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
# GROUP BY 
#     cabs.company_name;

# ###ej 3 
# 
# Del 1 al 7 de noviembre de 2017, las empresas de taxis más populares fueron Flash Cab y Taxi Affiliation Services. Encuentra el número de viajes de estas dos empresas y asigna a la variable resultante el nombre trips_amount. Junta los viajes de todas las demás empresas en el grupo "Other". Agrupa los datos por nombres de empresas de taxis. Asigna el nombre company al campo con nombres de empresas de taxis. Ordena el resultado en orden descendente por trips_amount.
# 
# # SQL
# 
# SELECT        
#     CASE 
#         WHEN company_name = 'Flash Cab' THEN 'Flash Cab'
#         WHEN company_name = 'Taxi Affiliation Services' THEN 'Taxi Affiliation Services'
#     ELSE 'Other'
# END AS company,
#     COUNT(trips.trip_id) AS trips_amount
# FROM
#     cabs
#       INNER JOIN trips ON cabs.cab_id = trips.cab_id 
# WHERE 
#     CAST(start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
# GROUP BY 
#     company
# ORDER BY 
#     trips_amount DESC;

# ### ej4 
# 
# Recupera los identificadores de los barrios de O'Hare y Loop de la tabla neighborhoods.
# 
# # SQL
# 
# SELECT        
#     name,
#     neighborhood_id    
# FROM
#     neighborhoods
# WHERE 
#    name LIKE '%Hare' OR name LIKE 'Loop'

# ### ej5
# 
# Para cada hora recupera los registros de condiciones meteorológicas 
# de la tabla weather_records. Usando el operador CASE, divide todas las
# horas en dos grupos: Bad si el campo description contiene las palabras 
# rain o storm, y Good para los demás. Nombra el campo resultante weather_conditions.
# La tabla final debe incluir dos campos: fecha y hora (ts) y weather_conditions.
# 
# # sql
# SELECT        
#     ts,
#     CASE 
#         WHEN description LIKE '%rain%' OR description LIKE '%storm%' THEN 'Bad'
#         ELSE 'Good'
#     END AS weather_conditions
# FROM
#     weather_records
# 

# ### ej6
# 
# Recupera de la tabla de trips todos los viajes que comenzaron en el Loop (pickup_location_id: 50) el sábado y terminaron en O'Hare (dropoff_location_id: 63). Obtén las condiciones climáticas para cada viaje. Utiliza el método que aplicaste en la tarea anterior. Recupera también la duración de cada viaje. Ignora los viajes para los que no hay datos disponibles sobre las condiciones climáticas.
# 
# Las columnas de la tabla deben estar en el siguiente orden:
# 
# start_ts
# weather_conditions
# duration_seconds
# Ordena por trip_id.
# # SQL
# 
# SELECT        
#     trips.start_ts,
#     CASE -- traemos la consulta del clima del ej5
#         WHEN description LIKE '%rain%' OR description LIKE '%storm%' THEN 'Bad'
#     ELSE 'Good'
# END AS weather_conditions,
#     duration_seconds
# FROM
#     trips
#     INNER JOIN weather_records ON trips.start_ts = weather_records.ts -- unimos las tablas con 2 columnas de fecha ts y satart_ts aunqueno son coincidentes al 100%
# WHERE 
#     trips.pickup_location_id = 50 -- lugar de pickup
#     AND trips.dropoff_location_id = 63 -- cambia a dropoff
#     AND EXTRACT (DOW from trips.start_ts) = 6 -- el 6 del 0al 6 de los 7 dias es el Sabado del mes de nov 2017
# ORDER BY 
#     trip_id;

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM trips \nWHERE pickup_location_id = 50\n')


# In[7]:


# Parte 4 graficos y analisis en pandas  y py 

import pandas as pd
from matplotlib import pyplot as plt # importamos para los graficos 

companies = pd.read_csv('moved_project_sql_result_01.csv') # no hay acceso los archviso csv

print(companies.info(),companies.head()) # con estos 2 metodos tenemos una vista de data types y estructura de los 2 df

doln = pd.read_csv('moved_project_sql_result_04.csv') # dol = dropoff_location_name

print(doln.info(), doln.head())

doln.sort_values('average_trips', ascending=False) # con esta linea sabemos los 10 vecindario / colonias con mayor destino


# In[9]:


# grafico 1 'companies'

# revisamos la cantidad de empresas son 64 por lo cual solo porndremos por legebilildad las top 10  

print(len(companies['company_name'].unique())) 

# agrupamos los datos de las empresas para que se vean consolidados y luego procedemos a sacar el top 10

companies_grouped = companies.groupby('company_name')['trips_amount'].sum().reset_index() 

top_10_companies = companies_grouped.sort_values('trips_amount', ascending=False).head(10) # traemos solo el top 10 

colores_azules = ['#003366', '#004080', '#0066cc', '#3399ff', '#66b3ff', 
                  '#99ccff', '#b3d9ff', '#cce6ff', '#e6f3ff', '#f0f8ff']

top_10_companies.plot(title = "# Trips Chicago / Company",
        kind= 'bar',
        x= "company_name",
        y= "trips_amount",
        color = colores_azules,              
        figsize = [5,5],
        rot = 90,
        ylabel = "16 & 17-nov-2017",
        xlabel = "")


# In[8]:


# grafico 2 

top_10_vecindarios = doln.sort_values('average_trips', ascending=False).head(10) # con esta linea sabemos los 10 vecindario / colonias con mayor destino

colores_amarillos = ['#b8860b', '#daa520', '#ffd700', '#ffdc00', '#ffe135', 
                     '#ffe66d', '#ffeb9c', '#fff2cc', '#fff8dc', '#fffacd']

top_10_vecindarios.plot(title = " Top 10 vencidarios Chicago",
        kind= 'bar',
        x= "dropoff_location_name",
        y= "average_trips",
        color = colores_amarillos,              
        figsize = [5,5],
        rot =75,
        ylabel = "16 & 17-nov-2017",
        xlabel = "")


# # Analisis de los resultados de las graficas
# ## Grafica 1 
# Por lo que vemos en el primer gráfico "Trips Chicago / Company"
# 
# Es un analisis del top 10 de una base de datos de 64 empresas para los días viernes y Sábado 16 y 17 de nov 2017; en las que: 
# 
# Podemos ver que la empresa Flash Cab lidera esos días con casi 20 mil viajes siendo día, seguido de Taxi Affilation Services con 11,422, de la empresa 3 al 5 y del 6 al 9 rondadno los 8,000 viajes salvo el 10 que ya cae cercano a los 5000 viajes. Están todos cercacnos alos 10 mil viajes que son casi la mitad del primer lugar, donde cabe hacerse la pregunta porqué están grande la brecha entre ese 1er lugar y el resto de compañias en el sector. Podría ser un mejor serivicio, flotilla más grandes de autos o costos más accesibles. 
# 
# ## Grafica 2 
# 
# En esta gráfica llamada Top 10 Vencindarios podemos ver tambien concentraciones importantes siendo el barrio de Loop el más concurrido con más de 10 mil viajes en promedio terminados, seguido de River North con una cantidad promedio similar lijeramente menro a los 10k viajes, en 3° y 4° están Streeterville & West Loop respectivamente, de estas rondando los 6000 viajes promedio y de ahi al resto desceienden estrepitosamente de los 2,500 hacia abajo. 
# Podríamos suponer que esos barrios es donde está la fiesta y lugares de esparcimiento al ser fin de semana los días de la muestra. O quiza una zona con mayor población dentro de Chicago. Buscando en internet efectivamente el loop es la zona más poblada de Chicago y también coincide la 2nda suposición "The Loop: El corazón de la ciudad, con acceso directo a museos, teatros, el Millennium Park y el lago Michigan. Ideal para turistas por su ubicación central" por lo cual hace logica que sea una zona con mucho más actividad que el resto. 

# In[ ]:


# parte 5 

loop_airport = pd.read_csv("moved_project_sql_result_07.csv")

print(loop_airport.info())

 # saco la media de la duracion de viajes en minutos ya que es una unidad más entendible y para ver el comportamiento 

loop_airport["duration_seconds"] = loop_airport["duration_seconds"]/60  # conversion a minutos
loop_airport = loop_airport.rename(columns={"duration_seconds": "duration_min"}) # cambio a muinutos

print(loop_airport.head(1),loop_airport.describe()) #34.53 min la media de los viajes



# In[ ]:


# Prueba de hipotesis 
from scipy import stats as st
import math as mt
from scipy.stats import ttest_ind
import numpy as np

# cantidad de dias lluviosos vs dias con buen clima

print(loop_airport['weather_conditions'].value_counts()) 

#180 bad (lluvia) y 888 Good (sin lluvia) 
#total 1068 los malos son el 16.85% y 83.15% los buenos

dias_buenos = loop_airport[loop_airport['weather_conditions'] == 'Good']['duration_min']
dias_lluviosos = loop_airport[loop_airport['weather_conditions'] == 'Bad']['duration_min'] 

# o el valor que corresponda

print(f"Días buenos: {len(dias_buenos)} viajes, media: {dias_buenos.mean():.2f} min")
print(f"Días lluviosos: {len(dias_lluviosos)} viajes, media: {dias_lluviosos.mean():.2f} min")


interested_value = 33.33 # duración de  los viajes de Loop - O'Hare airport
alpha = 0.05 # indica el nivel de significación estadística

results = st.ttest_ind(dias_buenos, dias_lluviosos) # probamos la hipotesis 
print('valor p:', results.pvalue)

if ((results.pvalue < alpha) and (dias_buenos.mean() < interested_value)):
    print("Rechazamos la hipótesis nula: La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos")
else:
    print("No podemos rechazar la hipótesis nula: la duracion de los viajes con días lluviosos no cambia significativamente")



# Podemos observar algo esperado que aumente la duracion de los viajes ya que con lluvia todo mundo maneja mas lento por seguridad y menos gente sale en transportes alternos lo cual congestiona vialidades, viendo los valores:
# 
# Días buenos: 33.33 minutos promedio Días lluviosos: 40.45 minutos promedio Diferencia: Aproximadamente 7 minutos más (21% de aumento)
# 
# El valor p extremadamente bajo (6.52e-12) confirma estadísticamente que esta diferencia es altamente significativa, no es casualidad.
# 
# Ademas de que los sabados son d+ias congestionados en la ciudad de chicago por la actividad cultural como ya veíamos en las graficas anteriores.

# In[ ]:




