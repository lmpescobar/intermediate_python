# Ejercicio
# Acceder a un diccionario

# Descripción:
# Si las claves de un diccionario se eligen sabiamente, acceder a los valores de un diccionario es fácil e intuitivo.
# Por ejemplo, para obtener la capital de Francia desde el diccionario `europe` puedes usar:
#
# europe['france']
#
# Aquí, 'france' es la clave y 'paris' es el valor que se devuelve.

# Instrucciones:
# 1. Verifica cuáles son las claves en `europe` llamando al método `keys()` en `europe`.
#    Imprime el resultado.
# 2. Imprime el valor que pertenece a la clave `'norway'`.

# Código en Python
# Definición del diccionario europe
europe = {  # Diccionario de países europeos y sus capitales
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# Imprimir las claves en europe
print(europe.keys())  # Muestra todas las claves en el diccionario europe

# Imprimir el valor que pertenece a la clave 'norway'
print(europe['norway'])  # Muestra la capital de Noruega, que es 'oslo'