# Ejercicio
# Scatter Plot (1)

# Descripción
# Cuando tienes una escala de tiempo en el eje horizontal, el gráfico de líneas es tu amigo. Pero en muchos otros casos,
# cuando estás tratando de evaluar si hay una correlación entre dos variables, por ejemplo, el gráfico de dispersión
# es la mejor opción. A continuación, se muestra un ejemplo de cómo construir un gráfico de dispersión.

# Vamos a continuar con el gráfico de gdp_cap versus life_exp, los datos de PIB per cápita y esperanza de vida para
# diferentes países en 2007. Tal vez un gráfico de dispersión sea una mejor alternativa.

# Nuevamente, el paquete matplotlib.pyplot está disponible como plt.

# Instrucciones
# 1. Cambia el gráfico de líneas que está en el script a un gráfico de dispersión.
# 2. Se hará evidente una correlación cuando muestres el PIB per cápita en una escala logarítmica.
#    Añade la línea plt.xscale('log').
# 3. Termina tu script con plt.show() para mostrar el gráfico.

# Código en Python

# Importar el paquete matplotlib.pyplot como plt
import matplotlib.pyplot as plt

# Listas de datos (80 elementos en cada una)
gdp_cap = [
    974.5803384, 5937.029525999998, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927, 29796.04834,
    1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298802, 12569.85177, 9065.800825, 10680.79282,
    1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.0165362, 1704.063724, 13171.63885,
    4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.22272,
    8948.102923, 22833.30851, 35278.41874, 2082.481567, 6025.374752, 6873.262326, 5581.180998, 5728.353514,
    12154.08975, 641.3695236, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442,
    1327.60891, 27538.41188, 4184.548089, 1201.637154, 3548.330846, 39724.97867, 906.6075822, 1630.512774,
    60457.15626, 2749.320965, 14646.42094, 712.5865077, 10787.97964, 2861.092593, 926.1410683, 3816.044375,
    823.6856205, 9437.372438, 7494.881464, 597.3105033, 9630.595475, 1544.750112, 4791.541786, 1681.632344,
    4056.53213, 21454.00806, 328.8686445, 641.3695236, 7408.905561, 1268.658293, 18987.1374, 25185.00911,
    40106.63266, 1239.730261, 4811.060429, 1091.359778, 3642.928068, 6908.000226, 4519.461171, 10951.47011
]

life_exp = [
    43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852,
    50.728, 72.39, 73.004, 52.295, 49.58, 59.723, 50.43, 80.653, 44.741, 50.651, 78.553, 72.961, 72.889,
    65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.338,
    71.878, 51.578, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007,
    66.465, 70.308, 70.198, 63.537, 71.164, 64.698, 70.616, 70.198, 62.069, 73.537, 75.64, 75.076, 76.442,
    73.923, 72.971, 63.785, 72.307, 54.001, 67.278, 66.803, 77.338, 65.54, 70.742, 70.342, 68.4, 56.66,
    74.658, 78.242, 56.007, 78.22, 79.522, 72.434, 75.748, 76.6, 77.37, 66.003
]

# Crear un gráfico de dispersión con gdp_cap en el eje x y life_exp en el eje y
plt.scatter(gdp_cap, life_exp)

# Poner el eje x en una escala logarítmica
plt.xscale('log')

# Mostrar el gráfico
plt.show()