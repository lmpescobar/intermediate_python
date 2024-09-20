# Ejercicio
# Construir un histograma (1)

# Descripción:
# life_exp, es una lista que contiene datos sobre la expectativa de vida de diferentes países en 2007.
# Vamos a crear un histograma de life_exp para visualizar cómo está distribuida la expectativa de vida.

# Instrucciones:
# 1. Utiliza plt.hist() para crear un histograma de los valores en life_exp. No especifiques el número de bins;
#    Python establecerá el número de bins en 10 por defecto.
# 2. Añade plt.show() para mostrar el histograma. ¿Puedes decir cuál bin contiene más observaciones?

# Código en Python
# Importar matplotlib.pyplot como plt
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib.pyplot y la asigna al alias plt

# Lista con la expectativa de vida en diferentes países en 2007
life_exp = [43.828, 76.423, 72.301, 42.731, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852,
            50.728, 72.39, 70.616, 75.748, 73.47, 68.123, 78.623, 52.517, 70.198, 49.58,
            59.723, 72.272, 74.02, 55.322, 79.972, 63.536, 70.994, 59.443, 78.885, 80.653,
            44.741, 50.651, 78.242, 75.562, 65.061, 79.267, 56.735, 71.338, 71.878, 51.578,
            58.04, 52.947, 79.313, 80.657, 56.728, 60.974, 45.678, 73.951, 59.443, 48.303,
            74.241, 54.467, 72.33, 69.19, 59.276, 64.164, 72.801, 63.212, 74.32, 62.761,
            72.39, 70.259, 75.364, 58.065, 68.48, 75.884, 62.69, 71.777, 80.546, 32.978,
            75.748, 56.007, 46.388, 60.916, 70.616, 58.405, 73.67, 57.227, 59.515, 55.785,
            78.7, 60.916, 63.8, 70.615, 64.286, 79.762, 81.235, 78.242, 79.829, 75.635,
            64.299, 72.686, 72.852, 74.213, 72.899, 59.545, 62.398, 57.753, 58.302, 71.878,
            78.332, 80.941, 59.273, 77.926, 61.929, 65.386, 78.691, 79.394, 78.332, 74.847,
            61.537, 51.542, 78.593, 75.878, 58.615, 69.819, 63.479, 77.906, 66.803, 82.207,
            73.927, 71.73, 73.338, 65.161, 56.938, 62.879, 54.791, 59.545, 78.332, 80.941,
            79.441, 72.39, 74.213, 79.829, 79.313, 78.242, 78.242, 78.242, 75.479, 79.762,
            81.235, 75.489, 78.332, 78.242, 72.906, 79.829, 79.762, 79.829, 74.94, 74.847,
            74.217, 79.267, 77.926, 79.441, 79.394, 79.441, 79.762, 79.979, 81.235, 77.906,
            77.926, 79.891, 79.441, 79.829, 79.313, 75.748, 75.314, 80.721, 81.235, 79.441,
            76.805, 79.829, 78.691, 75.314, 78.332, 79.829, 80.942, 79.441, 76.423, 79.441,
            77.932, 75.314, 79.762, 75.788, 79.829, 77.906, 78.242, 78.242, 80.546, 75.748]

# Crear histograma de los datos de life_exp
plt.hist(life_exp)  # Crea un histograma con los valores de la lista life_exp

# Mostrar histograma
plt.show()  # Muestra el histograma creado en la línea anterior

# Impresiones o resultados:
# Se mostrará un histograma con 10 barras por defecto. El bin con más observaciones será el que tenga la barra más alta.