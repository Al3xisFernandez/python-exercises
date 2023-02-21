from __init__ import *
import os

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
limpiar()

import time
tiempo=time.time()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def ya_hechos():
    pass
print('''
El hundimiento del Titanic es uno de los naufragios más famosos de la historia.

El 15 de abril de 1912, durante su viaje inaugural, el RMS Titanic, ampliamente considerado como "insumergible", se hundió después de chocar con un iceberg. 
Desafortunadamente, no había suficientes botes salvavidas para todos a bordo, lo que resultó en la muerte de 1502 de los 2224 pasajeros y tripulantes.
Si bien hubo algún elemento de suerte involucrado en la supervivencia, parece que algunos grupos de personas tenían más probabilidades de sobrevivir que otros.

        Basic EDA and cleaning data
df_titanic = pd.read_csv('titanic.csv')
df_titanic3 = pd.read_excel("titanic3.xls")
        https://www.kaggle.com/code/francescopaolol/logisticregression-on-complete-titanic-dataset
        titanic1 (todas las columnas en capitalize)
                'PassengerId': 'PassengerId', 
                'Survived'   : { 0 = 'Fallecio', 1 = 'sobrevivio' }, 
                'Pclass'     : { 1 : '1st', 2 : '2nd', 3 : '3rd'  }, 
                'Name'       : 'Nombre', 
                'Sex'        : ['male','female'], 
                'Age'        : Edad, #                                                  int
      *         'SibSp'      : Número de hermanos / cónyuges del pasajero a bordo,#     int
      *         'Parch'      : Número de padres / hijos del pasajero a bordo, #         int
      *         'Ticket'     : 'Numero de ticket', 
                'Fare'       : 'Precio del ticket', 
      *         'Cabin'      : 'Cabina', 
                'Embarked'   : {'C':'Chernourg','Q':'Queenstown','S':'Southhampton'},#puerto de origen
                
        titanic3 (todas las columnas en lower)
                'boat'       : Número de bote de rescate (si sobrevivio),
                'body'       : Número de cuerpo (si no sobrevivio pero el cuerpo fue encontrado),
                'home.dest'  : 'destino del viaje',
                'survived'   : 'out target'

 Número de hermanos / cónyuges del pasajero (valor entero)

Parch: el número de padres / hijos del pasajero (valor entero)
''',Fore.WHITE+Back.BLUE,'''

    1)  Lee el archivos csv y genera un DataFrame
            confirma que es el adecuado visualizando los 10 primeros y ultimos regietros
    2)  Genera un resumen de su informacion en bruto
    3)  Eliminar las columnas que no son necesarias para el trabajo ('SibSp','Parch','Ticket', 'Cabin')
    4)  Con datos numéricos visualiza las columnas "Name","Fare" y "Age" del df 
            segun el precio del tiqket en orden de menor a mayor
            segun la edad en orden de mayor a menor
            quien fue el pasajero menor edad, quien el mayor y la media del pasaje
            guarda estos resiltados en un diccionario
    5)  Selecciona los pasajeros 'Sex' = 'females', 'Survived' = '0'   
            quienes y cuantos de estos eran de 1ra, de 2da y de 3ra clase
            ver métodos distintos
    6)  Reemplazar :
            las iniciales por los puertos de destino:
                'Embarked'   : {'C':'Chernourg','Q':'Queenstown','S':'Southhampton'}
            la sobrevivencia o fallecimiento:
                'Survived'   : { 0 : 'Fallecio', 1 : 'sobrevivio' },

    7)  Generar nuevas columnas a partir del genero y de las clases:


    8)  Malditos NaN.
            Busca en que columnas hay nulos (None / np.nan) 
                Si existen NaN en 'Age' reemplazarlos por la media de la columna

    9)  imprime las tarifas promedio para cada clase.


    10) ¿Qué tipo de personas tuvieron más probabilidades de sobrevivir?
    
    
    Verifica que los tipos de datos de las columnas, fijate si se adecuan a tus neccesidades, sino cambia los tipos.\n''',
Style.RESET_ALL,
Fore.BLACK+Back.LIGHTCYAN_EX,
'''
¿Qué tipo de personas tuvieron más probabilidades de sobrevivir?
utilizando datos de pasajeros (es decir, nombre, edad, sexo, clase socioeconómica, etc.).

se salvaron primero los niños luego las mujeres luego los hombres y la tripulacion al final?
se salvaron los de 1ra clase luego los de 2da , 3ra, etc.?
''',Style.RESET_ALL)


pausa()

import time
tiempo=time.time()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_titanic = pd.read_csv('titanic.csv')
# ~ df_titanic3 = pd.read_excel("titanic3.xls")#, index_col=None)
def ya_hechos():
    pass

#######################################################################################################
limpiar()
print (time.time()-tiempo)
print ("*"*104)
print ("*","1)  Lee el archivos csv y genera un DataFrame".center(100),"*")
print ("*"*104)
df_titanic = pd.read_csv('titanic.csv')
#df_titanic = pd.read_csv ( "train.csv", usecols = [ "PassengerId", "Sobrevived", "Pclass" ] ) 
print (f"{df_titanic.head (10)}")
print (f"{df_titanic.tail (10)}")
pausa()
#######################################################################################################
print ("*"*104)
print ("*","2)  Genera un resumen de su informacion en bruto".center(100),"*")
print ("*"*104)
print (f"{df_titanic.describe()}")
#['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
print ('''f_titanic.describe 
Este método se utiliza para obtener un resumen de los valores numéricos en su conjunto de datos. 
    Calcula con las columnas con valores numéricos
        la cantidad de registros,
        la media, 
        la desviación estándar, 
        el valor mínimo, 
        el primer percentil, 
        el segundo percentil, 
        el tercer percentil,
        el valor máximo. 
Estos datos y muchos mas se pueden obtener por separado
''')
print("DataFrame:",df_titanic)
print("-"*50)
print("objeto tipo:-------------------------------------->:",type(df_titanic))
print("DataFrame index:---------------------------------->:",df_titanic.index)
print("DataFrame desviacion estandar:-------------------->:",df_titanic.std(numeric_only=True))
print("DataFrame media:---------------------------------->:",df_titanic.mean(numeric_only=True))
print("DataFrame Minimo:--------------------------------->:",df_titanic.min(numeric_only=True))
print("DataFrame Maximo:--------------------------------->:",df_titanic.max(numeric_only=True))
print("DataFrame tamaño:--------------------------------->:",df_titanic.size)
print("DataFrame shape:---------------------------------->:",df_titanic.shape)
print("DataFrame memory_usage:--------------------------->:\n",df_titanic.memory_usage())
print("DataFrame ndim:----------------------------------->:",df_titanic.ndim)
print("DataFrame size:----------------------------------->:",df_titanic.size)
# ~ print("DataFrame name:----------------------------------->:",df_titanic.name)
print("DataFrame indice:--------------------------------->:",df_titanic.index)
print("DataFrame columns:-------------------------------->:",df_titanic.columns)
print("DataFrame axes:----------------------------------->:\n",df_titanic.axes)
print("DataFrame dtypes:--------------------------------->:\n",df_titanic.dtypes)
print("DataFrame empty:---------------------------------->:",df_titanic.empty) 
print("DataFrame nulos:---------------------------------->:",df_titanic.isnull().sum()) 
print("DataFrame info:----------------------------------->:",df_titanic.info())   
print ('''
El método .info() devuelve la siguiente información sobre cada columna de un DataFrame:
    índice de cada columna, 
    nombres, 
    cantidad de valores no nulos,
    uso de memoria.
''')
pausa()
limpiar()
#######################################################################################################
print ("*"*104)
print ("*",' 3)  Eliminar las columnas que no son necesarias para el trabajo :'.center(100),"*")
print ("*","         ('SibSp','Parch','Ticket', 'Cabin')".center(100),"*")
print ("*"*104)
print (f"{df_titanic[['Name','Survived','Embarked','Sex']]=}")
print (f"{df_titanic.columns}")
df_titanic=df_titanic.drop(['SibSp','Parch','Ticket', 'Cabin'], axis=1)
print (f"{df_titanic[['Name','Survived','Embarked','Sex']]=}")
print (f"{df_titanic.columns}")
pausa()
limpiar()
#######################################################################################################
print ("*"*104)
print ("*",' 4) Con datos numéricos visualiza las columnas "Name","Fare" y "Age" del df'.center(100),"*")
print ("*"*104)
print ("*"*104)
print ("*",' 4.1)    segun el precio del tiqket en orden de menor a mayor'.center(100),"*")
print ("*"*104)
df_titanic = pd.read_csv('titanic.csv')    
print (f'df[["Name","Fare","Age"]].sort_values("Fare")\n:{df_titanic[["Name","Fare","Age"]].sort_values("Fare")}')
pausa()
#------------------------------------------------------------------------------------------------------
print ("*"*104)
print ("*",' 4.2)  vsegun la edad en orden de mayor a menor'.center(100),"*")
print ("*"*104)
print (f'df[["Name","Fare","Age"]].sort_values("Age")\n:{df_titanic[["Name","Fare","Age"]].sort_values("Age", ascending = False)}')
#------------------------------------------------------------------------------------------------------
print ("*"*104)
print ("*",' 4.3)  quien fue el pasajero menor edad, quien el mayor y la media de los pasajeros'.center(100),"*")
print ("*"*104)
print (f'df.sort_values("Fare")\n:{df_titanic[["Name","Fare","Age"]].Age.min()}')
print('El pasajero mayor edad:',df_titanic.Age.max())
print('El pasajero menor edad:',df_titanic.Age.min())
print('Promedio de edad de los pasajeros:' ,df_titanic.Age.mean())
#######################################################################################################
pausa()
limpiar()
print ("*"*104)
print ("*"," 5)  Selecciona los pasajeros 'Sex' = 'females', 'Survived' = '0' ".center(100),"*")  
print ("*","        quienes y cuantos de estos eran de 1ra, de 2da y de 3ra clase".center(100),"*")
print ("*"*104)
df1=df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female')]
print("df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female')]:\n" ,df1[['Name','Survived','Sex']])
df1=df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female')& (df_titanic['Pclass']==1)]
print("df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female') & (df_titanic['Pclass']==1)]:\n" ,df1[['Name','Survived','Sex']])
print (f"df1['Pclass'].value_counts()\nclase, cantidad\n",df1['Pclass'].count())
df2=df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female')& (df_titanic['Pclass']==2)]
print("df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female') & (df_titanic['Pclass']==2)]:\n" ,df2[['Name','Survived','Sex']])
print (f"df2['Pclass'].value_counts()\nclase, cantidad\n",df2['Pclass'].count())
df3=df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female')& (df_titanic['Pclass']==3)]
print("df_titanic[(df_titanic['Survived']==0) & (df_titanic['Sex']=='female') & (df_titanic['Pclass']==3)]:\n" ,df3[['Name','Survived','Sex']])
print (f"df3['Pclass'].value_counts()\nclase, cantidad\n",df3['Pclass'].count())
#######################################################################################################
df1=df_titanic.groupby(['Survived','Sex'])['Pclass'].value_counts()
print (f"{df1=}")
matriz = df_titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100
print (f"{matriz=}")
print (f"{matriz==1=}")
print(f"{df_titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
print(f"{df_titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
sex_f=df_titanic[ df_titanic.Sex=='male']
print (f"{sex_f=}")
df3=df_titanic[['Sex','Survived','Pclass']].groupby(['Pclass']).value_counts(normalize=True) * 100
print (f"{df3=}")
# ~ df_titanic=df_titanic['Sex'].unstack()['female']
print (f"df_titanic:\n{df_titanic}")
# ~ df_titanic2 = df_titanic.describe().loc[['min','max']]
# ~ print (f"\ndf_titanic = df_titanic.describe().loc[['min','max']]:\n\n{df_titanic2}\n") 
pausa()
limpiar()
#######################################################################################################
print ("*"*104)
print ("*",' 6.1)  Reemplazar las iniciales por los puertos de destino:'.center(100),"*")
print ("*","         'Embarked'  : {'C':'Chernourg','Q':'Queenstown','S':'Southhampton'}".center(100),"*")
print ("*"*104)
print (f"df_titanic:\n{df_titanic}")
dic_replace={'C':'Chernourg','Q':'Queenstown','S':'Southhampton'}
df_titanic['Embarked']=df_titanic.Embarked.replace(dic_replace)
print (f"df_titanic:\n{df_titanic}")
print (f"{df_titanic[['Name','Survived','Embarked','Sex']]=}")
#------------------------------------------------------------------------------------------------------

pausa()
print ("*"*104)
print ("*",' 6.2)  Reemplazar la sobrevivencia o fallecimiento:'.center(100),"*")
print ("*","         'Survived'   : { 0 = 'Fallecio', 1 = 'sobrevivio' }".center(100),"*")
print ("*"*104)
dic_replace= { 0 : 'Fallecio', 1 : 'sobrevivio' }
df_titanic['Survived']=df_titanic.Survived.replace(dic_replace)
print (f"{df_titanic[['Name','Survived','Embarked','Sex']]=}")
pausa()
limpiar()
#######################################################################################################
print ("*"*104)
print ("*",' 7)  Generar nuevas columnas a partir del genero y de las clases:'.center(100),"*")
print ("*"*104)
print (f"columnas:{df_titanic.columns}")
df_titanic = pd.get_dummies(df_titanic, columns = ['Sex','Embarked'], dummy_na = True )
print (f"df:\n{df_titanic}")
print (f"{df_titanic.columns=}")
print (f"columnas:{df_titanic.columns}")
print (f"{df_titanic[['Name','Survived','Sex_nan', 'Embarked_nan']]=}")
df_1=df_titanic[(df_titanic['Age'].isna())]
# ~ print (f"{df_titanic[['Name','Survived','Sex_female', 'Sex_male', 'Sex_nan', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Embarked_nan']]=}")
print (f"{df_1[['Name','Survived','Sex_female', 'Sex_male', 'Sex_nan', 'Embarked_Chernourg', 'Embarked_Queenstown', 'Embarked_Southhampton',  'Embarked_nan']]=}")

pausa()
limpiar()


#######################################################################################################
# ~ df_titanic = pd.read_csv('titanic3.csv') 
# ~ print(df_titanic.info())

# ~ dic_sex={  'male'  :['Mr','Capt','Countess','Sir','Master','Col','Mayor','Rev'],
            # ~ 'female':['Miss','Mrs','Ms','Mlle','Mme','Lady'],
            # ~ 'desconocido':['Dr']}
# ~ df_titanic.insert(4, 'Title', '')
# ~ df_titanic['Title'] = df.transform['Name'] (lambda dato: dato ** 2)
# ~ df_titanic['Title'] = df_titanic['Name'].str.split(',')#, expand = True)
# ~ print (f"{df_titanic[['Title','Name','Survived']]=}")
# ~ print (f"columnas:{df_titanic.columns}")
#######################################################################################################
print ("*"*104)
print ("*",' 8)  Malditos NaN.Busca en que columnas hay nulos (None / np.nan) '.center(100),"*")
print ("*",'           Si existen NaN en "Age" reemplazarlos por la media de la columna'.center(100),"*")
print ("*"*104)
#######################################################################################################
#               Estandar

edad_is_null = pd.isnull(df_titanic.Age)
print("df.Age bool de valores nulos:\n",edad_is_null)
edad_null_true = df_titanic.Age[edad_is_null]
print("df.Age bool de valores True nulos:\n",edad_null_true)
edad_null_count = len(edad_null_true)
print("Cantidad de valores nulos en df.Age:\n",edad_null_count)
print (f'Cantidad de valores nulos en df.Age\ndf_titanic["Age"].isna().sum()=\n{df_titanic["Age"].isna().sum()}')
print ("limpiemos....")
# si eliminamos los valore NaN luego no podre cambiarlos porque no existiran
# ~ df_titanic['Age']=df_titanic.Age.dropna(how='all')
# ~ print (f"{df_titanic.Age}")
# Encuentra la edad promedio
mean_age = sum(df_titanic.Age.dropna()) / len(df_titanic.Age.dropna())
print(f"{sum(df_titanic['Age'])=}<-------------------------------malditos NaN. Hay que eliminar los valores perdidos")
print(f"{len(df_titanic.Age)=}")
print(f"{mean_age=}")
mean_age = sum(df_titanic.Age.dropna()) / len(df_titanic.Age.dropna())
print(f"{sum(df_titanic.Age.dropna())=}<-------------------------------:) ")
print(f"{len(df_titanic.Age.dropna())=}")
print(f"{mean_age=}")
print(f"{df_titanic.Age.mean()=}")
df_titanic['Age']=df_titanic['Age'].fillna(df_titanic.Age.mean())
print (f"{df_titanic[['Name','Survived','Age']]=}")
print (f"columnas:{df_titanic.columns}")

pausa()
limpiar()
#######################################################################################################

print ("*"*104)
print ("*",' Releo en original '.center(100),"*")
print ("*"*104)

df_titanic = pd.read_csv('titanic.csv')
print ("*"*104)
print ("*",' 9)  Cual era la tarifa promedio para cada clase. '.center(100),"*")
print ("*"*104)
precio_Class_1=[]
precio_Class_2=[]
precio_Class_3=[]
for Index, content in df_titanic.iterrows ():
    if content.Pclass== 1 and content.Fare!= None :
        precio_Class_1.append(content.Fare)
    elif content.Pclass== 2 and content.Fare!= None :
        precio_Class_2.append(content.Fare)
    elif content.Pclass== 3 and content.Fare!= None :
        precio_Class_3.append(content.Fare)
print (f"precio promedio de 1ra clase:{sum(precio_Class_1)/len(precio_Class_1)}")
print (f"precio promedio de 2da clase:{sum(precio_Class_2)/len(precio_Class_2)}")
print (f"precio promedio de 3ra clase:{sum(precio_Class_3)/len(precio_Class_3)}")
#------------------------------------------------------------------------------------------------------
df1=df_titanic[['Pclass','Fare']].groupby(['Pclass']).mean()
print (f"precio promedio de cada clase:\n{df1}")
pausa()
limpiar()
#######################################################################################################
print ("*"*104)
print ("*",' 10)  ¿Qué tipo de personas tuvieron más probabilidades de sobrevivir?'.center(100),"*")
print ("*","            'Survived'   : { 0 = 'Fallecio', 1 = 'sobrevivio' }, ".center(100),"*")
print ("*"*104)
sobrevivencia={ 'Class_1':{'total':{'Hombres':0,'Mujeres':0},'sobrevivio':{'Hombres':0,'Mujeres':0},'fallecio':{'Hombres':0,'Mujeres':0}},
                'Class_2':{'total':{'Hombres':0,'Mujeres':0},'sobrevivio':{'Hombres':0,'Mujeres':0},'fallecio':{'Hombres':0,'Mujeres':0}},
                'Class_3':{'total':{'Hombres':0,'Mujeres':0},'sobrevivio':{'Hombres':0,'Mujeres':0},'fallecio':{'Hombres':0,'Mujeres':0}}
                }

for Index, content in df_titanic.iterrows ():
    print (content)
    if content.Sex=='male':
        sobrevivencia[f'Class_{content.Pclass}']['sobrevivio' if content.Survived == 0 else 'fallecio']['Hombres']+=1
        sobrevivencia[f'Class_{content.Pclass}']['total']['Hombres']+=1
    else:
        sobrevivencia[f'Class_{content.Pclass}']['sobrevivio' if content.Survived == 0 else 'fallecio']['Mujeres']+=1
        sobrevivencia[f'Class_{content.Pclass}']['total']['Mujeres']+=1  

print (sobrevivencia)

pausa()

Total_sobrevivientes_Mujeres_clase_1= sobrevivencia['Class_1']['sobrevivio']['Mujeres']
Total_sobrevivientes_Hombres_clase_1= sobrevivencia['Class_1']['sobrevivio']['Hombres']
Total_sobrevivientes_Mujeres_clase_2= sobrevivencia['Class_2']['sobrevivio']['Mujeres']
Total_sobrevivientes_Hombres_clase_2= sobrevivencia['Class_2']['sobrevivio']['Hombres']
Total_sobrevivientes_Mujeres_clase_3= sobrevivencia['Class_3']['sobrevivio']['Mujeres']
Total_sobrevivientes_Hombres_clase_3= sobrevivencia['Class_3']['sobrevivio']['Hombres']
print (f"total de Mujeres sobrevivientes que viajaban en 1ra clase: {Total_sobrevivientes_Mujeres_clase_1}")
print (f"total de Hombres sobrevivientes que viajaban en 1ra clase: {Total_sobrevivientes_Hombres_clase_1}")
print (f"total de Mujeres sobrevivientes que viajaban en 2da clase: {Total_sobrevivientes_Mujeres_clase_2}")
print (f"total de Hombres sobrevivientes que viajaban en 2da clase: {Total_sobrevivientes_Hombres_clase_2}")
print (f"total de Mujeres sobrevivientes que viajaban en 3ra clase: {Total_sobrevivientes_Mujeres_clase_3}")
print (f"total de Hombres sobrevivientes que viajaban en 3ra clase: {Total_sobrevivientes_Hombres_clase_3}") 
#------------------------------------------------------------------------------------------------------
# ~ print("*"*100)
# ~ df1=df_titanic[['Pclass','Sex','Survived']].groupby(['Pclass','Sex']).sum()
# ~ print (f"""precio promedio de cada clase:
               # ~ Not
# ~ {df1}""")
# ~ print("*"*100)
#------------------------------------------------------------------------------------------------------
print("*"*100)
pausa()
Total_fallecidos_Mujeres_clase_1= sobrevivencia['Class_1']['fallecio']['Mujeres']
Total_fallecidos_Hombres_clase_1= sobrevivencia['Class_1']['fallecio']['Hombres']
Total_fallecidos_Mujeres_clase_2= sobrevivencia['Class_2']['fallecio']['Mujeres']
Total_fallecidos_Hombres_clase_2= sobrevivencia['Class_2']['fallecio']['Hombres']
Total_fallecidos_Mujeres_clase_3= sobrevivencia['Class_3']['fallecio']['Mujeres']
Total_fallecidos_Hombres_clase_3= sobrevivencia['Class_3']['fallecio']['Hombres']
print (f"total de Mujeres fallecidas que viajaban en 1ra clase: {Total_fallecidos_Mujeres_clase_1}")
print (f"total de Hombres fallecidos que viajaban en 1ra clase: {Total_fallecidos_Hombres_clase_1}")
print (f"total de Mujeres fallecidas que viajaban en 2da clase: {Total_fallecidos_Mujeres_clase_2}")
print (f"total de Hombres fallecidos que viajaban en 2da clase: {Total_fallecidos_Hombres_clase_2}")
print (f"total de Mujeres fallecidas que viajaban en 3ra clase: {Total_fallecidos_Mujeres_clase_3}")
print (f"total de Hombres fallecidos que viajaban en 3ra clase: {Total_fallecidos_Hombres_clase_3}") 
#------------------------------------------------------------------------------------------------------
print("*"*100)
pausa()
df1=df_titanic[['Pclass','Sex','Survived']].groupby(['Pclass','Sex']).sum()
print (f"""precio promedio de cada clase:
               Not
{df1}""")
#------------------------------------------------------------------------------------------------------
print("*"*100)
Total_Mujeres_viajaba_en_clase_1= sobrevivencia['Class_1']['total']['Mujeres']
Total_Hombres_viajaba_en_clase_1= sobrevivencia['Class_1']['total']['Hombres']
Total_Mujeres_viajaba_en_clase_2= sobrevivencia['Class_2']['total']['Mujeres']
Total_Hombres_viajaba_en_clase_2= sobrevivencia['Class_2']['total']['Hombres']
Total_Mujeres_viajaba_en_clase_3= sobrevivencia['Class_3']['total']['Mujeres']
Total_Hombres_viajaba_en_clase_3= sobrevivencia['Class_3']['total']['Hombres']

print (f"total de Mujeres que viajaban en 1ra clase :{Total_Mujeres_viajaba_en_clase_1}")
print (f"total de Hombres que viajaban en 1ra clase :{Total_Hombres_viajaba_en_clase_1}")
print (f"total de Mujeres que viajaban en 2da clase :{Total_Mujeres_viajaba_en_clase_2}")
print (f"total de Hombres que viajaban en 2da clase :{Total_Hombres_viajaba_en_clase_2}")
print (f"total de Mujeres que viajaban en 3ra clase :{Total_Mujeres_viajaba_en_clase_3}") 
print (f"total de Hombres que viajaban en 3ra clase :{Total_Hombres_viajaba_en_clase_3}")
#------------------------------------------------------------------------------------------------------
print("*"*100)
pausa()
Porcentaje_Mujeres_clase_1= round(Total_sobrevivientes_Mujeres_clase_1/Total_Mujeres_viajaba_en_clase_1*100,2)
Porcentaje_Hombres_clase_1= round(Total_sobrevivientes_Hombres_clase_1/Total_Hombres_viajaba_en_clase_1*100,2)
Porcentaje_Mujeres_clase_2= round(Total_sobrevivientes_Mujeres_clase_2/Total_Mujeres_viajaba_en_clase_2*100,2)
Porcentaje_Hombres_clase_2= round(Total_sobrevivientes_Hombres_clase_2/Total_Hombres_viajaba_en_clase_2*100,2)
Porcentaje_Mujeres_clase_3= round(Total_sobrevivientes_Mujeres_clase_3/Total_Mujeres_viajaba_en_clase_3*100,2)
Porcentaje_Hombres_clase_3= round(Total_sobrevivientes_Hombres_clase_3/Total_Hombres_viajaba_en_clase_3*100,2)

print (f"Porcentaje de Mujeres sobrevivientes que viajaban en 1ra clase :{Porcentaje_Mujeres_clase_1}%")
print (f"Porcentaje de Hombres sobrevivientes que viajaban en 1ra clase :{Porcentaje_Hombres_clase_1}%")
print (f"Porcentaje de Mujeres sobrevivientes que viajaban en 2da clase :{Porcentaje_Mujeres_clase_2}%")
print (f"Porcentaje de Hombres sobrevivientes que viajaban en 2da clase :{Porcentaje_Hombres_clase_2}%")
print (f"Porcentaje de Mujeres sobrevivientes que viajaban en 3ra clase :{Porcentaje_Mujeres_clase_3}%") 
print (f"Porcentaje de Hombres sobrevivientes que viajaban en 3ra clase :{Porcentaje_Hombres_clase_3}%")
 

#------------------------------------------------------------------------------------------------------
print("*"*100)
pausa()
Porcentaje_Mujeres_clase_1= round(Total_fallecidos_Mujeres_clase_1/Total_Mujeres_viajaba_en_clase_1*100,2)
Porcentaje_Hombres_clase_1= round(Total_fallecidos_Hombres_clase_1/Total_Hombres_viajaba_en_clase_1*100,2)
Porcentaje_Mujeres_clase_2= round(Total_fallecidos_Mujeres_clase_2/Total_Mujeres_viajaba_en_clase_2*100,2)
Porcentaje_Hombres_clase_2= round(Total_fallecidos_Hombres_clase_2/Total_Hombres_viajaba_en_clase_2*100,2)
Porcentaje_Mujeres_clase_3= round(Total_fallecidos_Mujeres_clase_3/Total_Mujeres_viajaba_en_clase_3*100,2)
Porcentaje_Hombres_clase_3= round(Total_fallecidos_Hombres_clase_3/Total_Hombres_viajaba_en_clase_3*100,2)

print (f"Porcentaje de Mujeres fallecidos que viajaban en 1ra clase :{Porcentaje_Mujeres_clase_1}%")
print (f"Porcentaje de Hombres fallecidos que viajaban en 1ra clase :{Porcentaje_Hombres_clase_1}%")
print (f"Porcentaje de Mujeres fallecidos que viajaban en 2da clase :{Porcentaje_Mujeres_clase_2}%")
print (f"Porcentaje de Hombres fallecidos que viajaban en 2da clase :{Porcentaje_Hombres_clase_2}%")
print (f"Porcentaje de Mujeres fallecidos que viajaban en 3ra clase :{Porcentaje_Mujeres_clase_3}%") 
print (f"Porcentaje de Hombres fallecidos que viajaban en 3ra clase :{Porcentaje_Hombres_clase_3}%")
#------------------------------------------------------------------------------------------------------
print("*"*100)
df1=df_titanic[['Pclass','Sex','Survived']].groupby(['Pclass','Sex']).mean()
print (f"""precio promedio de cada clase:
               Not
{df1}""")
print("*"*100)
#------------------------------------------------------------------------------------------------------
Total_Mujeres_clase_1= sobrevivencia['Class_1']['total']['Mujeres']
Total_Hombres_clase_1= sobrevivencia['Class_1']['total']['Hombres']
Total_Mujeres_clase_2= sobrevivencia['Class_2']['total']['Mujeres']
Total_Hombres_clase_2= sobrevivencia['Class_2']['total']['Hombres']
Total_Mujeres_clase_3= sobrevivencia['Class_3']['total']['Mujeres']
Total_Hombres_clase_3= sobrevivencia['Class_3']['total']['Hombres']
print("*"*100)
#------------------------------------------------------------------------------------------------------
pausa()
limpiar()

# ~ print("*"*100)
# ~ df1=df_titanic[['Pclass','Sex','Survived']].groupby(['Pclass','Sex']).sum()
# ~ print (f"""precio promedio de cada clase:
               # ~ Not
# ~ {df1}""")
# ~ print("*"*100)

#------------------------------------------------------------------------------------------------------
print("*"*100)
# ~ Total_sobrevivientes_Mujeres= Total_sobrevivientes_Mujeres_clase_1 + Total_sobrevivientes_Mujeres_clase_2 + Total_sobrevivientes_Mujeres_clase_3
# ~ print (f"total de Mujeres sobrevivientes que viajaban en todas clase: {Total_sobrevivientes_Mujeres}")
# ~ Total_sobrevivientes_Hombres= Total_sobrevivientes_Hombres_clase_1 + Total_sobrevivientes_Hombres_clase_2 + Total_sobrevivientes_Hombres_clase_3
# ~ print (f"total de Hombres sobrevivientes que viajaban en todas clase: {Total_sobrevivientes_Hombres}")
Total_fallecidos_Mujeres= Total_fallecidos_Mujeres_clase_1 + Total_fallecidos_Mujeres_clase_2 + Total_fallecidos_Mujeres_clase_3
print (f"total de Mujeres fallecidos que viajaban en todas clase: {Total_fallecidos_Mujeres}")
Total_fallecidos_Hombres= Total_fallecidos_Hombres_clase_1 + Total_fallecidos_Hombres_clase_2 + Total_fallecidos_Hombres_clase_3
print (f"total de Hombres fallecidos que viajaban en todas clase: {Total_fallecidos_Hombres}")

#------------------------------------------------------------------------------------------------------
print("*"*100)
df1=df_titanic[['Survived','Sex','Pclass']].groupby(['Pclass']).count()
print (f"""precio promedio de cada clase:
               Not
{df1}""")
pausa()
limpiar()
# ~ df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              # ~ 'Parrot', 'Parrot'],
                   # ~ 'Max Speed': [380., 370., 24., 26.]})
# ~ df1=df_titanic.groupby("Animal", group_keys=True).apply(lambda x: x)
# ~ print (f"""precio promedio de cada clase:
               # ~ Not
# ~ {df1}""")



df1=df_titanic.groupby("Survived", group_keys=False).apply(lambda x: x)
print (f"""precio promedio de cada clase:
               Not
{df1}""")
pausa()
limpiar()
print("*"*50)
####################################################################################################
# ~ grupo = df_titanic.groupby(['Pclass',]).Survived==0
# ~ print("grupo = :\n", grupo)	
df = df_titanic.where(df_titanic['Survived'] == 1, "fallecio") 
print ("fallecio / sobrevivio:\n", df)
df = df.mask(df_titanic == 0, "fallecio") 
print ("fallecio / sobrevivio:\n", df)
print (df.columns)
print (df.Age)
print (df.Age.dtypes)
print("*"*50)
####################################################################################################
NuevosFilaAingresar = {'Survived':0,'Sex':'female'}
df1=df_titanic.append(NuevosFilaAingresar, ignore_index=True)
print("df {'Survived':0,'Sex':'female'} :\n",df1)
print (f"{df_titanic[['Survived','Sex']]}")
print (f"{df1[['Survived','Sex']]}")

NuevosFilaAingresar = {'Survived':0,'Sex':'female'}

# ~ df_aprobado=df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]



# ~ print ("Boliche Edad:\n",df_1[df_1['Edad'] >= 18]['Genero'])


# ~ print("*"*50)
# ~ df_1["Boliche"] = df_1.apply(lambda x: "Menor" if x["Edad"] < 18 else x["Genero"], axis=1)
# ~ print ("Boliche Edad:\n",df_1["Boliche"])

# ~ grupo = grupo[grupo["Survived"]!=0]
# ~ print("grupo = ):\n", grupo)	
####################################################################################################
print ("*"*104)
print ("*",' Releo en original '.center(100),"*")
print ("*"*104)
df_titanic = pd.read_csv('titanic.csv')

df=df_titanic
df1=df_titanic
print (f"{df1=}")
df1['Age'].isnull().any()
print (f"{df1=}")
df1=df.groupby(['Sex', 'Survived'])['Survived'].count()
df2=df[df['Sex']=="male"].value_counts(normalize=True) * 100
print("=======================\n",df[df['Sex']=="male"].value_counts(normalize=True) * 100)
print (f"{df2=}")




print(f"{df['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
#------------------------------------------------------------------------------------------------------
matriz = df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100
print (f"{matriz=}")
print (f"{matriz==1=}")
print(f"{df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
print(f"{df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
# ~ plt.pie(df['Survived'])
# ~ plt.show()
print (df.columns)
print (df.Age)
print (df.Age.dtypes)
print(" Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.")

df["mayor"]=df['Age'] >= 18
print(df)
print("*"*50)
#------------------------------------------------------------------------------------------------------
print(" Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.")
print(df.groupby(['Pclass', df['Age'] >= 18])['Survived'].value_counts(normalize = True) * 100)
print("*"*50)
pausa()
limpiar()
print("*"*50)
#------------------------------------------------------------------------------------------------------
# ~ df[['Sex','Survived']].groupby(['Sex']).mean().plot.bar()
# ~ plt.show()
df3=df[['Sex','Survived']].groupby(['Sex']).mean()
print (f"{df3=}")
fig = plt.figure(figsize =(10, 7))
plt.pie(df3['Survived'], labels =[ "Femeninos","Masculinos"])
plt.show()

f,ax=plt.subplots(1,2,figsize=(20,20))
df[df['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived = 0')
eje_x_1=list(range(0,85,5))

eje_x_1=list(range(0,round(max(df.Age)+1),round((max(df.Age)+1)/10)))
print (eje_x_1)

ax[0].set_xticks(eje_x_1)
df[df['Survived']==1].Age.plot.hist(ax=ax[1],bins=20,edgecolor='black',color='green')
eje_x_2=list(range(0,round(max(df.Age)+1),round((max(df.Age)+1)/10)))
print (eje_x_2)

ax[1].set_xticks(eje_x_2)
ax[1].set_title('Survived = 1')

plt.show()


# ~ df=df.groupby('Initial')['Age'].mean()
print(f"{df=}")
print("*"*50)
#------------------------------------------------------------------------------------------------------
'''
# ~ df['Initial'].replace(['Mlle','Mme' ,'Ms'  ,'Dr','Major','Lady','Countess','Jonkheer','Col'  ,'Rev'  ,'Capt','Sir','Don'],
                              # ~ ['Miss','Miss','Miss','Mr','Mr'   ,'Mrs' ,'Mrs'     ,'Other'   ,'Other','Other','Mr'  ,'Mr' ,'Mr' ],inplace=True)
'''

# ~ import seaborn as sb

# ~ f,ax=plt.subplots(1,2,figsize=(18,8))
# ~ sb.violinplot('Pclass','Age',hue='Survived',data=df_titanic[['Pclass','Age']],split=True,ax=ax[0])
# ~ ax[0].set_title('PClass and Age vs Survived')
# ~ ax[0].set_yticks(range(0,110,10))
# ~ sb.violinplot("Sex","Age", hue="Survived", data=df_titanic[['Sex','Age']],split=True,ax=ax[1])
# ~ ax[1].set_title('Sex and Age vs Survived')
# ~ ax[1].set_yticks(range(0,110,10))
# ~ plt.show()

# ~ sb.countplot('Survived',data=train_data)
# ~ plt.show()
# ~ print("*"*50)
#------------------------------------------------------------------------------------------------------
'''
Antes de poder utilizar los algoritmos de aprendizaje automático que todos conocemos y amamos, 
Es importante comprender cómo obtener inicialmente los datos en el orden correcto y cómo analizar 
efectivamente los datos para producir el mejor modelo. Esta publicación proporcionará una hoja de 
ruta básica que un científico de datos puede seguir para realizar análisis de datos exploratorios ( EDA ) 
cuando trabaje con un nuevo conjunto de datos en Python.

Conjunto de datos:
Revisión inicial:
Después de cargar el archivo en un marco de datos de Pandas, es útil mirar las primeras filas y el tamaño 
del conjunto de datos para tener una idea de con qué está trabajando. 
Esto se logra mejor usando el .head ( ) y .forma métodos.


los .describe ( ) El método proporciona una descripción estadística rápida de las características cuantitativas 
en el conjunto de datos desde la desviación estándar de cada característica hasta los valores mínimos y máximos. 
Esto también se puede usar para detectar posibles valores atípicos.

 Esta .isnull ( ) y .info ( ) 
 act_2018.isnull ( ).sum ( )
 
 We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers (imputation). check the average age by passenger class. For example:

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline

    #Data visualization to see the age difference due to Passenger class
    plt.figure(figsize=(12, 7))
    sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')

    def impute_age(cols):
        Age = cols[0]
        Pclass = cols[1]

        if pd.isnull(Age):

            if Pclass == 1:
                return 37

            elif Pclass == 2:
                return 29

            else:
                return 24

        else:
            return Age
     train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)#filling the missing values
 
'''
 # ~ https://towardsdatascience.com/steps-before-modeling-cleaning-to-eda-9a9e02981e57
'''
# First filling NaN on train set as I did before.
grouped = train.groupby(["Sex","Title", "Pclass"])
grouped_m = grouped.median().reset_index()[["Sex", "Title", "Pclass", "Age"]]
train["Age"] = train["Age"].fillna(grouped["Age"].transform("median"))

# Then used pd.DataFrame.merge() to apply the same grouped features on the test data.
med = train.groupby(['Sex', 'Pclass', 'Title'], 
                   as_index=False)['Age'].median()
test = test.merge(med, on=['Sex','Pclass','Title'], how='left', suffixes=('','_'))
test['Age'] = test['Age'].fillna(test.pop('Age_'))
'''
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
'''

'''
dfSurvivals = pd.read_excel("titanic3.xls", index_col=None)
dfSurvivals.to_csv('titanic3.csv')
print (f"{dfSurvivals}")
################################################################################
print(f"The Titanic survivals data set consists of {dfSurvivals.shape[1]} different parameters for {dfSurvivals.shape[0]} samples.")

################################################################################
print (f"{dfSurvivals.info()=}")
print (f"{(dfSurvivals.isnull() | dfSurvivals.empty | dfSurvivals.isna()).sum()=}")
def showPercentageNan(colName, dtFrame):
    perc = (dtFrame[colName].isnull().sum() / dtFrame.shape[0])
    print(f"Percent of missing ''{colName}'' records is {round(perc * 100,3)} %")
colNan = [ 
            "fare",
            "cabin",
            "embarked",
            "boat",
            "body",
            "home.dest"
        ]

#===============================================================================


df_ohe = pd.get_dummies(dfSurvivals, columns = ['sex','embarked'], dummy_na = True )
# ~ 'Sex', 'Embarked'
print(f"{df_ohe}")
# ~ exit()
#===============================================================================

for col in colNan:
    showPercentageNan(col, dfSurvivals)
################################################################################
dfSurvivals.drop(["cabin","boat","body","home.dest"], axis=1, inplace=True)
print(f"{dfSurvivals=}")
dfSurvivals["fare"].fillna(value = dfSurvivals["fare"].mean(), inplace=True)
dfSurvivals["embarked"].fillna(dfSurvivals["embarked"].value_counts().idxmax(), inplace=True)
dfSurvivals["age"].fillna(value = dfSurvivals["age"].mean(), inplace=True)
nrAgeNaN = dfSurvivals["age"].isna().sum()
nrFareNaN = dfSurvivals["fare"].isna().sum()
nrEmbarkedNaN = dfSurvivals["embarked"].isna().sum()
print(f"Now we have {nrAgeNaN} missing values on age column!")
print(f"Now we have {nrFareNaN} missing values on fare column!")
print(f"Now we have {nrEmbarkedNaN} missing values on embarked column!")
################################################################################
#pip install scikit-learn
from sklearn.preprocessing import LabelEncoder

labelencoder_X = LabelEncoder()

dfSurvivals["name"] = labelencoder_X.fit_transform(dfSurvivals["name"])
dfSurvivals["embarked"] = labelencoder_X.fit_transform(dfSurvivals["embarked"])
dfSurvivals["ticket"] = dfSurvivals["ticket"].astype(str)
dfSurvivals["ticket"] = labelencoder_X.fit_transform(dfSurvivals["ticket"])

################################################################################


from sklearn.preprocessing import OneHotEncoder

result = OneHotEncoder().fit_transform(dfSurvivals["sex"].values.reshape(-1, 1)).toarray()
dfSurvivals[["Female", "Male"]] = pd.DataFrame(result, index = dfSurvivals.index)
dfSurvivals.drop(["sex"], axis=1, inplace=True)

################################################################################

dfSurvivals.head()
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

X = dfSurvivals.drop("survived", axis=1)
y = dfSurvivals["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(max_iter=5000)
model.fit(X_train,y_train)
p_predict = model.predict(X_test)

print ("The accuracy is", round(accuracy_score(p_predict, y_test) * 100,2))
print (f"{X=}")
print (f"{y=}")
# ~ print (f"{dfSurvivals}")

# ~ https://www.kaggle.com/datasets/hesh97/titanicdataset-traincsv




################################################################################



# ~ df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})


# ~ print ("dividimos en terminos de bin el DF ")
# ~ corte = [0, 5, 18, 35,60,90]
# ~ df_titanic['edad_corte'] = pd.cut(df_titanic['Age'], corte)
# ~ print (df_titanic[['Name','Age','edad_corte']])
# ~ df_titanic['cortes 10'] = pd.qcut(df_titanic['Age'], 10)
# ~ print (df_titanic[['Name','Age','edad_corte','cortes 10']])




import pandas as pd
def x():
    #create DataFrame
    df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C'],
                       'points': [25, 12, 25, 14, 19, 53, 25, 29]})

    #view DataFrame
    print(df)

    df.groupby(['team']).sum().plot(kind='pie', y='points')


    plt.show() 
    pausa()


print (df_titanic.columns)
# ~ df.groupby(['group_column']).sum().plot(kind='pie', y='value_column')
df_titanic.groupby(['Sex']).sum().plot(kind='pie', y='Survived')


plt.show()
df=df_titanic.copy()

df1=df_titanic.copy()
print (f"{df1=}")
df1['Age'].isnull().any()
print (f"{df1=}")
df1=df.groupby(['Sex', 'Survived'])['Survived'].count()
df1.plot(kind='pie', y='Survived');
plt.show()
df1=df[df['Sex']=="male"].value_counts(normalize=True)
print("=======================",type(df1))
print("=======================\n",df1)

pausa()
print ("df[df['Sex']=='male'].value_counts(normalize=True):\n",df[df['Sex']=='male'].value_counts(normalize=True))
df1.plot(kind='pie', y='Survived');
plt.show()
print("=======================\n",df1)
print (f"{df1=}")



print(f"{df['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
#------------------------------------------------------------------------------------------------------
matriz = df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100
print (f"{matriz=}")
print (f"{matriz==1=}")
print(f"{df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
print(f"{df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100=}")
print("*"*50)
# ~ plt.pie(df['Survived'])
# ~ plt.show()

print(" Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.")
df["mayor"]=df['Age'] >= 18
print(df)
print("*"*50)
#------------------------------------------------------------------------------------------------------
print(" Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.")
print(df.groupby(['Pclass', df['Age'] >= 18])['Survived'].value_counts(normalize = True) * 100)


plt.show()
print("*"*50)
pausa()
limpiar()
#------------------------------------------------------------------------------------------------------



df_titanic = pd.get_dummies(df_titanic, columns = ['Sex'], dummy_na = True )
print (f"{df_titanic[['Name','Survived','Sex_female', 'Sex_male', 'Sex_nan']]=}")
print (f"columnas:{df_titanic.columns}")
df_titanic.groupby(['Sex_female', 'Sex_male']).sum().plot(kind='pie', y='Survived')

plt.show()
print("*"*50)
pausa()
limpiar()
#------------------------------------------------------------------------------------------------------
df_titanic.groupby(['Sex_female', 'Sex_male']).sum().plot(kind='pie', y='Survived', autopct='%1.0f%%',
                        colors = ['pink', 'steelblue'],
                        title='Supervivencia segun  sexo')
print ("""
Esta bien?
    La base de salida sobre la de entrada
    cuantas mujeres se salvaron sobre cuantas viajaban 


""")
plt.show()
print("*"*50)
pausa()
limpiar()
#------------------------------------------------------------------------------------------------------
df_titanic.groupby(['Sex_female']).sum().plot(kind='pie', y='Survived', autopct='%1.0f%%',
                        colors = ['red', 'blue'],
                        title='Supervivencia ingreso/egreso sexo')
plt.show()
print("*"*50)
pausa()
limpiar()

'''
    print(df_titanic.groupby('Pclass')['Survived'].value_counts()/df_titanic['Survived'].count() )
    #    o
    print(df_titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100)
'''

# ~ https://www.statology.org/pandas-pie-chart/
#------------------------------------------------------------------------------------------------------
df_titanic.groupby(['Sex_female'])['Survived'].value_counts().plot(kind='pie', y='Survived', autopct='%1.0f%%',
                        colors = ['orange', 'black'],
                        title='Supervivencia ingreso/egreso sexo')
plt.show()
x=df_titanic.groupby(['Sex_female'])['Survived'].value_counts()
print (f"Sex_female\n{x=}")
y=x.to_list()
print (f"Sex_female\n{y=}")
print (f"{(y[0]/(sum(y))*100)=}")
print (f"{(y[1]/(sum(y))*100)=}")
x=df_titanic.groupby(['Sex_male'])['Survived'].value_counts()/df_titanic['Survived'].count() 
print (f"Sex_male\n{x=}")
z=x.to_list()
print (f"Sex_male\n{y=}")
print (f"{(z[0]/(sum(z))*100)=}")
print (f"{(z[1]/(sum(z))*100)=}")
####################################################################################################
print ("*"*104)
print ("*",' Releo en original '.center(100),"*")
print ("*"*104)
df_titanic = pd.read_csv('titanic.csv')
NuevosFilaAingresar = {'Survived':0,'Sex':'female'}
df1=df_titanic.append(NuevosFilaAingresar, ignore_index=True)
print("df {'Survived':0,'Sex':'female'} :\n",df1)
print (f"{df_titanic[['Survived','Sex']]}")
print (f"{df1[['Survived','Sex']]}")

NuevosFilaAingresar = {'Survived':0,'Sex':'female'}
# ~ df_titanic.groupby([["Female", "Male"]]).sum().plot(kind='pie', y='Survived', autopct='%1.0f%%',
                                # ~ colors = ['red', 'pink', 'steelblue'],
                                # ~ title='Points Scored by Team')
#                                   'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
################################################################################
print(df_titanic[df_titanic["Pclass"]==1]['Name'].sort_values())
# ~ df_titanic.Age.plot(title='df_titanic Ed.IT 2023', 
                                    # ~ xlabel = 'Age',
plt.show()                                   # ~ figsize=(10,6))
# ~ plt.show(block=False)
# ~ plt.pause(10)
# ~ plt.close();

# ~ df_titanic.Age.sort_values().plot(title='df_titanic Ed.IT 2023', 
                                    # ~ xlabel = 'Age',
          
# Create the figure and two axes (two rows, one column)
fig, (ax1, ax2) = plt.subplots(2, 1)

# Create a plot of y = sin(x) on the first row
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)
ax1.plot(x1, y1)

# Create a plot of y = cos(x) on the second row
x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)
ax2.plot(x2, y2)

# Save the figure
# ~ plt.savefig('sin_cos.png')

plt.show(block=False)
plt.pause(10)
plt.close();


