# Ejercicio
# Manipulación de diccionarios (2)

# Descripción:
# Alguien pensó que sería gracioso alterar tu diccionario cuidadosamente generado.
# Una versión modificada del diccionario `europe` está disponible en el script.
# ¿Puedes limpiarlo? No hagas esto adaptando la definición de `europe`, sino añadiendo comandos de Python al script para actualizar y eliminar pares clave-valor.

# Instrucciones:
# 1. La capital de Alemania no es `'bonn'`; es `'berlin'`. Actualiza su valor.
# 2. Australia no está en Europa, Austria sí lo está. Elimina la clave `'australia'` del diccionario `europe`.
# 3. Imprime el diccionario `europe` para ver si los cambios se reflejan correctamente.

# Código en Python
# Definición del diccionario europe
europe = {  # Diccionario de países europeos y sus capitales
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'bonn',  # La capital de Alemania está incorrecta aquí
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'australia': 'vienna'  # Australia no está en Europa, pero Austria sí lo está
}

# Actualizar la capital de Alemania
europe['germany'] = 'berlin'  # Corrige la capital de Alemania a 'berlin'

# Eliminar Australia del diccionario
del europe['australia']  # Elimina la entrada incorrecta de Australia

# Imprimir el diccionario europe actualizado
print(europe)  # Muestra el diccionario corregido