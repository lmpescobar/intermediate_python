# Ejercicio: Conducción por la derecha (Driving right)

# Descripción:
# En este ejercicio, vamos a simplificar el código para filtrar el DataFrame `cars`
# y seleccionar las filas donde la columna `drives_right` es `True`.
# Anteriormente creamos una variable intermedia `dr`, pero ahora lo haremos en una sola línea.

# Instrucciones:
# 1. Simplifica el código para calcular la variable `sel` directamente, sin usar la variable intermedia `dr`.
# 2. Imprime `sel` para verificar que todas las observaciones tienen `drives_right` igual a `True`.

# Código en Python

# Importar los datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de 'cars.csv' como DataFrame
cars = pd.read_csv('cars.csv', index_col = 0)  # Lee el archivo CSV 'cars.csv' y usa la primera columna como índice

# Convertir el código a una sola línea
sel = cars[cars["drives_right"]]  # Filtra el DataFrame cars donde la columna 'drives_right' es True

# Imprimir sel
print(sel)  # Muestra las observaciones donde 'drives_right' es True

# Explicación del código:
# 1. Importamos la biblioteca pandas para trabajar con DataFrames.
# 2. Leemos el archivo 'cars.csv' y usamos la primera columna como índice del DataFrame.
# 3. Filtramos el DataFrame `cars` en una sola línea, seleccionando solo las filas donde `drives_right` es `True`.
# 4. Imprimimos `sel` para verificar el resultado filtrado.