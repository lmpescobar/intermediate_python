# Ejercicio: Uso de la sentencia `if` en Python

# Descripción:
# Vamos a explorar la sentencia `if`, que se utiliza para ejecutar un bloque de código
# solo si se cumple una condición específica. En este ejercicio, tenemos dos variables
# `room` y `area`. `room` indica la habitación en la que nos encontramos y `area` es
# el área de esa habitación. Usaremos sentencias `if` para verificar ciertas condiciones
# sobre estas variables.

# Instrucciones:
# 1. Examina la sentencia `if` que imprime "looking around in the kitchen." si `room` es igual a "kit".
# 2. Escribe otra sentencia `if` que imprima "big place!" si `area` es mayor que 15.

# Código en Python

# Definir variables
room = "kit"  # Variable que indica la habitación en la que estamos (kit = cocina)
area = 14.0   # Variable que indica el área de la habitación en metros cuadrados

# Sentencia if para la variable room
if room == "kit":  # Verifica si la variable `room` es igual a "kit"
    print("looking around in the kitchen.")  # Imprime un mensaje si la condición se cumple

# Sentencia if para la variable area
if area > 15:  # Verifica si el valor de `area` es mayor que 15
    print("big place!")  # Imprime un mensaje si la condición se cumple

# Explicación del código:
# 1. Se definió la variable `room` con el valor "kit", que indica que estamos en la cocina.
# 2. Se definió la variable `area` con un valor de 14.0, que representa el área de la cocina.
# 3. La primera sentencia `if` verifica si la variable `room` es igual a "kit" y, si es así,
#    imprime el mensaje "looking around in the kitchen.".
# 4. La segunda sentencia `if` verifica si el valor de `area` es mayor que 15. Si la condición
#    se cumple, imprime el mensaje "big place!". En este caso, no se imprime porque el área es 14.