# Ejercicio
# Corchetes (1)

# Descripción:
# En el video, viste que puedes indexar y seleccionar DataFrames de Pandas de muchas maneras diferentes.
# La forma más simple, pero no la más poderosa, es usar corchetes.
#
# En el código de ejemplo, se importa el mismo archivo `cars.csv` como un DataFrame de Pandas.
# Para seleccionar solo la columna `cars_per_cap` de `cars`, puedes usar:
# 
# cars['cars_per_cap']
# cars[['cars_per_cap']]
#
# La versión de un solo corchete devuelve una Serie de Pandas, la versión de doble corchete devuelve un DataFrame de Pandas.

# Instrucciones:
# 1. Usa corchetes simples para imprimir la columna `country` de `cars` como una Serie de Pandas.
# 2. Usa corchetes dobles para imprimir la columna `country` de `cars` como un DataFrame de Pandas.
# 3. Usa corchetes dobles para imprimir un DataFrame con las columnas `country` y `drives_right` de `cars`, en ese orden.

# Código en Python
# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de cars.csv
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir la columna country como una Serie de Pandas
print(cars['country'])  # Devuelve la columna 'country' como una Serie

# Imprimir la columna country como un DataFrame de Pandas
print(cars[['country']])  # Devuelve la columna 'country' como un DataFrame

# Imprimir un DataFrame con las columnas country y drives_right
print(cars[['country', 'drives_right']])  # Devuelve un DataFrame con las columnas 'country' y 'drives_right'