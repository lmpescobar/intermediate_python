# Ejercicio
# Personalizaciones adicionales en el gráfico de dispersión

# Descripción:
# Vamos a agregar más personalizaciones al gráfico de dispersión, como etiquetas de texto para resaltar países específicos y cuadrículas.
# Usaremos las funciones `plt.text()` para agregar nombres de países y `plt.grid(True)` para agregar líneas de cuadrícula al gráfico.

# Instrucciones:
# 1. Agrega `plt.text()` para mostrar los nombres "India" y "China" en posiciones específicas del gráfico.
# 2. Añade `plt.grid(True)` después de las llamadas a `plt.text()` para que las líneas de la cuadrícula se dibujen en el gráfico.

# Código en Python
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot como plt para generar gráficos
import numpy as np  # Importa la biblioteca numpy y la asigna al alias np

# Lista gdp_cap con 50 datos
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744,
           36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084,
           7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916,
           1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885,
           4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142,
           1544.750112, 14619.22272, 8948.102923, 22833.30851, 35278.41874, 2082.481567,
           6025.374752, 6873.262326, 5581.180998, 5728.353514, 12154.08975, 641.3695236,
           690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442,
           1327.60891, 27538.41188]

# Lista life_exp con 50 datos
life_exp = [43.828, 76.423, 72.301, 42.731, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852,
            50.728, 72.39, 70.616, 75.748, 73.47, 68.123, 78.623, 52.517, 70.198, 49.58,
            59.723, 72.272, 74.02, 55.322, 79.972, 63.536, 70.994, 59.443, 78.885, 80.653,
            44.741, 50.651, 78.242, 75.562, 65.061, 79.267, 56.735, 71.338, 71.878, 51.578,
            58.04, 52.947, 79.313, 80.657, 56.728, 60.974, 45.678, 73.951, 59.443, 48.303]

# Lista pop con 50 datos (población en millones)
pop = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.403452,
       8.078314, 9.119152, 4.552197, 0.301931, 11.068834, 6.337982, 6.19109, 79.481339, 2.133446, 6.830929,
       2.978576, 0.276361, 22.276056, 10.263469, 16.284741, 1318.6831, 44.22755, 0.71096, 1.093718, 3.504344,
       44.664295, 0.191212, 7.939819, 0.479233, 22.44283, 6.426679, 2.780132, 127.467972, 6.217245, 3.270065,
       8.860588, 0.456351, 5.133052, 4.139314, 0.581424, 3.61885, 34.859424, 3.600523, 1.325252, 0.297779]

# Lista col con colores según continente
col = ['red', 'green', 'blue', 'yellow', 'black', 'red', 'green', 'blue', 'yellow', 'black',
       'red', 'green', 'blue', 'yellow', 'black', 'red', 'green', 'blue', 'yellow', 'black',
       'red', 'green', 'blue', 'yellow', 'black', 'red', 'green', 'blue', 'yellow', 'black',
       'red', 'green', 'blue', 'yellow', 'black', 'red', 'green', 'blue', 'yellow', 'black',
       'red', 'green', 'blue', 'yellow', 'black', 'red', 'green', 'blue', 'yellow', 'black']

# Crear gráfico de dispersión con datos, tamaño y color de puntos según la población y continente
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)  # Ajusta el color y la transparencia con alpha

# Personalizaciones previas
plt.xscale('log')  # Establece la escala logarítmica en el eje x
plt.xlabel('GDP per Capita [in USD]')  # Asigna la etiqueta al eje x
plt.ylabel('Life Expectancy [in years]')  # Asigna la etiqueta al eje y
plt.title('World Development in 2007')  # Asigna el título al gráfico
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])  # Reemplazar valores por etiquetas

# Personalizaciones adicionales
plt.text(1550, 71, 'India')  # Agrega el texto "India" en el punto específico
plt.text(5700, 80, 'China')  # Agrega el texto "China" en el punto específico

# Agregar cuadrícula al gráfico
plt.grid(True)  # Activa las líneas de cuadrícula

# Mostrar el gráfico después de personalizarlo
plt.show()  # Muestra el gráfico de dispersión con las etiquetas de los ticks personalizadas y la cuadrícula