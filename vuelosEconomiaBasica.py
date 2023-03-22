#No funciona

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('itineraries_clean.csv')
df = df.groupby(['startingAirport', 'destinationAirport', 'isBasicEconomy']).size().reset_index(name='Count')

# Crear una lista con las etiquetas y otra con los tamaños
labels = []
sizes = []
for isBasicEconomy in [True, False]:
    # Filtrar los itinerarios que tengan el tipo de tarifa correspondiente
    filtered_df = df[df['isBasicEconomy'] == isBasicEconomy]
    
    # Verificar si el dataframe filtrado contiene algún elemento
    if not filtered_df.empty:
        # Agregar las etiquetas y los tamaños a las listas correspondientes
        labels += filtered_df['startingAirport'] + ' to ' + filtered_df['destinationAirport']
        sizes += filtered_df['Count'].tolist()

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Itinerarios por combinación de aeropuertos y tipo de tarifa')
plt.show()