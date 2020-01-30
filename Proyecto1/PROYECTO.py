from wordcloud import WordCloud
import pandas
csv2=open('Etiquetas2.csv')

import csv
reader = csv.DictReader(csv2,delimiter=',')#DictReader metodo para leer sabiendo que valor es cada columna
print(reader)
#El archivo contiene ID,Tagname, count, ExcerptPostId, WikiPostId
nombres=[]
frecuencias=[]
for linea in reader:
    nombres.append(linea['tn'])#append agregar
    frecuencias.append(float(linea['count']))
print(nombres)
#Hay que crear diccionario de frecuencias para que solgan completas las palabras
frecuencias2=dict(zip(nombres,frecuencias))#diccionario para convertir las filas en diccionario,frecuencia 2 es un diccionario
    #frecuencias2[tagname]=count
print(frecuencias2)
Nube=WordCloud(width=1000, height=1000,
                      background_color='black',
                      min_font_size=10).fit_words(frecuencias2)#fit para generar las palabtras
Nube.to_file("ImagenEtiquetas.png")
