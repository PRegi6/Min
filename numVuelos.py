import pandas as pd
import matplotlib.pyplot as plt

#Leo el dataframe y agrupo por aeropuerto origen y destino para comprobar cuantas veces aparace un vuelo con esas características
df = pd.read_csv('itineraries_clean.csv')
df = df.groupby(['startingAirport', 'destinationAirport']).count().reset_index()
df.columns = ['startinAirport', 'destinationAirport', 'Count']

#Genero un gráfico de barras para ver de manera gráfica los resultados
plt.bar(df['startingAirport'] + ' to ' + df['destinationAirport'], df['Count'])
plt.xticks(rotation=90)
plt.xlabel('Aeropuertos de origen y destino')
plt.ylabel('Número de apariciones')
plt.title('Apariciones de cada par de aeropuertos de origen y destino')

plt.savefig('grafico_aeropuertos.png', bbox_inches='tight')