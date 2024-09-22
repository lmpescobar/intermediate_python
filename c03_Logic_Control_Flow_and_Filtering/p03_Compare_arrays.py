# Ejercicio: Comparar arrays con NumPy

# Descripción:
# Puedes usar operadores de comparación con arreglos de NumPy para comparar valores elemento por elemento.
# En este ejercicio, se tienen dos arrays de NumPy: `my_house` y `your_house`, que contienen los valores de
# las áreas de distintas habitaciones de dos casas en metros cuadrados (cocina, sala, dormitorio y baño, en ese orden).
# Vamos a responder preguntas sobre estas áreas utilizando operadores de comparación.

# Instrucciones:
# 1. Usando operadores de comparación, genera arrays booleanos que respondan las siguientes preguntas:
#    - ¿Qué áreas en `my_house` son mayores o iguales a 18?
# 2. Compara los dos arrays `my_house` y `your_house` elemento por elemento. ¿Qué áreas en `my_house` 
#    son menores que las de `your_house`?
# 3. Asegúrate de envolver ambos comandos en una declaración `print()` para que puedas inspeccionar el resultado.

# Código en Python

# Crear arreglos
import numpy as np  # Importa la biblioteca NumPy

# Áreas en mi casa: cocina, sala, dormitorio, baño
my_house = np.array([18.0, 20.0, 10.75, 9.50])  
# Áreas en tu casa: cocina, sala, dormitorio, baño
your_house = np.array([14.0, 24.0, 14.25, 9.0])  

# ¿Qué áreas en my_house son mayores o iguales a 18?
print(my_house >= 18)  # Devuelve un array booleano comparando cada área con 18

# ¿Qué áreas en my_house son menores que las de your_house?
print(my_house < your_house)  # Compara cada elemento de my_house con your_house

# Explicación del código:
# 1. `my_house >= 18` crea un array booleano comparando cada valor en `my_house` con 18.
#    El resultado será [True, True, False, False] porque solo las dos primeras áreas son mayores o iguales a 18.
# 2. `my_house < your_house` compara cada valor de `my_house` con el correspondiente valor en `your_house`.
#    El resultado será [False, True, True, False] porque la sala y el dormitorio en `my_house` son menores en comparación.