# Importamos las librerías necesarias para el análisis exploratorio de datos.
import pandas as pd

# Importamos el dataset de crimenes en Los Angeles.
crimenes = pd.read_csv('C:/Users/Usuario/Documents/ITBA/Data set - Crimenes en Los Angeles/Crimenes en Los Angeles.csv', usecols=range(2, 28))

# Obtenemos una preview del dataset.
print("\n--- Preview del dataset ---")
print(crimenes.head(5))

# Acomodamos el dataset.
crimenes.rename(columns={'DATE OCC':'Dia_Ocurrencia', 'TIME OCC':'Tiempo_Ocurrencia', 'AREA':'Cod_Area', 'AREA NAME':'Nom_Area', 'Rpt Dist No':'Num_Distrito', 'Part 1-2':'Parte', 'Crm Cd':'Cod_Crimen', 'Crm Cd Desc':'Desc_Crimen', 'Mocodes':'M_Cod', 'Vict Age':'Edad_Victima', 'Vict Sex':'Sexo_Victima', 'Vict Descent':'Descendencia_Victima', 'Premis Cd':'Cod_Tipo_Ubic', 'Premis Desc':'Desc_Tipo_Ubic', 'Weapon Used Cd':'Cod_Arma', 'Weapon Desc':'Desc_Arma', 'Status':'Cod_Estado', 'Status Desc':'Desc_Estado', 'Crm Cd 1':'Sub_Cod1', 'Crm Cd 2':'Sub_Cod2', 'Crm Cd 3':'Sub_Cod3', 'Crm Cd 4':'Sub_Cod4', 'LOCATION':'Direccion', 'Cross Street':'Interseccion', 'LAT':'Latitud', 'LON':'Longitud'}, inplace=True)
print("\n--- Filas & Columnas ---")
print("Cantidad de filas:", crimenes.shape[0])
print("Cantidad de columnas:", crimenes.shape[1])

print("\n--- Tipos de datos ---")
columnas = crimenes.columns
columna_tipo = [crimenes[col].dtype for col in columnas]
print("Numero Columna\tNombre Columna\t\tTipo de dato")
for idx, (name, dtype) in enumerate(zip(columnas, columna_tipo)):
    print(f"{idx + 1}\t\t{name}\t\t{dtype}")

# Cambio el tipo de datos de mis columnas.
crimenes['Cod_Area'] = crimenes['Cod_Area'].astype('int', errors='Nada')
crimenes['Nom_Area'] = crimenes['Nom_Area'].astype('str', errors='Nada')
crimenes['Num_Distrito'] = crimenes['Num_Distrito'].astype('int', errors='Nada')
crimenes['Parte'] = crimenes['Parte'].astype('int', errors='Nada')
crimenes['Cod_Crimen'] = crimenes['Cod_Crimen'].astype('int', errors='Nada')
crimenes['Desc_Crimen'] = crimenes['Desc_Crimen'].astype('str', errors='Nada')
crimenes['M_Cod'] = crimenes['M_Cod'].astype('str', errors='Nada')
crimenes['Edad_Victima'] = crimenes['Edad_Victima'].astype('int', errors='Nada')
crimenes['Sexo_Victima'] = crimenes['Sexo_Victima'].astype('str', errors='Nada')
crimenes['Descendencia_Victima'] = crimenes['Descendencia_Victima'].astype('str', errors='Nada')
crimenes['Cod_Tipo_Ubic'] = crimenes['Cod_Tipo_Ubic'].astype('int', errors='Nada')
crimenes['Desc_Tipo_Ubic'] = crimenes['Desc_Tipo_Ubic'].astype('str', errors='Nada')
crimenes['Cod_Arma'] = crimenes['Cod_Arma'].astype('int', errors='Nada')
crimenes['Desc_Arma'] = crimenes['Desc_Arma'].astype('str', errors='Nada')
crimenes['Cod_Estado'] = crimenes['Cod_Estado'].astype('int', errors='Nada')
crimenes['Desc_Estado'] = crimenes['Desc_Estado'].astype('str', errors='Nada')
crimenes['Sub_Cod1'] = crimenes['Sub_Cod1'].astype('int', errors='Nada')
crimenes['Sub_Cod2'] = crimenes['Sub_Cod2'].astype('int', errors='Nada')
crimenes['Sub_Cod3'] = crimenes['Sub_Cod3'].astype('int', errors='Nada')
crimenes['Sub_Cod4'] = crimenes['Sub_Cod4'].astype('int', errors='Nada')
crimenes['Direccion'] = crimenes['Direccion'].astype('str', errors='Nada')
crimenes['Interseccion'] = crimenes['Interseccion'].astype('str', errors='Nada')
crimenes['Latitud'] = crimenes['Latitud'].astype('float64', errors='Nada')
crimenes['Longitud'] = crimenes['Longitud'].astype('float64', errors='Nada')

