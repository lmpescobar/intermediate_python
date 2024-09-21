# Ejercicio
# Convertir un diccionario a un DataFrame (2)

# Descripción:
# El código Python que resuelve el ejercicio anterior está incluido en el script.
# ¿Has notado que las etiquetas de las filas (es decir, las etiquetas de las diferentes observaciones) 
# se configuraron automáticamente como enteros de 0 a 6?
# 
# Para resolver esto, se ha creado una lista llamada `row_labels`.
# Puedes usarla para especificar las etiquetas de las filas del DataFrame `cars`.
# Haces esto estableciendo el atributo `index` de `cars`, al que puedes acceder como `cars.index`.

# Instrucciones:
# 1. Haz clic en "Run Code" para ver que, efectivamente, las etiquetas de fila no están correctamente configuradas.
# 2. Especifica las etiquetas de las filas estableciendo `cars.index` igual a `row_labels`.
# 3. Imprime `cars` nuevamente y verifica si las etiquetas de fila son correctas esta vez.

# Código en Python
# Importar pandas como pd
import pandas as pd  # Importa la biblioteca pandas

# Crear el DataFrame cars
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']  # Nombres de los países
dr = [True, False, False, False, True, True, True]  # Conducen por la derecha (True) o por la izquierda (False)
cpc = [809, 731, 588, 18, 200, 70, 45]  # Vehículos por cada mil personas
cars_dict = {  # Diccionario con los datos de los países
    'country': names,  # Clave 'country' con la lista names como valor
    'drives_right': dr,  # Clave 'drives_right' con la lista dr como valor
    'cars_per_cap': cpc  # Clave 'cars_per_cap' con la lista cpc como valor
}
cars = pd.DataFrame(cars_dict)  # Convierte el diccionario en un DataFrame

# Imprimir cars
print(cars)  # Muestra el DataFrame cars con los índices predeterminados (0, 1, 2, ...)

# Definir etiquetas de fila
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']  # Definición de etiquetas de fila

# Especificar etiquetas de fila en cars
cars.index = row_labels  # Establecer las etiquetas de fila usando la lista row_labels

# Imprimir cars nuevamente
print(cars)  # Muestra el DataFrame cars con las nuevas etiquetas de fila