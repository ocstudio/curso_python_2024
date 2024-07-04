import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
file_path = '/home/ocstudio/curso_python_2024/Natalidad mortalidad en colombia.csv'  # Reemplaza con la ruta correcta de tu archivo
df = pd.read_csv(file_path)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['año'], df['mortalidad'], marker='o', label='Mortalidad')
plt.plot(df['año'], df['natalidad'], marker='o', label='Natalidad')
plt.xlabel('Año')
plt.ylabel('Tasa por 1000 habitantes')
plt.title('Tasa de Mortalidad y Natalidad en Colombia (2000-2022)')
plt.xticks(df['año'], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
