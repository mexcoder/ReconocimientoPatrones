 # Actividad 03 Ayuda
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('owid-covid-data.csv')
data = data[data.location == 'Mexico']
data.plot(y = 'new_cases')

n = 0
while True:
    if data.new_cases.values[n] > 0:
        break
    else:
        n+=1

data = data[n:]