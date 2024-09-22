# Ejercicio
# loc e iloc (1)

# Descripción:
# Con `loc` e `iloc` puedes realizar prácticamente cualquier operación de selección de datos en DataFrames que se te ocurra.
# `loc` se basa en etiquetas, lo que significa que debes especificar filas y columnas basadas en sus etiquetas.
# `iloc` se basa en índices enteros, por lo que debes especificar filas y columnas por su índice entero, como hiciste en el ejercicio anterior.
#
# Prueba los siguientes comandos para experimentar con `loc` e `iloc` para seleccionar observaciones.
# Cada par de comandos a continuación da el mismo resultado.
#
# cars.loc['RU']
# cars.iloc[4]
#
# cars.loc[['RU']]
# cars.iloc[[4]]
#
# cars.loc[['RU', 'AUS']]
# cars.iloc[[4, 1]]
#
# Como antes, el código incluye la importación de los datos de `cars` como un DataFrame de Pandas.

# Instrucciones:
# 1. Usa `loc` o `iloc` para seleccionar la observación correspondiente a Japón como una Serie.
#    La etiqueta de esta fila es `JPN`, el índice es `2`. Asegúrate de imprimir la Serie resultante.
# 2. Usa `loc` o `iloc` para seleccionar las observaciones para Australia y Egipto como un DataFrame.
#    Puedes encontrar sobre las etiquetas/índices de estas filas inspeccionando `cars`.
#    Asegúrate de imprimir el DataFrame resultante.

# Código en Python
# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de cars.csv
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir la observación para Japón
print(cars.iloc[2])  # Selecciona la fila con índice 2 (Japón) y la imprime como una Serie

# Imprimir las observaciones para Australia y Egipto
print(cars.loc[['AUS', 'EG']])  # Selecciona las filas con etiquetas 'AUS' (Australia) y 'EG' (Egipto) y las imprime como un DataFrame