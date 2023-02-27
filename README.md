# Vuela Bonito y Barato
Proyecto final de la asignatura Cloud y Big Data - curso 2022/23

# Objetivo
Hemos analizado un conjunto de datos con información de un gran número de vuelos en EEUU, con el fin de llegar a conclusiones interesantes como cuáles son los viajes más económicos, cuáles son los destinos más frecuentes y con ello en que estados o ciudades el tráfico aéreo es más intenso o que días de la semana son más frecuentes.

# Necesidad de utilizar Big Data
Analizar la gran cantidad de vuelos y los datos asociados a cada vuelo es bastante costoso. Además, si queremos obtener resultados sencillamente y en un tiempo razonable es imprescindible aplicar la tecnología Big Data y 'large-scale parallel processing'.

# Datos utilizados para la obtención de resultados
Para el análisis de datos hemos usado un dataset que contiene información de los vuelos encontrados en Expedia entre las fechas 16/04/2022 y 05/10/2022.
Link a la página fr kaggle del dataset [aquí](https://www.kaggle.com/datasets/dilwong/flightprices).
El dataset ofrece gran variedad de datos acerca de cada vuelo pero para sacar conclusiones interesantes nos hemos enfocado en los siguientes:

- startingAirport (Aeropuerto origen)
- destinationAirport (Aeropuerto destino)
- flightDate (Fecha de vuelo)
- totalTravelDistance (Distancia recorrida en el vuelo contando escalas)
- totalFare (Precio del vuelo con impuestos añadidos)
- segmentsAirlineCode (Código de la aerolínea encargada del vuelo)
- seatsRemaining (Número de asientos libres en los vuelos)

Hemos utilizado como complemento otro archivo, 'USA_Covid_Data.csv', para poder relacionar el número de vuelos con el número de casos positivos oficiales por estado. Para este caso en concreto usamos el campo 'destinationAirport' de nuestro dataset original y los campos 'State', estado donde se observa la muestra, 'Active', casos positivos oficiales, y el campo 'Population' que representa el censo total del estado.

# Resultados gracias a los datos obtenidos 

- Promedio de tarifas por empresa
- Relación entre casos de covid y el número de vuelos
- Número de vuelos por día
- Relación entre distancia y tarifa
- Número de vuelos por aerolínea
- Evolución de la tarifa según los días
- Número de viajes sin escalas
- Vuelos por día
- Viajes más comunes

# Herramientas utilizadas
- Google Cloud: Servicio online para alojar las máquinas virtuales y clusters utilizados para procesar los datos.
- Apache Spark: Motor multi-lenguaje utilizado para facilitarnos la ejecución de los datos.
- Python: Lenguaje de programación base para ejecutar spark.
- Github: Servicio online para alojar todo el material correspondiente al proyecto.
- Kaggle: Página web de 

# Speed up y diferencia de rendimiento con distintos working nodes
> Utilizando una instancia de un cluster de 4 vCPU y cambiando el número de nodos trabajadores  
- TripsPerDay -> 2 Nodos -> 26 segundos 
- TripsPerDay -> 3 Nodos -> 23 segundos  
- TripsPerDay -> 5 Nodos -> 22 segundos 

- EmpresasFind -> 2 Nodos -> 1 min 2 sec 
- EmpresasFind -> 3 Nodos -> 58 sec 
- EmpresasFind -> 5 Nodos -> 57 sec 

- Viajes_concurridos -> 2 Nodos -> 1 min 17 sec 
- Viajes_concurridos -> 3 Nodos -> 1 min 16 sec 
- Viajes_concurridos -> 5 Nodos -> 1 min 13 sec 

> Utilizando una instancia de un cluster de 2 vCPU y cambiando el número de nodos trabajadores
- TripsPerDay -> 2 Nodos -> 33 segundos 
- TripsPerDay -> 3 Nodos -> 34 segundos 
- TripsPerDay -> 4 Nodos -> 32 segundos 

- EmpresasFind -> 2 Nodos -> 1 min 29 sec 
- EmpresasFind -> 3 Nodos -> 1 min 24 sec 
- EmpresasFind -> 4 Nodos -> 1 min 21 sec  

- Viajes_concurridos -> 3 Nodos -> 1 min 56 sec  
- Viajes_concurridos -> 3 Nodos -> 1 min 41 sec  
- Viajes_concurridos -> 4 Nodos -> 1 min 37 sec 

Podemos observar un breve speed-up respecto a ampliar el número de nodos trabajadores, pero no hay mucha diferencia, 
ya que no es directamente proporcional el ampliar el número de nodos (Depende de otros factores como el código , el lenguaje ...)

Pero está claro que es mucho más importante ampliar el número de vCPUs para ampliar el rendimiento; sin embargo, no hemos podio ampliar más,
ya que nuestra licencia nos limitaba el número de CPUs que podemos utilizar para clusters.

Lo hemos hecho con 3GB solo, ya que lo importante es ver el speed up si lo hubiera. Está claro que con más volumen de datos 
la diferencia de tiempo sería mayor

Está reflejado todo esto en el gráfico **performance_plot.png**

# Descripción del proyecto

## Archivo utilizados:
* 2 archivo .csv del que obtenemos los datos
* 9 scripts para el procesamiento de los datos y la obtención de los gráficos
* 12 imágenes que ilustran los gráficos del análisis de datos

## Cómo ejecutar el programa
Para poder ejecutar spark en modo **local** es necesario tener instalado python.
```
$ sudo apt-get install python
```

Una vez tengamos python instalado hay que instalar pyspark
```
$ curl -O https://archive.apache.org/dist/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz
$ tar xvf spark-3.3.1-bin-hadoop3.tgz
$ sudo mv spark-3.3.1-bin-hadoop3 /usr/local/spark
```
Ahora hay que actualizar la variable PATH en el archivo ~/.profile
```
$ echo 'PATH="$PATH:/usr/local/spark/bin"' >> ~/.profile
$ source ~/.profile
```
Después de ejecutar todos los comandos anteriores ya podemos ejecutar los scripts especificando el archivo csv del que sacar los datos
```
$ spark-submit <script-name> <file.csv>
```
Ejemplo: $ spark-submit mergueDayStats.py itineraries_3GB.csv

Para poder ejecutar todos los scripts es imprescindible ejecutar los siguientes comandos:
```
$ sudo apt-get install python3-pip ( si no tienes instalado el pip )
$ pip install pandas
$ pip install matplotlib
(mirar si no tiene pandas instalado)
```
Estos dos comandos instalan pandas, herramienta complementaria para tratar los datos, y la librería matplotlib para conseguirlos gráficos con el análisis de datos

# Conclusiones
Las conclusiones obtenidas del procesamiento de los datos se muestran en la página web, asociadas a su gráfico correspondiente.

# Página web
* [Página web](https://tripanalistycs.odoo.com/@/)
