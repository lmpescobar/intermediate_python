# Ejercicio: Bucles While Básico

# Descripción:
# Vamos a implementar un sistema básico de control utilizando un bucle `while` para corregir el valor de 
# una variable llamada `offset`. La variable `offset` representa la desviación de un péndulo invertido 
# que debe corregirse hasta llegar a cero (posición perfecta).
# El bucle `while` continuará ejecutándose mientras `offset` no sea igual a 0. En cada iteración,
# imprimiremos "correcting..." y reduciremos el valor de `offset` en 1 hasta que alcance el valor de 0.

# Instrucciones:
# 1. Crea la variable `offset` con un valor inicial de 8.
# 2. Crea un bucle `while` que continúe ejecutándose mientras `offset` no sea igual a 0:
#    2.1. Dentro del bucle, imprime el mensaje "correcting...".
#    2.2. Luego, disminuye el valor de `offset` en 1.
#    2.3. Finalmente, imprime el valor actual de `offset` para ver cómo cambia en cada iteración.

# Código en Python

# Inicializar la variable offset
offset = 8  # Valor inicial de la desviación

# Crear el bucle while
while offset != 0:  # El bucle se ejecuta mientras offset no sea igual a 0
    print("correcting...")  # Imprime el mensaje indicando que se está corrigiendo la desviación
    offset = offset - 1     # Reduce el valor de offset en 1
    print(offset)           # Imprime el valor actual de offset después de reducirlo

# Explicación del código:
# 1. Se inicializa la variable `offset` con un valor de 8.
# 2. Se crea un bucle `while` que se ejecuta mientras el valor de `offset` sea diferente de 0.
# 3. Dentro del bucle:
#    - Se imprime "correcting..." en cada iteración para indicar que se está ajustando el valor de `offset`.
#    - Se disminuye el valor de `offset` en 1 con la expresión `offset = offset - 1`.
#    - Se imprime el nuevo valor de `offset` para observar cómo cambia en cada iteración.
# 4. El bucle finaliza cuando `offset` llega a 0, momento en el cual el bucle `while` deja de ejecutarse.