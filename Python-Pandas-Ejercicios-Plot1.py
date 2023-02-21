from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


# ~ https://www.aluracursos.com/blog/matplotlib-una-biblioteca-python-para-crear-graficos-interesantes
# ~ https://www.aluracursos.com/blog/analisis-de-datos-analizando-mi-distribucion-con-tres-alternativas-de-visualizacion
# ~ https://datacarpentry.org/python-ecology-lesson-es/guide/index.html




def hechos():
    pass#,inplace=True
    print(f'''  

    ''')
def Solución():
    pass
#######################################################################################################


print(f'''
● Crear un objeto de la clase '`DataFrame`'.
''')
## Solución.
nombre    = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
puntaje   = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
intentos  = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico  = ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
indices   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
df = pd.DataFrame(data=jugadores, index=indices)
print(f"df:\n{df}")
print("*"*100)
ww = df.dropna()
ww = ww.plot(kind='line', y='puntaje', color='red')
# ~ ww = df.dropna().plot(kind='line', y='puntaje', color='red')
plt.show(block=False)
plt.pause(3)
plt.close()
# ~ pausa()
limpiar()
#######################################################################################################
print(f'''
● Crear un gráfico de barras a partir de un objeto `DataFrame`.
''')
nombre    = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
puntaje   = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
intentos  = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico  = ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
indices   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
df = pd.DataFrame(data=jugadores, index=indices)
print(f"df:\n{df}")
print("*"*100)
ww = df.groupby('califico')['califico'].count().plot(kind='bar', color=['red','blue'])
plt.show(block=False)
plt.pause(3)
plt.close()
# ~ pausa()
limpiar()
#######################################################################################################
print(f'''
● Graficar múltiples curvas con los datos de un `DataFrame`.
''')
datos = {'dueño_mascota': ['Anacleto', 'Beba', 'Cristiano', 'Anatolio', 'Peter'],
         'gatos':         [         2,      3,           2,          0,       1],
         'perros':        [         1,      2,           0,          2,       3]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print(f"df:\n{df}")
print("*"*100)
ww = df.plot(x='dueño_mascota')
plt.show(block=False)
plt.pause(3)
plt.close()
# ~ pausa()
limpiar()

#######################################################################################################
print(f'''
● Crear un gráfico de barras a partir de un objeto `DataFrame`.
''')
def Solución():
    pass

indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print(f"df.loc['c']=\n{df.loc['c']}")
print(f"{type(df.loc['c'])=}")
print("*"*100)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Obtener los nombres de las filas y las columnas de un '`DataFrame`'.
''')
def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 5], 
         'Y': [5, 4, 3, 2, 1], 
         'Z': [2, 3, 5, 7,11]}
df = pd.DataFrame(data=datos)
print(f"{df.index=}")
print(f"{df.columns=}")
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print(f"{df.index=}")
print(f"{df.columns=}")
print("*"*100)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Mostrar un reporte con la información básica de un objeto '`DataFrame`'.
''')
def Solución():
    pass
lenguajes    = ['Python', 'Java', 'C#', 'JavaScript', 'C++', 'PHP']
año_creacion = [1990, 1995, 2013, 1995, 1985, 1995]
interpretado = [True, False, False, True, False, True]
extension    = ['.py', '.java', '.cs', '.js', '.cpp', '.php']
indices      = ['a', 'b', 'c', 'd', 'e', 'f']
datos        = {'lenguaje': lenguajes, 'año_creacion': año_creacion, 'interpretado': interpretado, 'extension': extension}
df = pd.DataFrame(data=datos, index=indices)
print(f"df={df}")
print(f"{df.columns=}")
print(f"{df.index=}")
print(f"df.info:{df.info}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.query("año_creacion < 2000 & interpretado == True " )
print("""df.query("' & puntaje == True " )=\n""",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.query("año_creacion < 2000 & extension[1] != 'j' ").groupby('interpretado')
for filtro,grupo in ww:
    print (filtro,grupo)
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
# ~ Ejercicios de la librería Matplotlib
# ~ Ejercicio 1
# ~ Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.


# ~ Ejercicio 2
# ~ Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso y una cadena con el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.


# ~ Ejercicio 3
# ~ Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener el título “Distribución de notas”.


# ~ Ejercicio 4
# ~ Escribir una función que reciba una serie de Pandas con el número de ventas de un producto durante los meses de un trimestre y un título y cree un diagrama de sectores con las ventas en formato png con el titulo dado. El diagrama debe guardarse en un fichero con formato png y el título dado.


# ~ Ejercicio 5
# ~ Escribir una función que reciba una serie de Pandas con el número de ventas de un producto por años y una cadena con el tipo de gráfico a generar (lineas, barras, sectores, areas) y devuelva un diagrama del tipo indicado con la evolución de las ventas por años y con el título “Evolución del número de ventas”.


# ~ Ejercicio 6
# ~ Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa por meses y devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos. El diagrama debe tener una leyenda identificando la línea de los ingresos y la de los gastos, un título con el nombre “Evolución de ingresos y gastos” y el eje y debe empezar en 0.


# ~ Ejercicio 7
# ~ El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.


# ~ Ejercicio 8
# ~ El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

# ~ Diagrama de sectores con los fallecidos y supervivientes.
# ~ Histograma con las edades.
# ~ Diagrama de barras con el número de personas en cada clase.
# ~ Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
# ~ Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
