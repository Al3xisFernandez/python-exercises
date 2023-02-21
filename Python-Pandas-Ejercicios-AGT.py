https://pynative.com/python-pandas-exercise/
print(f'''
● Ejercicio 1: desde el conjunto de datos dado, imprima las primeras y últimas cinco filas
''')
pausa()
limpiar()
#######################################################################################################

print(f'''
● Ejercicio 2: Limpie el conjunto de datos y actualice el archivo CSV
''')
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv", na_values={
                                                                                                    'price':["?","n.a"],
                                                                                                    'stroke':["?","n.a"],
                                                                                                    'horsepower':["?","n.a"],
                                                                                                    'peak-rpm':["?","n.a"],
                                                                                                    'average-mileage':["?","n.a"]})
print (df)

df.to_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")

pausa()
limpiar()
#######################################################################################################


print(f'''
● Ejercicio 3: encuentre el nombre de la compañía de automóviles más caro
''')

import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df

pausa()
limpiar()
#######################################################################################################
