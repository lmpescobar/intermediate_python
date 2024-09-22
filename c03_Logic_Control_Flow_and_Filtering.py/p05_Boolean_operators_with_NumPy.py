# Ejercicio: Operadores booleanos con NumPy

# Descripción:
# Los operadores booleanos como `and`, `or` y `not` no funcionan directamente con arreglos de NumPy.
# En su lugar, debes utilizar funciones específicas como `np.logical_and()`, `np.logical_or()`
# y `np.logical_not()`. En este ejercicio, vamos a practicar estas funciones para responder
# preguntas sobre las áreas de distintas habitaciones en dos casas (`my_house` y `your_house`).

# Instrucciones:
# 1. Genera arreglos booleanos que respondan las siguientes preguntas:
#    a) ¿Qué áreas en `my_house` son mayores que 18.5 o menores que 10?
#    b) ¿Qué áreas son menores que 11 en ambas, `my_house` y `your_house`?
# 2. Asegúrate de envolver ambos comandos en una instrucción `print()` para poder ver el resultado.

# Código en Python

# Crear arreglos
import numpy as np  # Importa la biblioteca numpy y la asigna al alias np

# Definir el arreglo my_house con las áreas de las habitaciones: cocina, sala, dormitorio y baño
my_house = np.array([18.0, 20.0, 10.75, 9.50])

# Definir el arreglo your_house con las áreas de las mismas habitaciones en otra casa
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# ¿Qué áreas en my_house son mayores que 18.5 o menores que 10?
print(np.logical_or(my_house > 18.5, my_house < 10))
# Esta expresión devuelve un arreglo de valores booleanos donde True indica que el área
# de esa habitación cumple con al menos una de las condiciones.

# ¿Qué áreas son menores que 11 en ambas, my_house y your_house?
print(np.logical_and(my_house < 11, your_house < 11))
# Esta expresión devuelve un arreglo de valores booleanos donde True indica que el área
# de esa habitación cumple con ambas condiciones: es menor a 11 en las dos casas.

# Explicación del código:
# 1. Se importó la biblioteca `numpy` para poder utilizar arreglos y funciones booleanas específicas.
# 2. Se crearon dos arreglos `my_house` y `your_house` con las áreas de diferentes habitaciones.
# 3. Se utilizó `np.logical_or()` para evaluar qué áreas en `my_house` son mayores que 18.5 o menores que 10.
#    El resultado es un arreglo booleano con True donde se cumple al menos una condición.
# 4. Se utilizó `np.logical_and()` para evaluar qué áreas son menores que 11 en ambas casas.
#    El resultado es un arreglo booleano con True donde se cumplen ambas condiciones.