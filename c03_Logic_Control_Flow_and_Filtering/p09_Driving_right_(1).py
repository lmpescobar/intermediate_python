# Ejercicio: Conducción por la derecha (Driving right)

# Descripción:
# En este ejercicio, vamos a filtrar las observaciones de un DataFrame basado en un array booleano.
# Queremos encontrar todas las observaciones en el DataFrame `cars` donde la columna `drives_right` es `True`,
# es decir, donde los países conducen por la derecha.

# Instrucciones:
# 1. Extrae la columna `drives_right` como una Serie de Pandas y guárdala en la variable `dr`.
# 2. Utiliza `dr`, que es una Serie booleana, para filtrar el DataFrame `cars` y guardar la selección resultante en `sel`.
# 3. Imprime `sel` para verificar que todas las observaciones tienen `drives_right` igual a `True`.

# Código en Python

# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Importar el archivo CSV de datos cars.csv y guardarlo como DataFrame llamado cars
cars = pd.read_csv('../c02_dictionaries_and_pandas/cars.csv', index_col = 0)  # Lee el archivo CSV y usa la primera columna como índice

# Extraer la columna drives_right como Serie y almacenarla en dr
dr = cars["drives_right"]  # Selecciona la columna 'drives_right' como una Serie

# Utilizar dr para seleccionar datos en cars y almacenarlos en sel
sel = cars[dr]  # Filtra el DataFrame cars usando la Serie booleana dr

# Imprimir sel
print(sel)  # Muestra las observaciones del DataFrame cars donde drives_right es True

# Explicación del código:
# 1. Importamos la biblioteca pandas para trabajar con DataFrames.
# 2. Leemos el archivo 'cars.csv' y usamos la primera columna como índice del DataFrame.
# 3. Extraemos la columna 'drives_right' como una Serie y la almacenamos en la variable `dr`.
# 4. Filtramos el DataFrame `cars` utilizando la Serie `dr` y guardamos el resultado en `sel`.
# 5. Imprimimos `sel` para mostrar solo las filas donde `drives_right` es `True`.