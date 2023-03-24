# Proyecto final de la asignatura Minería de datos y el paradigma Big Data - curso 2022/23

# Datos utilizados para la obtención de resultados
Para el análisis de datos hemos usado un dataset que contiene información de los vuelos encontrados en Expedia entre las fechas 16/04/2022 y 05/10/2022.
Link a la página fr kaggle del dataset [aquí](https://www.kaggle.com/datasets/dilwong/flightprices).
El dataset ofrece gran variedad de datos acerca de cada vuelo pero para sacar conclusiones interesantes nos hemos enfocado en los siguientes:

- searchDate (Fecha de la búsqueda del vuelo)
- flightDate (Fecha de vuelo)
- startingAirport (Aeropuerto origen)
- destinationAirport (Aeropuerto destino)
- travelDuration (Duración del viaje en horas y minutos)
- isBasicEconomy (Booleano que indica que el precio del vuelo es asequible)
- seatsRemaining (Número de asientos libres en los vuelos)
- totalFare (Precio del vuelo con impuestos añadidos)
- totalTravelDistance (Distancia recorrida en el vuelo contando escalas)
- segmentsAirlineName (Nombre de la aerolínea encargada del vuelo)
- segmentsAirlineCode (Código de la aerolínea encargada del vuelo)

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
- Kaggle: Página web para la obtrención del dataset

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
$ sudo apt-get install python3-pip (si no tienes instalado el pip)
$ pip install pandas
$ pip install matplotlib
(mirar si no tiene pandas instalado)
```

# Página web
* [Página web](https://tripanalistycs.odoo.com/@/)

Resultados para mineria:
- Numero de vuelos por cada par de aeropuertos (origen y destino) -> Hecho 
- Aerolineas más solicitadas
- Cuantos vuelos hay de economia basica y cuantos no por cada par de aeropuertos -> (Hecho)
- Relacion entre los viajes que más tardan y cuantas personas los eligen
- Relacion entre los viajes más caros y cuantas personas los eligen
- Numero de vuelos buscados en x mes -> Hecho
- Relacion entre vuelos (aeropuertos origen y destino) con la aerolinea que se encarga de dicho vuelo
- Aerolineas que ofrecen vuelos más baratos