# Ejercicio: and, or, not (1)

# Descripción:
# Los operadores booleanos como `and`, `or` y `not` te permiten combinar valores booleanos
# para realizar consultas más avanzadas sobre tus datos. En este ejercicio, vamos a utilizar
# estos operadores para evaluar diferentes condiciones basadas en el área de la cocina en
# dos casas: `my_kitchen` y `your_kitchen`.

# Instrucciones:
# 1. Escribe expresiones en Python, envueltas en una función `print()`, para verificar si:
#    a) `my_kitchen` es mayor que 10 y menor que 18.
#    b) `my_kitchen` es menor que 14 o mayor que 17.
#    c) El doble del área de `my_kitchen` es menor que el triple del área de `your_kitchen`.
# 2. Asegúrate de que cada expresión esté dentro de un `print()` para poder ver los resultados.

# Código en Python

# Definir variables
my_kitchen = 18.0  # Área de mi cocina
your_kitchen = 14.0  # Área de tu cocina

# ¿my_kitchen es mayor que 10 y menor que 18?
print(my_kitchen > 10 and my_kitchen < 18)  
# Esta expresión devuelve `False` porque my_kitchen no es menor que 18.

# ¿my_kitchen es menor que 14 o mayor que 17?
print(my_kitchen < 14 or my_kitchen > 17)  
# Esta expresión devuelve `True` porque my_kitchen es mayor que 17.

# ¿El doble de my_kitchen es menor que el triple de your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)  
# Esta expresión devuelve `True` porque 36 (doble de 18) es menor que 42 (triple de 14).

# Explicación del código:
# 1. La primera expresión verifica si el valor de `my_kitchen` está en el rango de 10 a 18 (exclusivo).
# 2. La segunda expresión verifica si `my_kitchen` es menor que 14 o mayor que 17. Solo uno de estos
#    necesita ser verdadero para que el resultado sea True.
# 3. La tercera expresión multiplica `my_kitchen` por 2 y `your_kitchen` por 3, luego compara
#    si el resultado de `my_kitchen` es menor que `your_kitchen`.