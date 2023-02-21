from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
def hechos():
    pass#,inplace=True
  
    limpiar()

#######################################################################################################
print(f'''
●   Genera un script que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie 
    con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 5%.
''')
def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
    while True:
        try:
            inicio = int(input('Introduce el año inicial: '))
            fin = int(input('Introduce el año final: '))
            if inicio>fin or fin-inicio>=20:
                print ("maximo 20 años")
                raise Exception("Sorry,+20 años !!! mucho trabajo, estoy vago")
            break
        except Exception as e:
            print (f"{e}")


    ventas = {}
    for i in range(inicio, fin+1):
        ventas[i] = float(input(f'Introduce las ventas del año {i} : '))
    ventas = pd.Series(ventas)
    print('Ventas\n', ventas)
    print('Ventas con descuento\n', ventas/1.05)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################

print(f'''
    ●  Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie 
    con la nota mínima, la máxima, media y la desviación típica.
''')
def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
    def estadistica_notas(notas):
        notas = pd.Series(notas)
        estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación estandar'])
        # ~ estadisticas = notas.describe()
        return estadisticas

    notas = {'Humberto':9.5, 'Anatolio':7.5, 'Tito':3.5, 'Tato': 8.5, 'Pepe': 6.5}
    print(estadistica_notas(notas))
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################

print(f'''
●   Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie 
    1)  con las notas de los alumnos aprobados (>=7) ordenadas de  menor a mayor.
    2)  con las notas de los alumnos que deben recuperar (<7) ordenadas de mayor a menor.
''')
def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
    def aprobados(notas):
        notas = pd.Series(notas)
        return notas[notas >= 7].sort_values(ascending=True)
    def recuperan(notas):
        notas = pd.Series(notas)
        return notas[notas < 7].sort_values(ascending=False)

    notas = {'Humberto':9.5, 'Anatolio':7.5, 'Tito':3.5, 'Tato': 8.5, 'Pepe': 6.5}
    print(f"aprobados=\n{aprobados(notas)}")
    print(f"recuperan=\n{recuperan(notas)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################
print(f'''
●  Escribir programa para una heladeria que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
    Que meses hay ganancias y que meses perdidas

                        Mes	        Ventas  Gastos
                        Enero	    42500   35000
                        Febrero	    37500   30000
                        Marzo	    35000   25000
                        Abril	    32500   22500
                        Marzo       30000   20000
                        Abril       25000   20000
                        Mayo        15000   18000
                        Junio       16000   17000
                        Julio       15000   16000
                        Agosto      20000   17000
                        Septiembre  25000   19000
                        octubre     30000   20000
                        Noviembre   35000   24000
                        Diciembre   40000   28000

''')

def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
    def resultados():
        df = pd.DataFrame(data=dic)
        print(f"df=\n{df}")
        df=df.T
        ganancias=df[df.Ventas >= df.Gastos]
        perdidas=df[df.Ventas < df.Gastos]
        return [ganancias,perdidas]
    def resultados2():
        df = pd.DataFrame(data=dic)
        print(f"df=\n{df}")
        df=df.T
        df["resultados"]=df.Ventas - df.Gastos
        ganancias=df[df.resultados >=0]
        perdidas= df[df.resultados < 0]
        return [ganancias,perdidas]


    # ~ def resultados3():
        # ~ df = pd.DataFrame(data=dic)
        # ~ print(f"df=\n{df}")
        # ~ df=df.T
        # ~ df['resultados'] = df.Ventas - df.Gastos
        # ~ return df.loc[['Enero','Diciembre'],'resultados'].sum()

        
    dic={ 
    'Enero'      :{'Ventas': 42500,'Gastos': 35000},
    'Febrero'    :{'Ventas': 37500,'Gastos': 30000},
    'Marzo'	     :{'Ventas': 35000,'Gastos': 25000},
    'Abril'	     :{'Ventas': 32500,'Gastos': 22500},
    'Marzo'      :{'Ventas': 30000,'Gastos': 20000},
    'Abril'      :{'Ventas': 25000,'Gastos': 20000},
    'Mayo'       :{'Ventas': 15000,'Gastos': 18000},
    'Junio'      :{'Ventas': 16000,'Gastos': 17000},
    'Julio'      :{'Ventas': 15000,'Gastos': 16000},
    'Agosto'     :{'Ventas': 17000,'Gastos': 17000},
    'Septiembre' :{'Ventas': 25000,'Gastos': 19000},
    'octubre'    :{'Ventas': 30000,'Gastos': 20000},
    'Noviembre'  :{'Ventas': 35000,'Gastos': 24000},
    'Diciembre'  :{'Ventas': 40000,'Gastos': 28000}}
    # ~ meses=[ 'Enero',
            # ~ 'Febrero',
            # ~ 'Marzo' ,
            # ~ 'Abril',
            # ~ 'Marzo',
            # ~ 'Abril',
            # ~ 'Mayo',
            # ~ 'Junio',
            # ~ 'Julio',
            # ~ 'Agosto',
            # ~ 'Septiembre',
            # ~ 'octubre',
            # ~ 'Noviembre',
            # ~ 'Diciembre']
    # ~ Ventas=[ 42500, 37500, 35000,32500,30000,25000,15000, 16000, 15000, 17000, 25000, 30000, 35000, 40000]
    # ~ Gastos=[ 350030000, 25000, 22500,20000,20000,18000,17000, 16000, 17000, 19000, 20000, 24000, 28000]
    gan,per=resultados()
    print(f"hubo ganancias en los siguientes meses:\n{gan}")
    print(f"hubo perdidass en los siguientes meses:\n{per}")
    print("*"*50)
    gan,per=resultados2()
    print(f"hubo ganancias en los siguientes meses:\n{gan}")
    print(f"hubo perdidass en los siguientes meses:\n{per}")
    print("*"*50)

    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()

    #######################################################################################################
print(f'''
●   El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
        nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
        Máximo (precio máximo de la acción durante la jornada), 
        Mínimo (precio mínimo de la acción durante la jornada), 
        volumen (Volumen al cierre de bolsa), 
        Efectivo (capitalización al cierre en miles de euros). 
        Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y 
        devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.
''')
def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
    def resumen_cotizaciones(fichero):
        df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
        return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])
        # ~ return pd.DataFrame(df.describe())
    r=resumen_cotizaciones('cotizacion_IBEX.csv')
    print(f"{r}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################
print(f'''
●  El fichero titanic.csv contiene información sobre los pasajeros del Titanic. 
Genera un script con los siguientes requisitos:

Generar un DataFrame con los datos del fichero.
Mostrar por pantalla las dimensiones del DataFrame, 
    el número de datos que contiene, 
    los nombres de sus columnas y filas, 
    los tipos de datos de las columnas, 
    las 10 primeras filas y 
    las 10 últimas filas
Mostrar por pantalla los datos del pasajero con identificador 148.
Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.
Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
''')
def Solución():
    pass
    print("""
    Mostrar por pantalla las dimensiones del DataFrame, 
        el número de datos que contiene, 
        los nombres de sus columnas y filas, 
        los tipos de datos de las columnas, 
        las 10 primeras filas y 
        las 10 últimas fila""")
    df_titanic = pd.read_csv('titanic.csv')
    print('Dimensiones:', df_titanic.shape)
    print('Número de elemntos:', df_titanic.size)
    print('Nombres de columnas:', df_titanic.columns)
    print('Nombres de filas:', df_titanic.index)
    print('Tipos de datos:\n', df_titanic.dtypes)
    print('Primeras 10 filas:\n', df_titanic.head(10))
    print('Últimas 10 filas:\n', df_titanic.tail(10))
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla los datos del pasajero con identificador 148")
    print(df_titanic.loc[148])
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(df_titanic[df_titanic.Name=='Navratil, Mr. Michel ("Louis M Hoffman")'])
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla las filas pares del DataFrame.")
    # ~ print(df_titanic[df_titanic.PassengerId %2==0
    print(df_titanic.iloc[range(0,df_titanic.shape[0],2)])
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.")
    print(df_titanic[df_titanic.Pclass==1].Name.sort_values(ascending=True))
    print(df_titanic[df_titanic["Pclass"]==1]['Name'].sort_values())
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.")
    print(df_titanic['Survived'].value_counts()/df_titanic['Survived'].count() * 100)
    #    o
    print(df_titanic['Survived'].value_counts(normalize=True) * 100)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.")
    print(df_titanic.groupby('Pclass')['Survived'].value_counts()/df_titanic['Survived'].count() )
    #    o
    print(df_titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Eliminar del DataFrame los pasajeros con edad desconocida.")
    print(df_titanic.dropna(subset=['Age']))
    #    o
    print(df_titanic[df_titanic['Age'].notna()])
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.")
    print(df_titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.")
    df_titanic["mayor"]=df_titanic['Age'] >= 18
    print(df_titanic)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print(" Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.")
    print(df_titanic.groupby(['Pclass', 'mayor'])['Survived'].value_counts(normalize = True) * 100)
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################
print(f'''
●  Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. 
Genera un script con los siguientes requisitos:

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


''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
print("Generar un DataFrame con los datos de los cuatro ficheros.")
emisiones_2016 = pd.read_csv('emisiones-2016.csv', sep = ';')
emisiones_2017 = pd.read_csv('emisiones-2017.csv', sep = ';')
emisiones_2018 = pd.read_csv('emisiones-2018.csv', sep = ';')
emisiones_2019 = pd.read_csv('emisiones-2019.csv', sep = ';')
emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])
print (f"df=\n{emisiones}")
#------------------------------------------------------------------------------------------------------
print("Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.") 
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
# ~ columnas.extend([col for col in emisiones if col.startswith('D')])
columnas.extend([col for col in emisiones if col[:1]=='D'])
emisiones2 = emisiones[columnas]
print (f"df=\n{emisiones2}")
#------------------------------------------------------------------------------------------------------
print("Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.") 
'''
Para facilitar el análisis de los datos en la tabla, podemos remodelar los datos en una forma más amigable para la computadora usando Pandas en Python. 
    Pandas.melt() es una de las funciones para hacerlo.
    Pandas.melt() desvía un DataFrame de formato ancho a formato largo.
    La función melt() es útil para enviar mensajes a un DataFrame en un formato en el que una o más columnas son variables de identificación, 
    mientras que todas las demás columnas, consideradas variables medidas, no están vinculadas al eje de la fila, 
    dejando solo dos columnas sin identificador, variable y valor.
'''
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
emisiones2 = emisiones.melt(id_vars=columnas, var_name='DIA', value_name='VALOR')
print (f"df=\n{emisiones2.head(100)}")
# ~ emisiones2 = emisiones[sum([col for col in emisiones if col[:1]=='D'])].cumsum()
# ~ emisiones['suma'] = emisiones.apply(lambda :col for col in emisiones if col[:1]=='D').sum()
# ~ print (f"df=\n{emisiones2}")
#------------------------------------------------------------------------------------------------------

print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  ''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
