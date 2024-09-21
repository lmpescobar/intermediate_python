# Ejercicio
# Convertir un diccionario a un DataFrame (1)

# Descripción:
# Pandas es una biblioteca de código abierto que proporciona estructuras de datos de alto rendimiento 
# y fáciles de usar y herramientas de análisis de datos para Python.
# ¡Parece prometedor!
# 
# El DataFrame es una de las estructuras de datos más importantes de Pandas. 
# Básicamente es una forma de almacenar datos tabulares donde se pueden etiquetar las filas y las columnas.
# Una forma de construir un DataFrame es a partir de un diccionario.
# 
# En los ejercicios que siguen, trabajarás con datos de vehículos de diferentes países.
# Cada observación corresponde a un país y las columnas brindan información sobre el número de vehículos 
# por cada mil habitantes, si las personas conducen por la derecha o por la izquierda, y así sucesivamente.
# 
# Tres listas están definidas en el script:
# - `names`, que contiene los nombres de los países para los que hay datos disponibles.
# - `dr`, una lista con valores booleanos que indica si las personas conducen por la izquierda o la derecha en el país correspondiente.
# - `cpc`, el número de vehículos motorizados por cada mil personas en el país correspondiente.
# 
# Cada clave del diccionario es una etiqueta de columna y cada valor es una lista que contiene 
# los elementos de la columna.

# Instrucciones:
# 1. Importa `pandas` como `pd`.
# 2. Usa las listas predefinidas para crear un diccionario llamado `my_dict`. 
#    Debe haber tres pares clave-valor:
#    - Clave `'country'` y valor `names`.
#    - Clave `'drives_right'` y valor `dr`.
#    - Clave `'cars_per_cap'` y valor `cpc`.
# 3. Usa `pd.DataFrame()` para convertir tu diccionario en un DataFrame llamado `cars`.
# 4. Imprime `cars` y observa lo bien que se ve.

# Código en Python
# Listas predefinidas
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']  # Nombres de países
dr = [True, False, False, False, True, True, True]  # Conducen por la derecha (True) o por la izquierda (False)
cpc = [809, 731, 588, 18, 200, 70, 45]  # Vehículos por cada mil personas

# Importar pandas como pd
import pandas as pd  # Importa la biblioteca pandas como el alias pd

# Crear diccionario my_dict con tres pares clave-valor
my_dict = {  # Diccionario con los datos de los países
    'country': names,  # Clave 'country' con la lista names como valor
    'drives_right': dr,  # Clave 'drives_right' con la lista dr como valor
    'cars_per_cap': cpc  # Clave 'cars_per_cap' con la lista cpc como valor
}

# Crear un DataFrame cars a partir de my_dict
cars = pd.DataFrame(my_dict)  # Convierte el diccionario en un DataFrame

# Imprimir cars
print(cars)  # Muestra el DataFrame cars