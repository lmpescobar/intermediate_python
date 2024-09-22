# Ejercicio: Mayor y menor que en Python

# Descripción:
# En el video, Hugo también habló sobre los signos de menor y mayor que, < y > en Python.
# Se pueden combinar con un signo de igual: <= y >=.
# Presta atención: <= es una sintaxis válida, pero =< no lo es.
# Todas las expresiones de Python en el siguiente bloque de código se evalúan como True:
# 3 < 4
# 3 <= 4
# "alpha" <= "beta"
# Recuerda que para la comparación de cadenas de texto, Python determina la relación
# basada en el orden alfabético.

# Instrucciones:
# 1. Escribe expresiones de Python, envueltas en una función print(), para comprobar si:
#    - `x` es mayor o igual que `-10`. La variable `x` ya ha sido definida para ti.
# 2. Escribe expresiones de Python para comprobar si:
#    - `"test"` es menor o igual que `y`. La variable `y` ya ha sido definida para ti.
# 3. Escribe una expresión de Python para comprobar si:
#    - `True` es mayor que `False`.

# Código en Python

# Comparación de enteros
x = -3 * 6  # Calcula el valor de x como -18
print(x >= -10)  # Comprueba si x es mayor o igual que -10

# Comparación de cadenas de texto
y = "test"  # Define la variable y como 'test'
print("test" <= y)  # Comprueba si 'test' es menor o igual que y

# Comparación de booleanos
print(True > False)  # Comprueba si True es mayor que False

# Explicación del código:
# 1. `x >= -10` evalúa si el valor de `x` (que es -18) es mayor o igual a -10.
#    Esto devolverá `False` porque -18 no es mayor o igual que -10.
# 2. `"test" <= y` evalúa si la cadena "test" es menor o igual a la cadena `y` (que también es "test").
#    Esto devolverá `True` porque las dos cadenas son iguales.
# 3. `True > False` evalúa si el valor booleano `True` es mayor que `False`.
#    Esto devolverá `True` porque en Python, `True` se evalúa como 1 y `False` como 0, y 1 es mayor que 0.