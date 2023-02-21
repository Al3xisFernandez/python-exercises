from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
def hechos():
    pass#,inplace=True
print(f'''
●  Guardar y leer un `DataFrame` en formato de 'CSV' con la funciones `to_csv` y  `read_csv`.
●  Guardar y leer un `DataFrame` en formato de serialización pickle  con las funciones `to_pickle`y `read_pickle` de Python.
●  Guardar y leer un `DataFrame` en formato de serialización  con las funciones `to_json` y `read_json` de pandas para JavaScript Object Notification.
●  Generar un `DataFrame` desde un string con formatos`.
●  Generar la representación en cadena de caracteres de un `DataFrame` con `to_string`.
●  Obtener la representación de diccionario de un objeto `DataFrame`  con las funciones `to_dict` y `from_dict`.
●  Guardar y leer un `DataFrame` en formato de 'HTML'  con las funciones `to_html` y `read_html` de pandas para navegadores de internet.
●  Guardar y leer el contenido de un `DataFrame` via portapapeles del sistema operativo con las funciones `to_clipboard` y `read_clipboard`.
●  Guardar y leer un `DataFrame` en formato de planilla de cálculo (excel/calc) con las funciones `to_excel` y `read_excel` de Microsoft.
●  Guardar y leer un `DataFrame` en formato de SQL `to_sql`  de SQLite/MySQL/SQLServer/MariaDB/etc. ver SQLAlchemy API .
●  Crea un `DataFrame` envialo a SQLite `to_sql`  SQLAlchemy API.
●  Elimina el `DataFrame` y recuperalo desde SQLite `read_sql` SQLAlchemy API.
●  Crea un `excel` desde SQLite `to_excel`.
●  Convertir una columna de tipo string - cadena de caracteres a fecha con `to_datetime`.
●  Crear un `DataFrame` a partir de arreglos *NumPy* y genera columnas e índices.
●  Crear un arreglos *NumPy* a partir de un `DataFrame`.''')
def Solución():
    pass
    #######################################################################################################
#'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']


print(f'''
● Crear un objeto de la clase '`DataFrame`'.
''')
## Solución.
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
df = pd.DataFrame(datos)
print(f"df:\n{df}")
print("*"*100)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Especificar nombres de índices arbitrarios a un objeto '`DataFrame`'.
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
● Crear un `DataFrame` a partir de listas varias.
''')
lista_col = ['X', 'Y']
lista_index = ['a', 'b']
lista_datos = [[3, 2], [7,3]] 
df = pd.DataFrame(data=lista_datos, columns = lista_col, index = lista_index) 
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de Pandas Series.
''')
series = {   'X': pd.Series([3, 2], 
                    index = ['a','b']), 
            'Y': pd.Series([7, 3], 
                    index = ['a','b'])} 
df = pd.DataFrame(data=series)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de una matriz (lista de listas) Python.
''')
def Solución():
    pass
matriz = [['X', 'Y'], [3, 2], [7, 3]]
encabezado = matriz.pop(0)
df = pd.DataFrame(data=matriz, columns=encabezado)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de un diccionario Python.
''')
def Solución():
    pass
dic = {'X':[3, 2], 'Y':[7, 3]}
df = pd.DataFrame(data=dic, index=['a','b'])
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de una lista de  diccionarios Python.
''')
def Solución():
    pass
dic = [{'X':3,'Y': 2},{'X':7, 'Y':3}]
df = pd.DataFrame(data=dic, index=['a','b'])
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()


#######################################################################################################
print("""
    'to_clipboard',     'read_clipboard',
    'to_csv',           'read_csv', 
    'to_dict',          'from_dict',  
    'to_excel',         'read_excel',
    'to_feather', 
    'to_gbq', 
    'to_hdf', 
    'to_html',          'read_html',
    'to_json',          'read_json', 
    'to_latex', 
    'to_markdown', 
    'to_numpy',         'read_numpy', 
    'to_orc', 
    'to_parquet', 
    'to_period', 
    'to_pickle',        'read_pickle', 
    'to_records', 
    'to_sql',           'read_sql',     'read_sql_query'
    'to_stata', 
    'to_string',        '', 
    'to_timestamp', 
    'to_xarray', 
    'to_xml'            
""")

#######################################################################################################
import csv
print(f'''
● Guardar y leer un `DataFrame` en formato de 'CSV' con la funciones `to_csv` y  `read_csv` puedes chequear el resultado con una planilla de calculo.
Nota: en archivos grandes debemos especificamos un parámetro llamado chunksize que restringe cuántas filas del archivo debe leer a la vez.
chunksize =1000) leemos 1000 filas a la vez, realizamos algunas tareas en ese fragmento, y pasamos a las siguientes 1000 filas.
''')

def Solución():
    pass
    #------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'CSV - (Comma Separated Values)'.center(50),"*")#                              query
print("*"*54)
print(f"df - hacia .csv=\n{df}")
df.to_csv('datos.csv')
del df
print("en la carpeta donde esta esta practica deberas encontrar `datos.csv` con fecha y hora actual ")
print("*"*50)
with open('datos.csv', 'r') as obj_csv:
    datos = csv.reader(obj_csv, delimiter=',')
    print(list(datos))
    for fila in datos:
        print(f"{fila= }")
csvReader = csv.DictReader(open("datos.csv"))
for row in csvReader:
    print(row)
print("-"*10,":)\n")
df = pd.read_csv('datos.csv', header=0)    
print(f"df - desde csv=\n{df}")  
print("-"*10,":)\n")
print(f"{'X':<5}   {'Y':^5}   {'Z':>5}\n","_"*20)
for index, row in df.iterrows():
    print(f"{row['X']:<5}   {row['Y']:^5}   {row['Z']:>5}")
print("-"*10,":)\n")
df = pd.read_csv('datos.csv', header=None, names=["X1","Y2","Z3"])    
print(f"df - desde csv=\n{df}")  
print("-"*10,":)\n")
print(f"{'X1':<5}   {'Y2':^5}   {'Z3':>5}\n","_"*20)
for index, row in df.iterrows():
    print(f"{row['X1']:<5}   {row['Y2']:^5}   {row['Z3']:>5}")        
df = pd.read_csv("datos.csv", usecols = ["X", "Z"])
print(f"df - desde csv usecols = ['X','Z'] =\n{df}") 
pausa()
limpiar()
#######################################################################################################
import pickle
print(f'''
●  Guardar y leer un `DataFrame` en formato de serialización pickle  con las funciones `to_pickle`y `read_pickle` de Python.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'pickles - (binarios)'.center(50),"*")#                              query
print("*"*54)
print(f"df - hacia pickle=\n{df}")
df.to_pickle('datos.pkl') 

del df
print("en la carpeta donde esta esta practica deberas encontrar `datos.pkl` con fecha y hora actual ")
print("*"*50)
with open('datos.pkl', 'rb') as obj_pkl:
    datos =pickle.load(obj_pkl) 
    print(f"{datos=}") 
    print("-"*10,":)\n")
    for clave,valores in datos.items():
        print(f"{clave= }:\n{valores}")
print("-"*10,":)\n")
df = pd.read_pickle('datos.pkl')    
print(f"df - desde pickle=\n{df}")    
pausa()
limpiar()
#######################################################################################################
import json
print(f'''
●  Guardar y leer un `DataFrame` en formato de serialización  con las funciones `to_json` y `read_json` de pandas para JavaScript Object Notification.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_json'.center(50),"*")
print("*"*54)
print(f"df - hacia json=\n{df}")
ww = df.to_json('datos.json')
print("en la carpeta donde esta esta practica deberas encontrar `datos.json` con fecha y hora actual.\nPuedes abrirlo en tu ide, block de notas o navegador web")
print("*"*50)
with open('datos.json', 'r') as obj_json:
    dic = json.load(obj_json)
    print(f"diccionario desde json ={dic}")
print("df.to_json()=\n",ww,f"\n.{type(ww)=}")
df = pd.read_json('datos.json')    
print(f"df - desde json=\n{df}") 
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  Generar un `DataFrame` desde un string con formatos`.
●  Generar la representación en cadena de caracteres de un `DataFrame` con `to_string`.
''')
def Solución():
    pass
import io
datos="""X\tY\tZ
1 4.4 99
2 4.5 200
3 4.7 65
4 3.2 140
"""
print ("*"*54)
print ("*", 'Por comprehension'.center(50),"*")
print ("*"*54)
df = pd.DataFrame(data =[y.split(" ")  for y in [x for x in datos.split('\n')[1:]  ][:-1]] , columns=[x for x in datos.split('\n')[0].split('\t')])
print(f"df=\n{df}")     
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_string'.center(50),"*")
print("*"*54)
print(f"df=\n{df}")
ww = df.to_string()
print("df.to_string()=\n",ww,f"\n.{type(ww)=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  Obtener la representación de diccionario de un objeto `DataFrame`  con las funciones `to_dict` y `from_dict`.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
df = pd.DataFrame.from_dict(data=datos, orient='index', columns=['a', 'b', 'c', 'e', 'f'])
print("*"*54)
print("*",'from_dict(orient="index")'.center(50),"*")
print("*"*54)
print("df=\n",df,f"\n.{type(df)=}")
print("*"*54)
print("*",'to_dict'.center(50),"*")
print("*"*54)
ww = df.to_dict()
print("df.to_dict()=\n",ww,f"\n.{type(ww)=}")
#------------------------------------------------------------------------------------------------------

datos = {'index': [('a', 'b'), ('a', 'c')],
        'columns': [('x', 1), ('y', 2)],
        'data': [[1, 3], [2, 4]],
        'index_names': ['n1', 'n2'],
        'column_names': ['z1', 'z2']}
print("*"*54)
print("*",'from_dict(orient="tight")'.center(50),"*")
print("*"*54)
df = pd.DataFrame.from_dict(data=datos, orient='tight')
print("df =\n",df,f"\n.{type(df)=}")
print("*"*54)
print("*",'to_dict'.center(50),"*")
print("*"*54)
ww = df.to_dict()
print("df.to_dict()=\n",ww,f"\n.{type(ww)=}")
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  Guardar y leer un `DataFrame` en formato de 'HTML'  con las funciones `to_html` y `read_html` de pandas para navegadores de internet.
''')
def Solución():
    pass
        
try:
    import lxml
except Exception as error_:
    import pip
    pip.main(['install', 'lxml'])
    import lxml
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_html'.center(50),"*")
print("*"*54)
print(f"df=\n{df}")
ww = df.to_html('datos.html')
print("en la carpeta donde esta esta practica deberas encontrar `datos.html` con fecha y hora actual.\nPuedes abrirlo en tu navegador web")
print("df.to_html()=\n",ww,f"\n.{type(ww)=}")
import lxml
del df
try:
    df = pd.read_html('datos.html')
    print("pd.read_html('datos.html')=\n",ww,f"\n.{type(ww)=}")
    df = pd.read_html(nombre_archivo)[0]
except:
    print ("error")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#############################################################################################################################################################################################################
print(f'''
● Guardar y leer  el contenido de un `DataFrame` via portapapeles del sistema operativo con las funciones `to_clipboard` y `read_clipboard`.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_clipboard'.center(50),"*")
print("*"*54)
print(f"df=\n{df}")
df.to_clipboard()
# ~ print(dir(df))
# ~ del df
try:
    print(f"df=\n{df}")
except Exception as E:
    print (E)
print ("""coloca ctrl+v para pegar el  `DataFrame` en cualquier aplicacion offimatica(MsOffice/Libreoffice), ide, notepad, etc.
el contenido en la aplicacion y vuelve a cortarlo y pegarlo aqui""")
#------------------------------------------------------------------------------------------------------
print("*"*50)
df = pd.read_clipboard()
print(f"df=\n{df}")
pausa()
limpiar()
#######################################################################################################
import openpyxl#pip install openpyxl
print(f'''
●  Guardar y leer un `DataFrame` en formato de planilla de cálculo (excel/calc) con las funciones `to_excel` y `read_excel` de Microsoft.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_excel'.center(50),"*")
print("*"*54)
print(f"df - hacia excel=\n{df}")
ww = df.to_excel('datos.xlsx', sheet_name='nombre_hoja_excel')
print("en la carpeta donde esta esta practica deberas encontrar `datos.xlsx` con fecha y hora actual.\nPuedes abrirlo `DataFrame` en cualquier aplicacion offimatica(MsOffice/Libreoffice).")
print("*"*50)
df = pd.read_excel('datos.xlsx')    
print("pd.read_excel('datos.xlsx')=\n",df,f"\n.{type(df)=}")
import xlrd
df2 = pd.read_excel('datos.xlsx', sheet_name='nombre_hoja_excel')
df3 = pd.read_excel('datos.xlsx', header=None, skiprows=1)
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
import sqlite3 
from sqlalchemy import create_engine
try:
    import mysql.connector
except Exception as error_:
    import pip
    pip.main(['install', 'mysql-connector-python'])
from mysql.connector import Error
from mysql.connector import errorcode
try:
    import pymysql
    import pymysql.cursors
except Exception as error_:
    import pip
    pip.main(['install', 'pymysql'])
    import pymysql
import pymysql.cursors
try:
    from sqlalchemy import create_engine
except Exception as error_:
    import pip
    pip.main(['install', 'sqlalchemy'])
    from sqlalchemy import create_engine
print(f'''
●  Guardar y leer un `DataFrame` en formato de SQL `to_sql`  de SQLite/MySQL/SQLServer/MariaDB/etc. ver SQLAlchemy API .
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_sql SQLite3'.center(50),"*")
print("*"*54)
print(f"df - hacia SQLite3=\n{df}")
base="datos"
tabla='datos'
try:
    os.remove(f'{base}.db')
except:
    print("el archivo esta abierto o no existe")
connection = sqlite3.connect(f'{base}.db')
cursor = connection.cursor()
cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabla} (X INTENGER, Y INTENGER,Z INTENGER)')
connection.commit()
df.to_sql(tabla, connection, if_exists='replace', index = False)

# ~ df.to_sql(tabla, con=engine, if_exists='append', chunksize=1000, index=False)
print(f"en la carpeta donde esta esta practica deberas encontrar `{base}.db` con fecha y hora actual.\nPuedes abrirlo en DB browser ")
salida= cursor.execute(f'SELECT * FROM {tabla}').fetchall()    
print(f"df - desde sql=\n{salida}") 
pausa()
print("*"*54)
print("*",'to_sql SQLite + sqlalchemy + py'.center(50),"*")
print("*"*54)
print(f"df - hacia SQLite=\n{df}")
print("*"*50)
from sqlalchemy import create_engine
base="datos_2"
tabla='datos'
try:
    os.remove(f'{base}.db')
except:
    print("el archivo esta abierto o no existe")
engine = create_engine(f'sqlite:///{base}.db', echo=True)# echo=False)
# ~ #connection = engine.connect()
df.to_sql(name=tabla, con=engine)
print(f"en la carpeta donde esta esta practica deberas encontrar `{base}.db` con fecha y hora actual.\nPuedes abrirlo en DB browser ")
salida= engine.execute(f'SELECT * FROM {tabla}').fetchall()
print(f"df - desde sql=\n{salida}") 
df_salida = pd.read_sql(f"SELECT * FROM {tabla}", connection) 
print("df - desde sql read_sql=\n",df_salida,f"\n.{type(df_salida)=}")
df_salida_2 = pd.read_sql_query(f"SELECT * FROM {tabla}", connection) 
print("df - desde sql read_sql_query=\n",df_salida_2,f"\n.{type(df_salida_2)=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
try:
    base="datos"
    datos_mysql={ "user": "root", "passwd": "2022", "host": "localhost", "local_infile": True, "autocommit": True, "charset": "utf8mb4"}
    connection = pymysql.connect(**datos_mysql)
    cursor = connection.cursor()
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {base};')
    cursor.execute(F"USE {base} ;")
    tabla='datosMySQL'
    cursor.execute(f'DROP TABLE IF EXISTS {tabla}')   
    # ~ cursor.execute('CREATE TABLE IF NOT EXISTS datosMySQL (X INT, Y INT,Z INT)') 
    print(cursor.execute("SHOW DATABASES"))
    print(cursor.execute("SHOW TABLES"))
    connection.close()
    base="datos"
    tabla='datosMySQL'
    datos_mysql={"database":base, "user": "root", "passwd": "2022", "host": "localhost", "local_infile": True, "autocommit": True, "charset": "utf8mb4"}
    #------------------------------------------------------------------------------------------------------
    engine = create_engine(f'mysql+pymysql://{datos_mysql["user"]}:{datos_mysql["passwd"]}@{datos_mysql["host"]}/{datos_mysql["database"]}?charset=utf8mb4')
    connection = engine.connect()
    df.to_sql(name=tabla, con=connection, if_exists = 'replace', index=False)
    # ~ df.to_sql(tabla, con=engine, if_exists='append', chunksize=1000, index=False)

    print("*"*54)
    print("*",'to_sql MySQL'.center(50),"*")
    print("*"*54)
    print(f"df - hacia MySQL=\n{df}")
    print("Puedes encontrar la base/tabla en  en MySQL workbench")
    df_salida = pd.read_sql(f"SELECT * FROM {base}.{tabla}", connection) 
    print("df - desde sql read_sql=\n",df_salida,f"\n.{type(df_salida)=}")
    df_salida_2 = pd.read_sql_query(f"SELECT * FROM {base}.{tabla}", connection) 
    print("df - desde sql read_sql_query=\n",df_salida_2,f"\n.{type(df_salida_2)=}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print('''
    tabla = "Tabla_sql"
    df.to_sql(name=tabla, con=connection, if_exists = 'replace', index=True)#<-----si creas la columna index
    df = pd.read_sql_query(name=tabla, con=conexion)
    df.drop(columns=['index'], inplace=True)#<-------------------------------------la eliminas al ingresar
    ''')
    query = f'SELECT X, Y FROM {tabla} WHERE X <= 2'

    df = pd.read_sql_query(query, con=connection)
    print(f"{query=}\ndf=\n{df}")
except:
    print ("confirmar MySQL instalado, ysuario y password")
pausa()
limpiar()
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
try:
    from sqlalchemy import create_engine
except Exception as error_:
    import pip
    pip.main(['install', 'sqlalchemy'])
    from sqlalchemy import create_engine
print(f'''
●  Crea un `DataFrame` envialo a SQLite `to_sql`  SQLAlchemy API.
●  Elimina el `DataFrame` y recuperalo desde SQLite `read_sql` SQLAlchemy API.
●  Crea un `excel` desde SQLite `to_excel`.
''')
def Solución():
    pass
#------------------------------------------------------------------------------------------------------
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print("*"*54)
print("*",'to_sql SQLite + sqlalchemy + read_sql+ to_excel'.center(50),"*")
print("*"*54)
nombre_archivo_excel = 'datos_desde_sql.xlsx'
nombre_hoja_excel = 'nombre_hoja_excel'
nombre_ddbb='datos_to_excel.db'
nombre_tabla='datos'
print(f"En la carpeta donde esta esta practica deberas encontrar `{nombre_ddbb}` con fecha y hora actual.\nPuedes abrirlo en DB browser ")
try:
    os.remove(f'{nombre_ddbb}')
except:
    print("el archivo esta abierto o no existe")
engine = create_engine(f'sqlite:///{nombre_ddbb}', echo=True)
df.to_sql(  name=nombre_tabla, 
            con=engine, 
            if_exists='replace', 
            index = False)
print("*"*54)
print(f"1) df - hacia SQLite3=\n{df}")
print(f"2) df - desde SQLite3=\n{df}")
print(f"3) df - hacia excel=\n{df}")
print("*"*50)
del df
connection = engine.connect()
df = pd.read_sql(f"SELECT * FROM {nombre_tabla}", connection).to_excel(nombre_archivo_excel,
                                                                                            header=True,
                                                                                            index=False,
                                                                                            sheet_name=nombre_hoja_excel)
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Convertir una columna de tipo string - cadena de caracteres a fecha con `to_datetime`.
''')
def Solución():
    pass
fechas = ['2018/12/31', '2022/01/31', '2023/05/21']
serie = pd.Series(fechas)
print(f"serie=\n{serie}")
serie = pd.to_datetime(pd.Series(serie))
#------------------------------------------------------------------------------------------------------
print(f"serie=\n{serie}")
df = pd.DataFrame(serie)
df.index=['fechas 1','fechas 2','fechas 3']
df.columns=['A']
print(f"df=\n{df}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
print(f"df.info()=\n{df.info()}")
df_2 = pd.DataFrame(serie, index=['fechas 1','fechas 2','fechas 3'], columns=['A'])
print(f"df=\n{df_2}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de arreglos *NumPy* y genera columnas e índices.
''')
def Solución():
    pass
dtype = [('Columna1', 'int32'), ('Columna2', 'float32'), ('Columna3', 'float64')]
np_arreglo = np.zeros(15, dtype=dtype)
indices = [f'Indice-{i}' for i in range(1, len(np_arreglo) + 1)]
df = pd.DataFrame(data=np_arreglo,index=indices)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
limpiar()
#######################################################################################################
print(f'''
● Crear un arreglos *NumPy* a partir de un `DataFrame`.
''')
def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
df = pd.DataFrame(data=datos)
print(f"df=\n{df}")
np_=df.to_numpy()
print(f"np_=\n{np_}\n{type(np_)}")
pausa()
limpiar()

#######################################################################################################

print(f'''
● Crear un objeto de la clase '`DataFrame`'.
''')
## Solución.
datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
df = pd.DataFrame(datos)
print(f"df:\n{df}")
print("*"*100)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Especificar nombres de índices arbitrarios a un objeto '`DataFrame`'.
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
● Crear un `DataFrame` a partir de listas varias.
''')
lista_col = ['X', 'Y']
lista_index = ['a', 'b']
lista_datos = [[3, 2], [7,3]] 
df = pd.DataFrame(data=lista_datos, columns = lista_col, index = lista_index) 
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de Pandas Series.
''')
series = {   'X': pd.Series([3, 2], 
                    index = ['a','b']), 
            'Y': pd.Series([7, 3], 
                    index = ['a','b'])} 
df = pd.DataFrame(data=series)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de una matriz (lista de listas) Python.
''')
def Solución():
    pass
matriz = [['X', 'Y'], [3, 2], [7, 3]]
encabezado = matriz.pop(0)
df = pd.DataFrame(data=matriz, columns=encabezado)
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de un diccionario Python.
''')
def Solución():
    pass
dic = {'X':[3, 2], 'Y':[7, 3]}
df = pd.DataFrame(data=dic, index=['a','b'])
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################
print(f'''
● Crear un `DataFrame` a partir de una lista de  diccionarios Python.
''')
def Solución():
    pass
dic = [{'X':3,'Y': 2},{'X':7, 'Y':3}]
df = pd.DataFrame(data=dic, index=['a','b'])
#------------------------------------------------------------------------------------------------------
print(f"df=\n{df}")
pausa()
#######################################################################################################

