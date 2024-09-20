# Ejercicio
# Gráfico de línea (1)

# Descripción
# Con matplotlib, puedes crear una gran cantidad de gráficos diferentes en Python. 
# El gráfico más básico es el gráfico de líneas. Aquí se muestra una receta general.

# El Banco Mundial tiene estimaciones de la población mundial para los años 1950 a 2100. 
# Los datos se cargan en tu espacio de trabajo como una lista llamada 'year', y las poblaciones 
# correspondientes como una lista llamada 'pop'.

# Instrucciones
# 1. Imprime el último elemento tanto de la lista 'year' como de la lista 'pop' para ver 
#    cuál es la población estimada para el año 2100. Usa dos funciones 'print()'.
# 2. Antes de comenzar, debes importar 'matplotlib.pyplot' como 'plt'. 
#    'pyplot' es un subpaquete de 'matplotlib', de ahí el punto.
# 3. Usa 'plt.plot()' para crear un gráfico de líneas. 'year' debe mapearse en el eje horizontal, 
#    'pop' en el eje vertical. No olvides terminar con la función 'plt.show()' para mostrar 
#    el gráfico.

# Código en Python

# Importar matplotlib.pyplot como plt
import matplotlib.pyplot as plt  # Se importa el subpaquete pyplot de matplotlib como plt.

# Datos de ejemplo: años y poblaciones
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
pop = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8, 8.5, 9.2, 9.9, 10.4, 10.8, 11.1, 11.3, 11.5]

# Imprimir el último elemento de ambas listas
print(year[-1])  # Se imprime el último año de la lista 'year'.
print(pop[-1])  # Se imprime la última población estimada de la lista 'pop'.

# Crear un gráfico de línea: 'year' en el eje x, 'pop' en el eje y
plt.plot(year, pop)  # Se crea el gráfico de línea con los datos de años y poblaciones.

# Mostrar el gráfico con plt.show()
plt.show()  # Se muestra el gráfico.