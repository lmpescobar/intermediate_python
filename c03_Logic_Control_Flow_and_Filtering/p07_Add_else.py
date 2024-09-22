# Ejercicio: Añadir la estructura `else` a las condiciones `if` en Python

# Descripción:
# En este ejercicio, vamos a extender la funcionalidad de las estructuras `if` usando `else`.
# La estructura `else` nos permite ejecutar un bloque de código alternativo cuando la condición `if` 
# no se cumple. Esto nos ayuda a manejar diferentes situaciones de manera más eficiente.

# Instrucciones:
# 1. Extiende la estructura `if` para la variable `room` usando `else` para imprimir "looking around elsewhere."
#    si la condición `room == "kit"` es falsa.
# 2. Añade una estructura `else` a la segunda estructura de control `if` para que se imprima "pretty small."
#    si la condición `area > 15` es falsa.

# Código en Python

# Definir variables
room = "kit"  # Variable que indica la habitación en la que estamos (kit = cocina)
area = 14.0   # Variable que indica el área de la habitación en metros cuadrados

# Estructura if-else para la variable room
if room == "kit":  # Verifica si la variable `room` es igual a "kit"
    print("looking around in the kitchen.")  # Imprime un mensaje si la condición se cumple
else:  # Se ejecuta si la condición `room == "kit"` es falsa
    print("looking around elsewhere.")  # Imprime un mensaje alternativo

# Estructura if-else para la variable area
if area > 15:  # Verifica si el valor de `area` es mayor que 15
    print("big place!")  # Imprime un mensaje si la condición se cumple
else:  # Se ejecuta si la condición `area > 15` es falsa
    print("pretty small.")  # Imprime un mensaje alternativo

# Explicación del código:
# 1. Se define la variable `room` con el valor "kit", indicando que estamos en la cocina.
# 2. Se define la variable `area` con un valor de 14.0, que representa el área de la cocina.
# 3. La primera estructura `if-else` verifica si `room` es igual a "kit". Si es cierto, imprime
#    "looking around in the kitchen.". Si no, imprime "looking around elsewhere.".
# 4. La segunda estructura `if-else` verifica si `area` es mayor que 15. Si la condición se cumple,
#    imprime "big place!". Si no, imprime "pretty small.".