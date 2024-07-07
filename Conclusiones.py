# En este archivo se encuentran las conclusiones del analisis realizado en el archivo EDA.py.
# Tomo el Data Set que obtuve en EDA.py y lo analizo para obtener conclusiones.

# Importamos las librerias necesarias:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

# Cargamos el dataset:
Trabajos_LinkedIn = pd.read_csv('C:/Users/Usuario/Documents/ITBA/SAT - 81.75/TP - Final - SAT/Trabajos_LinkedIn_Final.csv')

# Visualizamos las primeras filas del dataset:
print("\n--- Preview Dataset ---")
print(Trabajos_LinkedIn.head(5))

# Que titulo de trabajo se repite mas?
Titulos_de_trabajos = ' '.join(Trabajos_LinkedIn['title'])
filtro = set(['Full', 'Time', 'Part', 'Time'])
filtro_todo = set(STOPWORDS) | filtro
wordcloud = WordCloud(width=900, height=500, background_color='white', colormap='coolwarm', stopwords=filtro_todo).generate(Titulos_de_trabajos)
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Titulos de los Trabajos', fontsize=20)
plt.axis('off')
plt.tight_layout()
plt.show()

# Que tipo de trabajo es mas comun?
Tipo_Trabajo = Trabajos_LinkedIn['formatted_work_type'].value_counts()/Trabajos_LinkedIn['formatted_work_type'].value_counts().sum()*100
plt.figure(figsize=(14, 6))
Tipo_Trabajo.plot(kind='bar', color='olive')
plt.title('Tipo de trabajo mas comun [%]', fontsize=20)
plt.xlabel('Tipo de trabajo')
plt.ylabel('% Sobre el total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Que tamaño tienen las empresas que ofrecen trabajo?
Tamaño_empresa = Trabajos_LinkedIn['company_size'].value_counts()/Trabajos_LinkedIn['company_size'].value_counts().sum()*100
plt.figure(figsize=(12, 9))
plt.pie(Tamaño_empresa, labels=Tamaño_empresa.index, autopct='%1.1f%%', colors=[ 'green', 'yellow', 'orange','red', 'pink', 'purple', 'blue'])
plt.title('Tamaño de las empresas que ofrecen trabajo [%]', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.show()

# Cuales son las empresas que mas trabajo ofrecen?
Empresas_mas_trabajo = Trabajos_LinkedIn['name'].value_counts().head(5)
plt.figure(figsize=(10, 6))
Empresas_mas_trabajo.plot(kind='bar', color='purple')
plt.title('5 empresas que mas trabajo ofrecen', fontsize=20)
plt.xlabel('Nombre Empresa')
plt.ylabel('Cantidad de trabajos publicados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Se puede trabajar remoto?
Remoto = Trabajos_LinkedIn['remote_allowed'].value_counts()/Trabajos_LinkedIn['remote_allowed'].value_counts().sum()*100
plt.figure(figsize=(10, 8))
Remoto.plot(kind='pie', autopct='%1.1f%%', startangle=200, colors=['grey', 'brown'])
plt.title('Remoto permitido [%]', fontsize=20)
plt.ylabel('')
plt.show()

# Que nivel de experiencia se requiere?
Experiencia = Trabajos_LinkedIn['formatted_experience_level'].value_counts()/Trabajos_LinkedIn['formatted_experience_level'].value_counts().sum()*100
plt.figure(figsize=(10, 6))
Experiencia.plot(kind='bar', color='orange')
plt.title('Experiencia Requerida', fontsize=20)
plt.xlabel('Tipo de Experiencia')
plt.ylabel('Procentaje del total de trabajos publicados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(Experiencia)

# Que habilidades se requieren?
Habilidades = Trabajos_LinkedIn['skill_abr'].value_counts().head(10)
plt.figure(figsize=(10, 6))
Habilidades.plot(kind='bar', color='red')
plt.title('Habilidades requeridas', fontsize=20)
plt.xlabel('Habilidad')
plt.ylabel('Procentaje del total de trabajos publicados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(Habilidades)