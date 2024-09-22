# Ejercicio
# Comparación de igualdad

# Descripción:
# Para verificar si dos valores de Python, o variables, son iguales, puedes usar `==`.
# Para verificar si no son iguales, usa `!=`.
# Aquí tienes algunos ejemplos que todos dan como resultado `True`. Siéntete libre de probarlos:

# 2 == (1 + 1)
# "intermediate" != "python"
# True != False
# "Python" != "python"

# Cuando escribas estas comparaciones en un script, necesitas envolverlas en una función `print()`
# para ver la salida.

# Instrucciones:
# 1. Escribe código para ver si `True` es igual a `False`.
# 2. Escribe código en Python para comprobar si `-5 * 15` no es igual a `75`.
# 3. Pregunta a Python si las cadenas `"pyscript"` y `"PyScript"` son iguales.
# 4. ¿Qué sucede si comparas booleanos e enteros? Escribe código para ver si `True` y `1` son iguales.

# Código en Python

# Comparación de booleanos
print(True == False)  # Compara si True es igual a False. Debería devolver False.

# Comparación de enteros
print(-5 * 15 != 75)  # Compara si -5 * 15 no es igual a 75. Debería devolver True, porque -75 es distinto de 75.

# Comparación de cadenas
print("pyscript" == "PyScript")  # Compara si "pyscript" es igual a "PyScript". Debería devolver False por la diferencia de mayúsculas.

# Comparar un booleano con un entero
print(True == 1)  # Compara si True es igual a 1. Debería devolver True, porque en Python, True es equivalente a 1.