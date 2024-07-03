import matplotlib.pyplot as plt

# Datos
años = list(range(2000, 2023))
natalidad = [22.11, 21.58, 21.02, 20.44, 19.85, 19.27, 18.69, 18.17, 17.70, 17.28, 16.91, 16.61, 16.34, 16.09, 15.83, 15.59, 15.35, 15.08, 14.84, 14.68, 14.44, 14.20, 13.92]
mortalidad = [5.35, 5.35, 5.26, 5.18, 5.13, 5.07, 5.02, 4.99, 4.95, 4.91, 4.92, 4.95, 4.98, 5.04, 5.11, 5.17, 5.21, 5.25, 5.31, 5.41, 6.61, 7.74, 7.41]

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(años, natalidad, marker='o', linestyle='-', color='b', label='Tasa de natalidad')
plt.plot(años, mortalidad, marker='o', linestyle='-', color='r', label='Tasa de mortalidad')

# Etiquetas y título
plt.xlabel('Año')
plt.ylabel('Tasa')
plt.title('Tasa de Natalidad y Mortalidad en Colombia (2000-2022)')
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
