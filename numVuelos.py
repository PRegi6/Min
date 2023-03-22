import pandas as pd
import matplotlib.pyplot as plt

# Leo el dataframe
df = pd.read_csv('itineraries_clean.csv')

# Me quedo con los vuelos únicos, evito repeticiones del mismo vuelo
df = df.drop_duplicates(subset=['legId'])

# Convertir a objeto datetime para poder filtrar bien
df['flightDate'] = pd.to_datetime(df['flightDate'])
start_date = pd.Timestamp('2022-07-01')  # Fecha de inicio
end_date = pd.Timestamp('2022-07-31')  # Fecha de fin
df = df.loc[(df['flightDate'] >= start_date) & (df['flightDate'] <= end_date)]

df = df[['startingAirport', 'destinationAirport']]
df = df.groupby(['startingAirport', 'destinationAirport']).size().reset_index(name='Count')

# Generar gráfico circular
plt.pie(df['Count'], labels=df['startingAirport'] + ' to ' + df['destinationAirport'], autopct='%1.1f%%')
plt.title('Apariciones de cada par de aeropuertos de origen y destino (Julio 2022)')

plt.savefig('grafico_aeropuertos.png', bbox_inches='tight')