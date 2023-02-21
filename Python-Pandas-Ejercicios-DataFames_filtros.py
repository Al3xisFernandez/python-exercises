from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
"""
def hechos():
    pass#,inplace=True
    print(f'''  
Pandas es una biblioteca de código abierto en Python que se utiliza para análisis y manipulación de datos. Es una herramienta muy útil para trabajar con datos de diferentes tipos y formas, como tablas, series de tiempo, datos faltantes y mucho más.

Si ya estás familiarizado con los conceptos básicos de pandas, es posible que desees explorar algunas de las funcionalidades más avanzadas de la biblioteca. Esto puede incluir cosas como la manipulación de datos faltantes, la agregación y el resumen de datos, el trabajo con fechas y horas, y la visualización de datos.

A continuación te presentamos algunos ejemplos de uso avanzado de pandas:

Trabajo con datos faltantes: pandas proporciona herramientas poderosas para manipular y tratar los datos faltantes en un conjunto de datos. Por ejemplo, puedes utilizar el método dropna() para eliminar filas o columnas que contengan valores faltantes, o utilizar el método fillna() para reemplazar los valores faltantes con un valor específico.

Agregación y resumen de datos: pandas te permite agregar y resumir tus datos de diferentes maneras. Por ejemplo, puedes utilizar el método groupby() para agrupar tus datos por una o más columnas, y luego aplicar una función de agregación como mean(), sum() o count() a cada grupo.

Trabajo con fechas y horas: pandas tiene una capacidad incorporada para trabajar con fechas y horas. Por ejemplo, puedes utilizar el método to_datetime() para convertir una columna de cadenas de texto en una columna de objetos datetime, que luego puedes utilizar para extraer información como el año, el mes o el día de una fecha específica.

Visualización de datos: pandas se integra con la biblioteca de visualización de datos matplotlib, lo que te permite crear gráficos y visualizaciones a partir de tus datos de man


A continuación, te presentamos algunos ejemplos de uso avanzado de pandas que pueden servir como punto de partida para seguir explorando la biblioteca:

Manipulación de datos faltantes: en pandas, es posible trabajar con datos faltantes de diferentes maneras, como rellenarlos con un valor específico, eliminarlos o interpolarlos utilizando diferentes métodos. Por ejemplo, podrías utilizar el método fillna para rellenar los valores faltantes en una columna con un valor específico, o el método dropna para eliminar las filas que contienen valores faltantes.
Copy code
import pandas as pd

# Carga un conjunto de datos en un DataFrame de pandas
df = pd.read_csv("data.csv")

# Rellena los valores faltantes en la columna "col" con el valor 0
df["col"].fillna(0, inplace=True)

# Elimina las filas que contienen valores faltantes en cualquier columna
df.dropna(inplace=True)


    ''')
def Solución():
    pass
#######################################################################################################
import pandas as pd

# Importar una base de datos en un DataFrame
df = pd.read_csv('mi_base_de_datos.csv')
Seleccionar una columna de un DataFrame:
Copy code
# Seleccionar la columna 'nombre' del DataFrame
nombres = df['nombre']
Filtrar un DataFrame por un valor en una columna:
Copy code
# Filtrar el DataFrame por registros cuyo valor en la columna 'edad' sea mayor o igual a 18
mayores_de_edad = df[df['edad'] >= 18]
Agrupar un DataFrame por valores de una columna y calcular una agregación:
Copy code
# Agrupar el DataFrame por valores de la columna 'genero' y calcular la media de la columna 'altura' para cada grupo
promedio_altura_por_genero = df.groupby('genero')['altura'].mean()

    #######################################################################################################
    print(f'''
    ● Genera una consulta con la funciones df.filter(). 
    Esto permite al usuario realizar consultas más avanzadas y complicadas con filtros en el DataFrame. 
    Estas son abstracciones de nivel superior a df.loc 
    ''')
    def Solución():
    pass
    nombre = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print("*"*54)
    print("*",'filter'.center(50),"*")#                              filter
    print("*"*54)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.filter(items=["nombre","califico"])
    print(f"df.filter(items=['nombre','califico'])=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.filter(items=["nombre","califico"]).groupby('califico')
    for filtro,grupo in ww:
        print (filtro,grupo)
    print("*"*50)
    # We can specify the regex literal under regex in the function
    # ~ df.filter(regex="^C")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Genera una consulta con la funciones  df.query() con mas de un filtro. 
    Esto permite al usuario realizar consultas más avanzadas y complicadas con multiples filtros en el DataFrame. 
    Estas son abstracciones de nivel superior a df.loc 
    ''')
    def Solución():
    pass
    nombre = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print("*"*54)
    print("*",'query'.center(50),"*")#                              guery
    print("*"*54)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.query("califico=='Sí' & puntaje>10 & intentos <=2" )
    print('''df.query("califico=='Sí' & puntaje>10 & intentos <=2" )=\n''',ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.query("califico=='Sí' & puntaje>10 & intentos <=2").groupby('califico')
    for filtro,grupo in ww:
        print (filtro,grupo)
        


    # Seleccionar filas que cumplan cierta condición
    filtro = df['columna'] > valor
    seleccion = df[filtro]

    # Filtrar filas basándose en varias condiciones
    filtro_multiple = (df['columna_1'] > valor_1) & (df['columna_2'] == valor_2)
    seleccion = df[filtro_multiple]
     
        
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
import pandas as pd

# leer el conjunto de datos en un dataframe de pandas
df = pd.read_csv('data.csv')

# filtrar el dataframe para incluir solo filas que cumplan ciertas condiciones
df = df[df['column_name'] > some_value]

# agrupar los datos por una columna y calcular una agregación para cada grupo
df = df.groupby('column_name')['other_column_name'].mean()

# ordenar el dataframe por una columna en orden ascendente o descendente
df = df.sort_values('column_name', ascending=False)

#######################################################################################################
import pandas as pd

# leer el conjunto de datos en un dataframe de pandas
df = pd.read_csv('data.csv')

# filtrar el dataframe para incluir solo filas que cumplan ciertas condiciones
df = df[df['column_1'].isin(some_values)]
df = df[df['column_2'].notnull()]

# agrupar los datos por varias columnas y calcular una agregación para cada grupo
df = df.groupby(['column_1', 'column_2'])['column_3'].mean()

# aplicar una función a cada fila del dataframe
def some_function(row):
    return row['column_1'] + row['column_2']

df['new_column'] = df.apply(some_function, axis=1)

# realizar una unión entre dos dataframes
df = pd.merge(df1, df2, on='common_column')

# escribir el data
import pandas as pd

# Crear un DataFrame con valores faltantes
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [None, 5, 6, 7]})
print(df)

# Rellenar los valores faltantes con 0
df.fillna(0, inplace=True)
print(df)


print(f'''
● 
''')

def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)

#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
"""
#######################################################################################################
def yahechos():
    #------------------------------------------------------------------------------------------------------
# ~ print("*"*50)
# ~ pausa()
# ~ limpiar()
# ~ Filtrar por columna
# ~ Podemos seleccionar toda una columna. Para esto únicamente debemos incluir entre corchetes el nombre de la columna a seleccionar.

# ~ print (df["county"])
# ~ 1
# ~ print (df["county"])
# ~ Pero si deseamos unas cuantas filas únicamente, podemos especificar el rango:

# ~ print (df["county"][5:10]) # imprime de la linea 5 a la 10
# ~ print (df["county"][:10]) # imprime  las primeras 10
# ~ print (df["county"][-5:]) # imprime las últimas 5.
# ~ 1
# ~ 2
# ~ 3
# ~ print (df["county"][5:10]) # imprime de la linea 5 a la 10
# ~ print (df["county"][:10]) # imprime  las primeras 10
# ~ print (df["county"][-5:]) # imprime las últimas 5.
# ~ Nota: podemos escribir directamente el nombre de la columna sin los corchetes. La primera de las líneas de código anteriores, quedaría así:

# ~ print (df.county[5:10])
# ~ 1
# ~ print (df.county[5:10])
# ~ Para los siguientes ejemplos haremos uso de un dataframe llamado df3,  que contiene las columnas “condado”, “candidato”, “partido” y “votos”.

# ~ df3 = df[["county", "candidate", "party", "votes"]]
# ~ 1
# ~ df3 = df[["county", "candidate", "party", "votes"]]
# ~ Filtrar con condiciones
# ~ Para filtrar con condiciones, debemos escribir la condición dentro de corchetes. Por ejemplo, si deseamos mostrar a los que tienen más de 200 mil votos en un condado, podemos escribir:

# ~ print (df3[df3.votes>200000])
# ~ 1
# ~ print (df3[df3.votes>200000])
# ~ Lo anterior nos crea una matriz de valores booleanos True o False, de acuerdo a la condición expresada (df3.votes>200000). Ésta matriz es pasada al dataframe df3.

# ~ Filtrar con dos condiciones
# ~ Si tenemos dos condiciones a cumplir, cada condición la ponemos dentro de paréntesis y las unimos usando un operador lógico (&, |). En el siguiente ejemplo deseamos mostrar los votos obtenidos por el partido demócrata en el condado de Manhattan.

# ~ print (df3[(df3.county=='Manhattan') & (df.party=='Democrat')])
# ~ 1
# ~ print (df3[(df3.county=='Manhattan') & (df.party=='Democrat')])
# ~ Uso de Query con Pandas en Python
# ~ Vamos a realizar la misma consulta (mostrar los votos obtenidos por el partido demócrata en el condado de Manhattan) pero usando el método query.

# ~ print (df3.query("county=='Manhattan' and party=='Democrat'"))
# ~ 1
# ~ print (df3.query("county=='Manhattan' and party=='Democrat'"))
# ~ La diferencia radica en que solo se especifica el nombre de la columna y todo va entre comillas como si se tratara de una cadena.

# ~ Manejo de variables y uso de query con Pandas
# ~ Podemos incluir una variable dentro del query. En el ejemplo anterior deseamos que Manhattan esté dentro de una variable llamada “condado”. Entonces el query quedaría así:

# ~ condado = 'Manhattan'
# ~ print (df3.query("county==@condado and party=='Democrat'"))
# ~ 1
# ~ 2
# ~ condado = 'Manhattan'
# ~ print (df3.query("county==@condado and party=='Democrat'"))
# ~ isin y uso de query con pandas
# ~ Isin nos permite comprobar si un valor está dentro de una lista. Por ejemplo, si la consulta fuese: “Mostrar los votos de los condados de Autauga y Baldwin”, si lo quisiéramos hacer con dos condiciones quedaría así:

# ~ #1 Usando matriz de valores booleanos
# ~ print (df3[(df3.county=='Autauga') | (df3.county=='Baldwin')])


# ~ #2 Usando query
# ~ print (df3.query("county=='Autauga' or county=='Baldwin'"))
# ~ 1
# ~ 2
# ~ 3
# ~ 4
# ~ 5
# ~ 6
# ~ #1 Usando matriz de valores booleanos
# ~ print (df3[(df3.county=='Autauga') | (df3.county=='Baldwin')])
 
 
# ~ #2 Usando query
# ~ print (df3.query("county=='Autauga' or county=='Baldwin'"))
# ~ Observamos que se realizan dos consultas, una por cada valor buscado. Pero como es la misma columna, podemos utilizar el método isin:

# ~ print (df3[(df3.county.isin(["Autauga","Baldwin"]))])
# ~ 1
# ~ print (df3[(df3.county.isin(["Autauga","Baldwin"]))])
# ~ Y obtendremos los mismos resultados.

# ~ Contains
# ~ Si la consulta requiere que comprobemos solo parte del valor del dato, podemos utilizar contains en el caso de las cadenas de caracteres. Por ejemplo, si deseamos mostrar los votos de los condados que contengan la palabra  ‘Saint’, podemos hacer lo siguiente:

# ~ print (df3[df3.county.str.contains('Saint')])
# ~ 1
# ~ print (df3[df3.county.str.contains('Saint')])
# ~ Lo que nos devolverá valores correspondientes a Saint Francisc, Saint Agatha, y Saint Laurence.

# ~ Ordenamiento en Pandas
# ~ ¿Quiénes fueron los 3 candidatos que más votos obtuvieron  en un condado? Para contestar ésta pregunta debemos realizar una operación de ordenamiento. De esa forma podemos extraer los 3 primeros resultados que nos arroje Pandas.

# ~ Código:

# ~ dfordenado = df3.sort_values(by="votes", ascending=False)
# ~ print ("Ordenados por votos de mayor a menor")
# ~ print (dfordenado.head(3))
# ~ 1
# ~ 2
# ~ 3
# ~ dfordenado = df3.sort_values(by="votes", ascending=False)
# ~ print ("Ordenados por votos de mayor a menor")
# ~ print (dfordenado.head(3))
# ~ Le estamos diciendo que al dataframe de nombre df3, lo ordene (sort_values) con base en la columna “votes“, en forma descendente (ascending=False). Como solo deseamos 3, utilizamos head(3) para obtener solo los tres primeros.

# ~ Agrupamiento en Pandas
# ~ El agrupamiento nos permitirá realizar operaciones (como contar o sumar) sobre un subgrupo dentro de un dataframe. Por ejemplo, si deseamos el  total de votos por estado y por partido, tendríamos que agrupar todos los votos de un estado, y después agrupar todos los votos de cada partido. Hacerlo con Pandas es muy sencillo:

# ~ #print ("total de votos por estado y por partido")
# ~ #print (df.groupby(["state", "party"]).sum())
# ~ 1
# ~ 2
# ~ #print ("total de votos por estado y por partido")
# ~ #print (df.groupby(["state", "party"]).sum())
# ~ Ésta operación nos agrupa todos los registros, primero por estado y luego por partido y realiza la suma de las columnas numéricas, si solo queremos  la de votos deberíamos especificarla: df.groupby([“state”, “party”])[“votes”].sum()

# ~ Aplicar una función a una columna en Pandas
# ~ Código:

# ~ def miles(x):
	# ~ return x/1000

# ~ df3["votesm"] = df3["votes"].apply(miles)
# ~ print (df3.head())
# ~ 1
# ~ 2
# ~ 3
# ~ 4
# ~ 5
# ~ def miles(x):
	# ~ return x/1000
 
# ~ df3["votesm"] = df3["votes"].apply(miles)
# ~ print (df3.head())
# ~ Primero estamos creando una función llamada miles que recibe un valor (x), y lo regresa dividido entre 1000. (return x/1000).

# ~ Luego creamos una columna llamada “votesm” y le asignamos el resultado de aplicar a cada valor de “votes” la función miles.
print('''
Los DataFrames son la estructura mas importante en pandas y están directamente inspirados en el lenguaje de programación R. 
Se puede pensar en un DataFrame como un conjunto de Series reunidas que comparten el mismo índice. 
En los DataFrame tenemos la opción de especificar tanto el index (el nombre de las filas) como columns (el nombre de las columnas).
''')
# Importar la funcion de NumPy para crear arreglos de numeros enteros
from numpy.random import randn
np.random.seed(101) # Inicializar el generador aleatorio 

df = pd.DataFrame(randn(5,4),
                  index='A B C D E'.split(),
                  columns='W X Y Z'.split())
print (f"df=\n{df}")
'''
Descripcion general del dataframe
    Numero de Filas y Columnas
    
    df.shape # retorna un Tuple asi: (filas, col)
'''
print (f"df.shape=\n{df.shape}")
'''
Informacion General de los datos:
    * Informacion general de los datos de cada columna.
    * Indica el numero de filas del dataset.
    * Muestra el numero de datos No Nulos por columna (valores validos).
    * Tipo de dato de cada columna.
    * Tamaño total del dataset.

        df.info()
'''
print (f"df.info()=\n{df.info()}")

Ejercicio 1
Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.


Ejercicio 2
Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.


Ejercicio 3
Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.


Ejercicio 4
Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

Mes	Ventas	Gastos
Enero	30500	22000
Febrero	35600	23400
Marzo	28300	18100
Abril	33900	20700

Ejercicio 5
Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.


Ejercicio 6
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.


Ejercicio 7
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

Generar un DataFrame con los datos del fichero.
Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
Mostrar por pantalla los datos del pasajero con identificador 148.
Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.
Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.

Ejercicio 8
Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

Generar un DataFrame con los datos de los cuatro ficheros.
Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
Mostrar un resumen descriptivo para cada contaminante por distritos.
Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.

