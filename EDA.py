# Importamos las librerías necesarias para el análisis exploratorio de datos.
import pandas as pd

# Importamos el dataset de crimenes en Los Angeles.
crimenes = pd.read_csv('C:/Users/Usuario/Documents/ITBA/Data set - Crimenes en Los Angeles/Crimenes en Los Angeles.csv', usecols=range(1, 27))

# Obtenemos una preview del dataset y sus principales caracteristicas.
print(crimenes.head(5))

