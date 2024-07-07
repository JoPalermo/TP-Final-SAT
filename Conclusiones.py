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










