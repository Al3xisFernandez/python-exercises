from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
def hechos():
    pass#,inplace=True
    print('''  
    ● Crear un objeto de la clase 'DataFrame'.
    ● Especificar nombres de índices arbitrarios a un objeto 'DataFrame'.
    ● Obtener los nombres de las filas y las columnas de un 'DataFrame'.
    ● Obtener los tipos de datos de las columnas de un 'DataFrame'.
    ● Mostrar un reporte con la información básica de un objeto 'DataFrame'.
    ● Obtener las columnas de un determinado tipo de dato con 'select_dtypes'.
    
    
    Parámetro	Descripción
            datos	        Los datos toman varias formas como ndarray, series, mapas, listas, dict, constantes y también otro DataFrame
            artículos	    eje = 0
            eje principal	eje = 1
            eje menor	    eje = 2
            dtype	        Un tipo de datos de cada columna.
            Copiar	        Copiar datos Predeterminado, falso
    Series.sum          Devuelve la suma dela serie (columna).
    Series.min          Devuelve lo mínimo.
    Series.max          Devuelve el máximo.
    Series.idxmin       Devuelve el índice del mínimo.
    Series.idxmax       Devuelve el índice del máximo.
    DataFrame.sum       Devuelve la suma sobre el eje solicitado.
    DataFrame.min       Devuelve el mínimo sobre el eje solicitado.
    DataFrame.max       Devuelve el máximo sobre el eje solicitado.
    DataFrame.idxmin    Devuelve el índice del mínimo sobre el eje solicitado.
    DataFrame.idxmax    Devuelve el índice del máximo sobre el eje solicitado.
    DataFrame.add(valor)   df + valor.
    DataFrame.sub(valor)   df - valor. 
    DataFrame.mul(valor)   df * valor.
    DataFrame.div(valor)   df / valor.
    
    
    DataFrame.sum(valor)   df   axis 0 o 'índice'
    DataFrame.agg(valor)   df   axis 1 o 'columnas'
                
pandas.DataFrame.div(otro, eje='columnas', nivel=Ninguno, fill_value=Ninguno)

otro: escalar, secuencia, serie o marco de datos : este parámetro consiste en cualquier estructura de datos de uno o varios elementos, u objeto similar a una lista.
eje: {0 o 'índice', 1 o 'columnas'} : se utiliza para decidir el eje en el que se aplica la operación.
nivel: int o etiqueta : el parámetro de nivel se usa para transmitir a través de un nivel y hacer coincidir los valores de índice en el nivel de índice múltiple pasado.
fill_value: flotante o Ninguno, predeterminado Ninguno : siempre que los marcos de datos tengan valores faltantes, para completar los valores faltantes existentes (NaN), podemos usar el parámetro fill_value.
    ''')
def Solución():
    pass
#######################################################################################################

print(f'''
● Crear un objeto de la clase 'DataFrame'.
''')
## Solución.
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
print("-"*10,":)\n")
pausa()
#######################################################################################################
#------------------------------------------------------------------------------------------------------
ww = df + 1
print(f"df + 1=\n{ww}")
ww = df.add( 10 )
print(f"df.add( 10 )=\n{ww}")
print("-"*10,":)\n")
ww=df.add([2, 4, 6, 8, 10], axis='index')#axis=0)
print(f"df.add([2, 4, 6, 8, 10], axis='index')=\n{ww}")
print("-"*10,":)\n")
ww=df.add([6, 3, 9], axis='columns')#axis=1)
print(f"df.add([6, 3 ,9], axis='columns')=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww = df / 5
print(f"df / 5=\n{ww}")
ww = df.div(10)
print(f"df.div(10)=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww = df.rdiv(10)
print(f"df.rdiv(10)=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww = df - [1, 2, 5]
print(f"df - [1, 2 ,5]=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww=df.sub([2, 4, 6, 8, 10], axis='index')
print(f"df.sub([2, 4, 6, 8, 10], axis='index')=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww=df.sub([6, 3, 9], axis='columns')
print(f"df.sub([6, 3 ,9], axis='columns')=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
# ~ ww=df.mul({'Z':3,'Y': 5, 'Z': 2})
# ~ print(f"df - [1, 2]=\n{ww}")
# ~ pausa()
# ~ #------------------------------------------------------------------------------------------------------
datos={'angles': [0, 3, 4],
               'degrees': [360, 180, 360]}
indices=['circle', 'triangle', 'rectangle']
df = pd.DataFrame(data=datos, index=indices)
print(f"df=\n{df}")
ww=df.sub(pd.Series([10, 25, 50], index=['circle', 'triangle', 'rectangle']), axis='index')
print(f"df.sub(pd.Series([10, 25, 50], index=['circle', 'triangle', 'rectangle']), axis='index')=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww=df.mul({'angles': 10, 'degrees': 2})
print("df.mul({'angles': 10, 'degrees': 2})=\n",ww)
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
ww=df.mul({'circle': 0, 'triangle': 2, 'rectangle': 3}, axis='index')
print("df.mul({'circle': 0, 'triangle': 2, 'rectangle': 3}, axis='index')=\n",ww)
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
other = pd.DataFrame({'angles': [0, 3, 4]},
                 index=['circle', 'triangle', 'rectangle'])
ww=df.mul(other, fill_value=0)
print(f"df.mul(other, fill_value=0)=\n{ww}")
print("-"*10,":)\n")
pausa()
#------------------------------------------------------------------------------------------------------
df_multindex = pd.DataFrame({'angles': [0, 3, 4, 4, 5, 6],
                         'degrees': [360, 180, 360, 360, 540, 720]},
                        index=[['A', 'A', 'A', 'B', 'B', 'B'],
                               ['circle', 'triangle', 'rectangle',
                                'square', 'pentagon', 'hexagon']])
ww=df.div(df_multindex, level=1, fill_value=0)
print(f"df.mul(other, fill_value=0)=\n{ww}")
print("-"*10,":)\n")
pausa()


#------------------------------------------------------------------------------------------------------
print(f"df.mul(other, fill_value=0)=\n{ww}")
print("-"*10,":)\n")
pausa()
#######################################################################################################
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
print("-"*10,":)\n")
ww = df.agg("mean", axis="index")# axis=0)
print("df.agg('mean', axis='index')=\n",ww)
print("-"*10,":)\n")
ww = df.agg("mean", axis="columns")# axis=1)
print("df.agg('mean', axis='columns')=\n",ww)
print("-"*10,":)\n")
pausa()
#######################################################################################################
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
print("-"*10,":)\n")
ww = df.agg("mean", axis="index")# axis=0)
print("df.agg('mean', axis='index')",ww)
print("-"*10,":)\n")
ww = df.agg("mean", axis="columns")# axis=1)
print("df.agg('mean', axis='columns')",ww)
print("-"*10,":)\n")
pausa()
ww = df.agg({'X' : ['sum', 'min'], 'Y' : ['mean', 'max'], 'Z':['idxmin','idxmax']})
print("df.agg({'X' : ['sum', 'min'], 'Y' : ['mean', 'max'], 'Z':['idxmin','idxmax']}=\n",ww)
