# Importamos las librerias que se van a utilizar:
import pandas as pd
import numpy as np

# Importamos el Data Set con el nombre "crimenes":
#dtypes = {'DR_NO':int, 'Date Rptd':str, 'DATE OCC':str, 'TIME OCC':int, 'AREA':int, 'AREA NAME':str, 'Rpt Dist No':int, 'Part 1-2':int, 'Crm Cd':int, 'Crm Cd Desc':str, 'Mocodes':str, 'Vict Age':int, 'Vict Sex':str, 'Vict Descent':str, 'Premis Cd':int, 'Premis Desc':str, 'Weapon Used Cd':int, 'Weapon Desc':str, 'Status':str, 'Status Desc':str, 'Crm Cd 1':int, 'Crm Cd 2':int, 'Crm Cd 3':int, 'Crm Cd 4':int, 'LOCATION':str, 'Cross Street':str, 'LAT':int, 'LON':int}
crimenes = pd.read_csv("C:/Users/Usuario/Documents/ITBA/Data set - Crimenes en Los Angeles/Crimenes en Los Angeles.csv")

# Previsualizacion del dataset y renombramos las columnas:
#crimenes.sample(5) # Previsualizacion del dataset
#crimenes.columns = ['ID', 'Date 1', 'Date 2', 'Time 1', 'Num_Area', 'Nom_Area', 'Nose 1', 'Parte', 'Nose 2', 'Nose 3', 'Nose 4', 'Edad_Vict', 'Sexo_Vict', 'Nose 5', 'Nose 6', 'Nose 7', 'Cod_Arma', 'Desc_Arma', 'Estado', 'Desc_Estado', 'Nose 8', 'Nose 9', 'Nose 10', 'Nose 11', 'Localidad', 'Interseccion', 'Latitud', 'Longitud']


#crimenes.shape # Dimensiones del dataset


