# Ejercicio
# loc e iloc (3)

# Descripción:
# También es posible seleccionar solo columnas con `loc` e `iloc`.
# En ambos casos, simplemente coloca un corte desde el principio hasta el final antes de la coma:
#
# cars.loc[:, 'country']
# cars.iloc[:, 1]
#
# cars.loc[:, ['country', 'drives_right']]
# cars.iloc[:, [1, 2]]

# Instrucciones:
# 1. Imprime la columna `drives_right` como una Serie usando `loc` o `iloc`.
# 2. Imprime la columna `drives_right` como un DataFrame usando `loc` o `iloc`.
# 3. Imprime ambas columnas `cars_per_cap` y `drives_right` como un DataFrame usando `loc` o `iloc`.

# Código en Python
# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de cars.csv
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir la columna drives_right como Serie
print(cars.loc[:, 'drives_right'])  # Selecciona toda la columna 'drives_right' como una Serie usando loc

# Imprimir la columna drives_right como DataFrame
print(cars.loc[:, ['drives_right']])  # Selecciona toda la columna 'drives_right' como un DataFrame usando loc

# Imprimir las columnas cars_per_cap y drives_right como DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])  # Selecciona las columnas 'cars_per_cap' y 'drives_right' como un DataFrame usando loc