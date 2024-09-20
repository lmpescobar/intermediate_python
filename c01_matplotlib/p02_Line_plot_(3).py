# Ejercicio: Line plot (3)
# Descripción:
# Ahora que has creado tu primer gráfico de líneas, vamos a trabajar con los datos que el profesor Hans Rosling 
# utilizó para construir su hermoso gráfico de burbujas. Estos datos fueron recolectados en 2007. Dos listas están 
# disponibles para ti:

# - life_exp: contiene la expectativa de vida para cada país.
# - gdp_cap: contiene el PIB per cápita (es decir, por persona) para cada país, expresado en dólares estadounidenses.

# PIB significa Producto Interno Bruto. Básicamente representa el tamaño de la economía de un país. Divide esto 
# por la población y obtendrás el PIB per cápita.

# `matplotlib.pyplot` ya se ha importado como `plt`, por lo que puedes empezar de inmediato.

# Instrucciones:
# 1. Imprime el último elemento tanto de la lista gdp_cap como de la lista life_exp; es información sobre Zimbabue.
# 2. Construye un gráfico de líneas, con gdp_cap en el eje x y life_exp en el eje y.
# 3. No olvides terminar con un comando plt.show() para mostrar realmente el gráfico.

# Código en Python

import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib.pyplot

# Listas de ejemplo con exactamente 80 elementos cada una
gdp_cap = [
    974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927, 29796.04834,
    1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282,
    1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885,
    4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.22272,
    8948.102923, 22833.30851, 35278.41874, 2082.481567, 6025.374752, 6873.262326, 5581.180998, 5728.353514,
    12154.08975, 641.3695236, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442,
    1327.60891, 27538.41188, 518.5420362, 942.6542111, 579.231743, 1201.637154, 3548.330846, 1569.331442,
    36180.78919, 33724.75778, 37506.41907, 28569.7197, 926.1410683, 9269.657808, 28821.0637, 39724.97867,
    2602.394995, 4519.461171, 33859.74835, 37506.41907, 940.905775, 2602.394995, 4519.461171, 33859.74835,
    37506.41907, 2612.394995, 3719.461171, 93859.74835, 33724.75778, 17506.41907, 14269.7197, 1210.1410683
]

life_exp = [
    43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852,
    50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.741, 50.651, 78.553, 72.961, 72.889,
    65.152, 46.388, 46.859, 75.537, 58.042, 70.683, 78.273, 77.338, 81.757, 78.885, 71.338, 74.468, 50.536,
    75.64, 72.466, 61.338, 73.536, 70.61, 79.59, 73.338, 73.536, 60.61, 80.59, 69.83, 74.28, 73.338, 69.62,
    70.98, 70.56, 70.45, 71.38, 70.63, 74.38, 73.63, 75.78, 70.38, 68.38, 70.89, 69.38, 68.38, 66.38, 68.88,
    68.38, 73.38, 72.38, 71.38, 70.38, 68.78, 69.28, 68.88, 68.68, 70.68, 71.68, 72.68
]

# Imprimir el último elemento de gdp_cap y life_exp
print(gdp_cap[-1])  # Imprime el último valor de la lista gdp_cap, correspondiente a Zimbabue.
print(life_exp[-1])  # Imprime el último valor de la lista life_exp, correspondiente a Zimbabue.

# Crear un gráfico de líneas, gdp_cap en el eje x y life_exp en el eje y
plt.plot(gdp_cap, life_exp)  # Crea un gráfico de líneas con gdp_cap en el eje x y life_exp en el eje y.

# Mostrar el gráfico
plt.show()  # Muestra el gráfico generado.