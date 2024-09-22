# Ejercicio
# loc e iloc (2)

# Descripción:
# `loc` e `iloc` también te permiten seleccionar tanto filas como columnas de un DataFrame.
# Para experimentar, prueba los siguientes comandos. De nuevo, los pares de comandos producen el mismo resultado.
#
# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]
#
# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]
#
# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]
#
# Instrucciones:
# 1. Imprime el valor de `drives_right` de la fila correspondiente a Marruecos (su etiqueta de fila es `MOR`).
# 2. Imprime un sub-DataFrame que contenga las observaciones de Rusia y Marruecos y las columnas `country` y `drives_right`.

# Código en Python
# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de cars.csv
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir el valor de drives_right para Marruecos
print(cars.loc['MOR', 'drives_right'])  # Selecciona el valor de la columna 'drives_right' para la fila 'MOR' (Marruecos)

# Imprimir sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])  # Selecciona las filas 'RU' (Rusia) y 'MOR' (Marruecos) y las columnas 'country' y 'drives_right'