# Ejercicio: Coches por cápita (Parte 2)

# Descripción:
# Vamos a trabajar nuevamente con el DataFrame `cars` para filtrar aquellos países que tienen un número
# de coches por cada mil habitantes (cars_per_cap) entre 100 y 500. 
# Utilizaremos operadores lógicos avanzados para realizar el filtrado del DataFrame.

# Instrucciones:
# 1. Importa la biblioteca pandas como `pd`.
# 2. Importa la biblioteca numpy como `np` (la usaremos para realizar operaciones lógicas).
# 3. Lee los datos del archivo CSV `cars.csv` como un DataFrame llamado `cars`.
# 4. Selecciona la columna `cars_per_cap` del DataFrame `cars` y guárdala como una Series de Pandas en `cpc`.
# 5. Usa `np.logical_and` para crear una Series booleana `between` que sea `True` para los países que tienen 
#    más de 100 y menos de 500 coches por cada mil habitantes, y `False` en caso contrario.
# 6. Usa la Series `between` para filtrar el DataFrame `cars` y guarda el resultado en `medium`.
# 7. Imprime `medium` para ver si todo funciona correctamente.

# Código en Python

# Importar los datos de cars
import pandas as pd  # Importa la biblioteca pandas como pd
import numpy as np   # Importa la biblioteca numpy como np

# Leer los datos de 'cars.csv' como DataFrame
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' y usa la primera columna como índice

# Crear la Series `cpc` con la columna 'cars_per_cap'
cpc = cars['cars_per_cap']  # Selecciona la columna 'cars_per_cap' y la guarda como una Series en cpc

# Crear la Series booleana `between` que identifica los países con más de 100 y menos de 500 coches por cada mil habitantes
between = np.logical_and(cpc > 100, cpc < 500)  # Compara cpc para encontrar valores entre 100 y 500

# Usar la Series `between` para filtrar el DataFrame `cars`
medium = cars[between]  # Filtra el DataFrame cars usando la Series booleana between

# Imprimir `medium`
print(medium)  # Muestra los países con entre 100 y 500 coches por cada mil habitantes

# Explicación del código:
# 1. Importamos la biblioteca pandas y numpy para trabajar con DataFrames y operaciones lógicas.
# 2. Leemos el archivo 'cars.csv' y usamos la primera columna como índice del DataFrame.
# 3. Seleccionamos la columna 'cars_per_cap' como una Series y la almacenamos en `cpc`.
# 4. Creamos una Series booleana `between` que contiene `True` para países con más de 100 y menos de 500 coches.
# 5. Filtramos el DataFrame `cars` usando `between` y almacenamos el resultado en `medium`.
# 6. Imprimimos `medium` para verificar que se ha filtrado correctamente.