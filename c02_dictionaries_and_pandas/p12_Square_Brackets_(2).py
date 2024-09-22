# Ejercicio
# Corchetes (2)

# Descripción:
# Los corchetes no solo sirven para seleccionar columnas. También puedes usarlos para obtener filas,
# u observaciones, de un DataFrame. La siguiente llamada selecciona las primeras cinco filas del DataFrame `cars`:
#
# cars[0:5]
#
# El resultado es otro DataFrame que contiene solo las filas que especificaste.
#
# Atención: solo puedes seleccionar filas usando corchetes si especificas un rango, como `0:4`.
# Además, estás usando los índices enteros de las filas aquí, no las etiquetas de fila.

# Instrucciones:
# 1. Selecciona las primeras 3 observaciones de `cars` y imprímelas.
# 2. Selecciona la cuarta, quinta y sexta observación, correspondiente a los índices 3, 4 y 5, e imprímelas.

# Código en Python
# Importar datos de cars
import pandas as pd  # Importa la biblioteca pandas

# Leer los datos de cars.csv
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir las primeras 3 observaciones
print(cars[0:3])  # Selecciona las primeras 3 filas (índices 0, 1 y 2) del DataFrame cars

# Imprimir cuarta, quinta y sexta observación
print(cars[3:6])  # Selecciona las filas 3, 4 y 5 del DataFrame cars