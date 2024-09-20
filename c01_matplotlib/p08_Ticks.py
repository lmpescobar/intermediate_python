# Ejercicio
# Personalizar un gráfico de dispersión: Ajuste de Ticks

# Descripción:
# Vamos a ajustar las etiquetas (ticks) del eje x para mejorar la legibilidad del gráfico de dispersión.
# Utilizaremos la función xticks() para reemplazar los valores numéricos de los ticks con etiquetas de texto
# que representen mejor los datos.

# Instrucciones:
# 1. Utiliza tick_val y tick_lab como entradas en la función xticks() para hacer el gráfico más legible.
# 2. Muestra el gráfico con plt.show() después de haber agregado las personalizaciones.

# Código en Python
# Importar matplotlib.pyplot como plt
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib.pyplot y la asigna al alias plt

# Lista gdp_cap con 142 datos
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744,
           36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084,
           7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916,
           1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885,
           4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142,
           1544.750112, 14619.22272, 8948.102923, 22833.30851, 35278.41874, 2082.481567,
           6025.374752, 6873.262326, 5581.180998, 5728.353514, 12154.08975, 641.3695236,
           690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442,
           1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.231743, 1201.637154,
           3548.330846, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564,
           11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.880262,
           31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.13973, 47306.98978,
           10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101,
           12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.772271,
           9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778,
           36797.93332, 25185.00911, 2749.320965, 619.6768924, 2013.977305, 49357.19017,
           22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016,
           15389.92468, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639,
           1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561, 47143.17964,
           18678.31435, 25768.25759, 926.1410683, 9269.657807, 28821.0637, 3970.095407,
           2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684,
           1107.482182, 7458.396326, 882.9699438, 18008.50924, 7092.923025, 8458.276384,
           1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404,
           3025.349798, 2280.769906, 1271.211593, 469.7092981]

# Lista life_exp con 142 datos
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
            79.441, 72.39, 73.338, 65.161, 56.938, 62.879, 54.791, 59.545, 78.332, 80.941,
            79.441, 72.39]

# Crear gráfico de dispersión básico con escala logarítmica en el eje x
plt.scatter(gdp_cap, life_exp)  # Crea un gráfico de dispersión con los datos de gdp_cap en el eje x y life_exp en el eje y
plt.xscale('log')  # Establece la escala logarítmica en el eje x

# Personalizaciones previas
plt.xlabel('GDP per Capita [in USD]')  # Asigna la etiqueta al eje x
plt.ylabel('Life Expectancy [in years]')  # Asigna la etiqueta al eje y
plt.title('World Development in 2007')  # Asigna el título al gráfico

# Definición de valores y etiquetas de los ticks
tick_val = [1000, 10000, 100000]  # Valores de los ticks en el eje x
tick_lab = ['1k', '10k', '100k']  # Etiquetas de los ticks correspondientes a los valores

# Ajustar los ticks en el eje x
plt.xticks(tick_val, tick_lab)  # Reemplaza los valores de los ticks en el eje x por las etiquetas correspondientes

# Mostrar el gráfico después de personalizarlo
plt.show()  # Muestra el gráfico de dispersión con las etiquetas de los ticks personalizadas