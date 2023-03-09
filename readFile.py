import numpy as np
import pandas as pd

data = pd.read_csv('./Data/itineraries_300000_clean.csv',decimal='.',parse_dates=[1,2])
arrayNp = data.to_numpy()
print(data.columns)
print(arrayNp[-10:])