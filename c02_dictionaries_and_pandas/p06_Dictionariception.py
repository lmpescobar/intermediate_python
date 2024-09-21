# Ejercicio
# Diccionarios dentro de diccionarios

# Descripción:
# ¿Recuerdas las listas? Pueden contener cualquier cosa, incluso otras listas.
# Bueno, para los diccionarios sucede lo mismo. Los diccionarios pueden contener pares clave-valor 
# donde los valores son nuevamente diccionarios.
# 
# Como ejemplo, observa el script donde se ha codificado otra versión de `europe` 
# - el diccionario con el que has estado trabajando todo el tiempo.
# Las claves siguen siendo los nombres de los países, pero los valores son diccionarios que contienen 
# más información que solo el nombre de la capital.
# 
# Es perfectamente posible encadenar corchetes para seleccionar elementos. 
# Para obtener la población de España desde `europe`, por ejemplo, necesitas:
# 
# europe['spain']['population']

# Instrucciones:
# 1. Usa corchetes encadenados para seleccionar e imprimir el nombre de la capital de Francia.
# 2. Crea un diccionario llamado `data`, con las claves `'capital'` y `'population'`. 
#    Asígnales los valores `'rome'` y `59.83` respectivamente.
# 3. Agrega un nuevo par clave-valor a `europe`; la clave es `'italy'` y el valor es `data`, 
#    el diccionario que acabas de crear.
# 4. Imprime el diccionario `europe` para verificar los cambios.

# Código en Python
# Diccionario de diccionarios
europe = {  # Diccionario con países europeos y sus datos
    'spain': { 'capital':'madrid', 'population':46.77 },
    'france': { 'capital':'paris', 'population':66.03 },
    'germany': { 'capital':'berlin', 'population':80.62 },
    'norway': { 'capital':'oslo', 'population':5.084 }
}

# Imprimir la capital de Francia
print(europe['france']['capital'])  # Muestra la capital de Francia usando corchetes encadenados

# Crear sub-diccionario data
data = {  # Crear diccionario para Italia con capital y población
    'capital': 'rome',
    'population': 59.83
}

# Agregar data a europe bajo la clave 'italy'
europe['italy'] = data  # Añadir el diccionario data bajo la clave 'italy' en el diccionario europe

# Imprimir el diccionario europe actualizado
print(europe)  # Muestra el diccionario europe actualizado con la entrada para Italia