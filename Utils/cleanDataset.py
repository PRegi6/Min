path = './Data/'
file = 'itineraries.csv'
finalFile = 'itineraries.csv'

import pandas as pd

columnsSelected = [ 'searchDate', 'flightDate', 'startingAirport',
    'destinationAirport', 'travelDuration',
    'isBasicEconomy', 'totalFare',
    'seatsRemaining', 'totalTravelDistance', 
    'segmentsAirlineName', 'segmentsAirlineCode']

data = pd.read_csv(path + file,usecols=columnsSelected)

data.to_csv(path + finalFile)