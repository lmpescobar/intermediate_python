# Ejercicio
# CSV a DataFrame (1)

# Descripción:
# Colocar datos en un diccionario y luego construir un DataFrame funciona, pero no es muy eficiente.
# ¿Qué pasa si estás trabajando con millones de observaciones?
# En esos casos, los datos generalmente se encuentran disponibles como archivos regulares.
# Uno de esos tipos de archivo es el archivo CSV, que significa "valores separados por comas".
#
# Para importar datos de un archivo CSV a Python como un DataFrame de Pandas, 
# puedes usar `read_csv()`.
# 
# Vamos a explorar esta función con los mismos datos de vehículos de los ejercicios anteriores.
# Esta vez, sin embargo, los datos están disponibles en un archivo CSV llamado `cars.csv`.
# Está disponible en tu directorio de trabajo actual, por lo que la ruta al archivo es simplemente `'cars.csv'`.

# Instrucciones:
# 1. Para importar archivos CSV aún necesitas el paquete pandas; impórtalo como `pd`.
# 2. Usa `pd.read_csv()` para importar los datos de `cars.csv` como un DataFrame. 
#    Guarda este DataFrame como `cars`.
# 3. Imprime `cars`. ¿Todo se ve bien?

# Código en Python
# Importar pandas como pd
import pandas as pd  # Importa la biblioteca pandas

# Importar los datos de cars.csv como DataFrame: cars
cars = pd.read_csv('cars.csv')  # Lee el archivo CSV 'cars.csv' y lo guarda como un DataFrame llamado cars

# Imprimir cars
print(cars)  # Muestra el DataFrame cars para verificar que se haya cargado correctamente