# Ejercicio: Personalizar aún más usando `elif`

# Descripción:
# En este ejercicio, vamos a usar la estructura de control `elif` para manejar múltiples condiciones.
# La estructura `elif` (else if) permite evaluar varias condiciones, ejecutando el bloque de código
# correspondiente a la primera condición que sea verdadera.

# Instrucciones:
# 1. Agrega una condición `elif` a la estructura de control para la variable `room` que verifique si 
#    `room` es igual a "bed" e imprime "looking around in the bedroom.".
# 2. Añade una condición `elif` a la estructura de control para la variable `area` que verifique si 
#    `area` es mayor que 10 e imprime "medium size, nice!".
# 3. La estructura debe manejar diferentes valores para `room` y `area` con mensajes personalizados.

# Código en Python

# Definir variables
room = "bed"  # Variable que indica la habitación en la que estamos (bed = dormitorio)
area = 14.0   # Variable que indica el área de la habitación en metros cuadrados

# Estructura if-elif-else para la variable room
if room == "kit":  # Verifica si la variable `room` es igual a "kit" (cocina)
    print("looking around in the kitchen.")  # Imprime un mensaje si la condición se cumple
elif room == "bed":  # Verifica si la variable `room` es igual a "bed" (dormitorio)
    print("looking around in the bedroom.")  # Imprime un mensaje alternativo si la condición se cumple
else:  # Se ejecuta si ninguna de las condiciones anteriores es verdadera
    print("looking around elsewhere.")  # Imprime un mensaje alternativo

# Estructura if-elif-else para la variable area
if area > 15:  # Verifica si el valor de `area` es mayor que 15
    print("big place!")  # Imprime un mensaje si la condición se cumple
elif area > 10:  # Verifica si el valor de `area` es mayor que 10 y menor o igual a 15
    print("medium size, nice!")  # Imprime un mensaje si la condición se cumple
else:  # Se ejecuta si ninguna de las condiciones anteriores es verdadera
    print("pretty small.")  # Imprime un mensaje alternativo

# Explicación del código:
# 1. Se define la variable `room` con el valor "bed", indicando que estamos en el dormitorio.
# 2. Se define la variable `area` con un valor de 14.0, que representa el área del dormitorio.
# 3. La primera estructura `if-elif-else` verifica si `room` es igual a "kit" (cocina), si es "bed" 
#    (dormitorio) o si es otro valor, imprimiendo un mensaje específico para cada caso.
# 4. La segunda estructura `if-elif-else` verifica si `area` es mayor que 15, si es mayor que 10, 
#    o si es menor o igual a 10, imprimiendo un mensaje personalizado en cada caso.