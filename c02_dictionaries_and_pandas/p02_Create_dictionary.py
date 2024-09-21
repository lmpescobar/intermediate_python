# Ejercicio
# Crear un diccionario

# Descripción:
# Las listas `countries` y `capitals` están disponibles nuevamente en el script. 
# Tu tarea es convertir estos datos en un diccionario donde los nombres de los países sean las claves y las capitales sean los valores correspondientes.
# Aquí tienes una receta para crear un diccionario:
# 
# my_dict = {
#    "key1":"value1",
#    "key2":"value2",
# }
# 
# En este ejercicio, tanto las claves como los valores son strings. Este también será el caso para este ejercicio.

# Instrucciones:
# 1. Con las cadenas en `countries` y `capitals`, crea un diccionario llamado `europe` con 4 pares clave-valor.
#    Ten cuidado con las mayúsculas y minúsculas. Asegúrate de usar caracteres en minúsculas en todas partes.
# 2. Imprime el diccionario `europe` para ver si el resultado es lo que esperabas.

# Código en Python
# Definición de las listas de países y capitales
countries = ['spain', 'france', 'germany', 'norway']  # Lista de nombres de países
capitals = ['madrid', 'paris', 'berlin', 'oslo']  # Lista de nombres de capitales correspondientes

# Crear diccionario a partir de las listas countries y capitals
europe = {  # Creación del diccionario europe
    'spain': 'madrid',  # Par clave-valor: país-capital
    'france': 'paris',  # Par clave-valor: país-capital
    'germany': 'berlin',  # Par clave-valor: país-capital
    'norway': 'oslo'  # Par clave-valor: país-capital
}

# Imprimir el diccionario europe
print(europe)  # Muestra el diccionario con los países y sus capitales correspondientes