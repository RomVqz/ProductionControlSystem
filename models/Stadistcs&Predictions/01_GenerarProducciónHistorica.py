
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos generados
df = pd.read_csv('C:/Users/mottu/Documents/NTT/Equipo/CSV/produccion_historica.csv')

# Estadísticas: Producción diaria, semanal, mensual
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# 1. Producción diaria
produccion_diaria = df.groupby('fecha')['cantidad_producida'].sum()
produccion_diaria.plot(kind='line', title='Producción Diaria', xlabel='Fecha', ylabel='Cantidad Producida')
plt.show()

# 2. Producción mensual
df['mes'] = df['fecha'].dt.to_period('M')
produccion_mensual = df.groupby('mes')['cantidad_producida'].sum()
produccion_mensual.plot(kind='bar', title='Producción Mensual', xlabel='Mes', ylabel='Cantidad Producida')
plt.show()

# 3. Comparativa por turnos
produccion_por_turno = df.groupby('turno')['cantidad_producida'].sum()
produccion_por_turno.plot(kind='bar', title='Producción por Turno', xlabel='Turno', ylabel='Cantidad Producida')
plt.show()

# 4. Comparativa por planta
produccion_por_planta = df.groupby('planta')['cantidad_producida'].sum()
produccion_por_planta.plot(kind='bar', title='Producción por Planta', xlabel='Planta', ylabel='Cantidad Producida')
plt.show()

# Predicciones sencillas con base en la tendencia
# Predicción de la cantidad de producción a lo largo del tiempo (usamos los días como variables independientes)
df['dias'] = (df['fecha'] - df['fecha'].min()).dt.days
X = df[['dias']]
y = df['cantidad_producida']

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción para los próximos 7 días
dias_futuros = np.array([[x] for x in range(df['dias'].max() + 1, df['dias'].max() + 8)])
predicciones = modelo.predict(dias_futuros)

# Graficar la predicción con mejoras en la legibilidad
plt.figure(figsize=(10, 6))

# Graficar los últimos 30 días reales para hacer la comparación más clara
plt.plot(df['dias'][-30:], y[-30:], label='Datos Reales (últimos 30 días)', marker='o')

# Graficar las predicciones para los próximos 7 días
plt.plot(dias_futuros, predicciones, label='Predicciones (próximos 7 días)', linestyle='--', color='red', marker='x')

# Añadir títulos y etiquetas
plt.xlabel('Días desde el inicio del año')
plt.ylabel('Cantidad Producida')
plt.title('Predicción de Producción para los Próximos 7 Días')

# Añadir leyenda
plt.legend()

# Añadir límites para los ejes y mejorar visualización
plt.xlim([df['dias'].max() - 30, df['dias'].max() + 7])
plt.ylim([min(y[-30:]), max(y[-30:]) + 50])

plt.grid(True)
plt.show()
