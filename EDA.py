# Importamos las librerias necesarias:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Cargamos el dataset:
Trabajos_LinkedIn = pd.read_csv("C:/Users/Usuario/Documents/ITBA/SAT - 81.75/TP - Final - SAT/postings.csv")

# Visualizamos las primeras filas del dataset: 
print("--- Preview Dataset ---")
print(Trabajos_LinkedIn.head(5))

# Visualizamos la cantidad de filas y columnas del dataset:
print("\n--- Cantidad de filas y columnas ---")
print(Trabajos_LinkedIn.shape)

# Visualizamos los nombres de las columnas:
print("\n--- Nombres de las columnas ---")
columnas = Trabajos_LinkedIn.columns
Nombres_columnas = pd.DataFrame({
    'Nombre de Columna': columnas
})
print(Nombres_columnas)

# Visualizamos la cantidad de valores nulos por columna:
print("\n--- Valores Nulos x Columna ---")
Valores_nulos = Trabajos_LinkedIn.isna().sum()
print(Valores_nulos)

# Corregimos los valores nulos para cada columna:
print("\n--- Correccion de Valores Nulos ---")
NaN = {"job_id" : "Unknown", "company_name" : "Unknown", "title" : "Unknown", "description" : "Unknown", "max_salary" : "Unknown", "pay_period" : "Unknown", "location" : "Unknown", "company_id" : "Unknown", "views" : "Unknown", "med_salary" : "Unknown", "min_salary" : "Unknown", "formatted_work_type" : "Unknown", "applies" : "Unknown", "original_listed_time" : "Unknown", "remote_allowed" : "Unknown", "job_posting_url" : "Unknown", "application_url" : "Unknown", "application_type" : "Unknown", "expiry" : "Unknown", "closed_time" : "Unknown", "formatted_experience_level" : "Unknown", "skills_desc" : "Unknown", "listed_time" : "Unknown", "posting_domain" : "Unknown", "sponsored" : "Unknown", "work_type" : "Unknown", "currency" : "Unknown", "compensation_type" : "Unknown",}
Trabajos_LinkedIn = Trabajos_LinkedIn.fillna(NaN)
Valores_nulos = Trabajos_LinkedIn.isna().sum()
print(Valores_nulos)

# Visualizamos la cantidad de valores unicos por columna:
print("\n--- Valores Unicos x Columna ---")
Valores_unicos = Trabajos_LinkedIn.nunique()
print(Valores_unicos)

# Obtenemos los valores descriptivos del dataset:
print(Trabajos_LinkedIn.describe(include= "all"))

# print(Trabajos_LinkedIn.company_name.value_counts())

