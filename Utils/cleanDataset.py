path = './Data/'
file = 'itineraries.csv'
finalFile = 'itineraries_clean.csv'

import pandas as pd

columnsSelected = [ 'legId', 'searchDate', 'flightDate', 'startingAirport',
    'destinationAirport', 'travelDuration',
    'isBasicEconomy', 'totalFare',
    'seatsRemaining', 'totalTravelDistance', 
    'segmentsAirlineName', 'segmentsAirlineCode']

data = pd.read_csv(file,usecols=columnsSelected)

data.to_csv(finalFile)