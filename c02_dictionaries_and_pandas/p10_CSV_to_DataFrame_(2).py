# Ejercicio
# CSV a DataFrame (2)

# Descripción:
# La llamada a `read_csv()` para importar los datos del CSV no generó un error,
# pero la salida no es exactamente lo que queríamos. Las etiquetas de fila 
# se importaron como otra columna sin nombre.
# 
# ¿Recuerdas `index_col`, un argumento de `read_csv()` que puedes usar 
# para especificar qué columna en el archivo CSV debe usarse como etiquetas de fila?
# ¡Exactamente eso es lo que necesitas aquí!
#
# El código Python que resuelve el ejercicio anterior ya está incluido;
# ¿puedes hacer los cambios apropiados para corregir la importación de datos?

# Instrucciones:
# 1. Ejecuta el código con "Run Code" y confirma que la primera columna 
#    debería usarse como etiquetas de fila.
# 2. Especifica el argumento `index_col` dentro de `pd.read_csv()`: 
#    establécelo en `0` para que la primera columna se use como etiquetas de fila.
# 3. ¿Ha mejorado la impresión de `cars` ahora?

# Código en Python
# Importar pandas como pd
import pandas as pd  # Importa la biblioteca pandas

# Corregir la importación incluyendo index_col
cars = pd.read_csv('cars.csv', index_col=0)  # Lee el archivo CSV 'cars.csv' usando la primera columna como índice

# Imprimir cars
print(cars)  # Muestra el DataFrame cars para verificar que se haya cargado correctamente con la primera columna como índice