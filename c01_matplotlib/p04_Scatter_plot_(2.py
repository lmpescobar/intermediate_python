# Ejercicio: Gráfico de dispersión (2)

# Descripción:
# En el ejercicio anterior, viste que un mayor PIB generalmente corresponde a una mayor esperanza de vida.
# En otras palabras, existe una correlación positiva.
# ¿Crees que hay una relación entre la población y la esperanza de vida de un país?
# La lista `life_exp` del ejercicio anterior ya está disponible.
# Además, ahora también está disponible `pop`, que enumera las poblaciones correspondientes para los países en 2007.
# Las poblaciones están en millones de personas.

# Instrucciones:
# 1. Comienza desde cero: importa `matplotlib.pyplot` como `plt`.
# 2. Construye un gráfico de dispersión, donde `pop` esté en el eje horizontal y `life_exp` en el eje vertical.
# 3. Termina el script con `plt.show()` para mostrar el gráfico. ¿Ves alguna correlación?

# Código en Python:

# Importar paquete
import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot con el alias plt.

# Datos (pop y life_exp con 80 elementos cada uno)
pop = [
    31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.228744,
    8.078314, 9.119152, 4.552198, 2.01372, 0.301931, 1.056608, 14.280746, 18.013409, 4.12533, 22.233123,
    10.312344, 16.124756, 2.317657, 8.663387, 0.86879, 6.602224, 7.496992, 9.100565, 7.827661, 21.810065,
    4.13956, 16.284941, 14.377704, 8.939501, 3.738428, 0.49499, 0.627292, 9.119152, 2.105003, 2.009245,
    7.454648, 1.384897, 9.346647, 1.273096, 1.030803, 4.01722, 4.150888, 5.701579, 10.637429, 8.759504,
    1.493055, 1.093555, 4.133884, 1.168674, 3.195157, 3.839944, 1.51433, 1.379843, 8.603805, 3.35556,
    2.686786, 4.574128, 8.784495, 5.515125, 2.722453, 1.340883, 5.794515, 2.581416, 4.832065, 5.118067,
    8.063203, 2.01962, 2.033521, 1.35189, 1.137762, 1.025817, 2.014287, 0.610635, 3.405316, 4.587424
]

life_exp = [
    43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
    56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 72.89,
    70.198, 73.923, 76.384, 73.749, 70.665, 71.338, 71.164, 72.801, 73.518, 78.332,
    71.866, 75.64, 76.423, 65.593, 72.801, 50.74, 78.332, 65.554, 75.635, 71.338,
    73.923, 73.923, 65.593, 74.58, 76.711, 78.242, 74.852, 74.05, 75.32, 78.242,
    68.15, 72.301, 75.64, 72.301, 78.242, 50.74, 65.593, 65.593, 65.593, 65.593,
    74.852, 70.665, 70.665, 76.423, 72.301, 75.64, 75.64, 65.593, 76.711, 73.005,
    73.005, 75.32, 50.74, 76.423, 75.32, 75.32, 78.332, 50.74, 76.711, 78.242,
]

# Construir gráfico de dispersión
plt.scatter(pop, life_exp)  # Crear un gráfico de dispersión con pop en el eje x y life_exp en el eje y.

# Mostrar el gráfico
plt.show()  # Mostrar el gráfico generado.