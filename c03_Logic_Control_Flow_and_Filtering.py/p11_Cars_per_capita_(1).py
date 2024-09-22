# Ejercicio: Coches por cápita (Cars per capita)

# Descripción:
# Vamos a trabajar con el DataFrame `cars` y determinar qué países tienen un número alto de coches por cada mil habitantes.
# Queremos filtrar aquellos países que tienen más de 500 coches por cada mil habitantes.
# Utilizaremos Series booleanas para realizar el filtrado del DataFrame.

# Instrucciones:
# 1. Selecciona la columna `cars_per_cap` del DataFrame `cars` y guárdala como una Series de Pandas en `cpc`.
# 2. Usa `cpc` en combinación con el operador de comparación `>` y 500 para crear una Series booleana `many_cars`,
#    que será `True` para los países con más de 500 coches por cada mil habitantes y `False` en caso contrario.
# 3. Utiliza `many_cars` para filtrar `cars`, de forma similar a lo que hiciste antes, y guarda el resultado en `car_maniac`.
# 4. Imprime `car_maniac` para ver si todo funciona correctamente.

# Código en Python

# Importar los datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de 'cars.csv' como DataFrame
cars = pd.read_csv('cars.csv', index_col = 0)  # Lee el archivo CSV 'cars.csv' y usa la primera columna como índice

# Crear la Series `cpc` con la columna 'cars_per_cap'
cpc = cars['cars_per_cap']  # Selecciona la columna 'cars_per_cap' y la guarda como una Series en cpc

# Crear la Series booleana `many_cars` que identifica los países con más de 500 coches por cada mil habitantes
many_cars = cpc > 500  # Compara cpc con 500, devolviendo True para países con más de 500 coches

# Usar la Series `many_cars` para filtrar el DataFrame `cars`
car_maniac = cars[many_cars]  # Filtra el DataFrame cars usando la Series booleana many_cars

# Imprimir `car_maniac`
print(car_maniac)  # Muestra los países con más de 500 coches por cada mil habitantes

# Explicación del código:
# 1. Importamos la biblioteca pandas para trabajar con DataFrames.
# 2. Leemos el archivo 'cars.csv' y usamos la primera columna como índice del DataFrame.
# 3. Seleccionamos la columna 'cars_per_cap' como una Series y la almacenamos en `cpc`.
# 4. Creamos una Series booleana `many_cars` que contiene `True` para países con más de 500 coches por cada mil habitantes.
# 5. Filtramos el DataFrame `cars` usando `many_cars` y almacenamos el resultado en `car_maniac`.
# 6. Imprimimos `car_maniac` para verificar que se ha filtrado correctamente.