# Ejercicio
# Motivación para diccionarios

# Descripción:
# En este ejercicio, vamos a ver por qué los diccionarios son útiles.
# Tenemos dos listas definidas en el script:
# - `countries` contiene los nombres de algunos países europeos.
# - `capitals` enumera los nombres correspondientes de sus capitales.

# Instrucciones:
# 1. Usa el método `index()` en la lista `countries` para encontrar el índice de 'germany'. 
#    Guarda este índice como `ind_ger`.
# 2. Usa `ind_ger` para acceder a la capital de Alemania de la lista `capitals`. Imprímela en la salida.

# Código en Python
# Definición de los países y sus capitales
countries = ['spain', 'france', 'germany', 'norway']  # Lista de países europeos
capitals = ['madrid', 'paris', 'berlin', 'oslo']  # Lista de capitales correspondientes a cada país

# Obtener el índice de 'germany' y almacenarlo en ind_ger
ind_ger = countries.index('germany')  # Utiliza el método index() para encontrar el índice de 'germany'

# Usar ind_ger para imprimir la capital de Alemania
print(capitals[ind_ger])  # Imprime el valor en la posición ind_ger de la lista capitals, que es 'berlin'