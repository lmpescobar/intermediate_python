# Ejercicio
# Manipulación de diccionarios (1)

# Descripción:
# Si sabes cómo acceder a un diccionario, también puedes asignar un nuevo valor a él. Para agregar un nuevo par clave-valor a `europe`, puedes usar algo como esto:
# 
# europe['iceland'] = 'reykjavik'
# 
# Esto agregará el par clave-valor `'iceland': 'reykjavik'` al diccionario `europe`.

# Instrucciones:
# 1. Agrega la clave `'italy'` con el valor `'rome'` al diccionario `europe`.
# 2. Para comprobar que `'italy'` es ahora una clave en `europe`, imprime `italy` en `europe`.
# 3. Agrega otro par clave-valor al diccionario `europe`: `'poland'` es la clave, y `'warsaw'` es el valor correspondiente.
# 4. Imprime el diccionario `europe`.

# Código en Python
# Definición del diccionario europe
europe = {  # Diccionario de países europeos y sus capitales
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# Agregar 'italy' con el valor 'rome' a europe
europe['italy'] = 'rome'  # Añade el par clave-valor 'italy':'rome' al diccionario

# Comprobar que 'italy' está en europe imprimiendo el resultado de la comprobación
print('italy' in europe)  # Verifica si 'italy' es una clave en el diccionario y devuelve True

# Agregar 'poland' con el valor 'warsaw' a europe
europe['poland'] = 'warsaw'  # Añade el par clave-valor 'poland':'warsaw' al diccionario

# Imprimir el diccionario europe actualizado
print(europe)  # Muestra el diccionario actualizado con los nuevos pares clave-valor añadidos