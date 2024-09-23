
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime  # Importación correcta de datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar datos del CSV
df = pd.read_csv('C:/Users/mottu/Documents/NTT/Equipo/CSV/rendimiento_empleados.csv')

# Convertir fechas a formato datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# Estadísticas básicas
# 1. Total de órdenes completadas por empleado
ordenes_por_empleado = df.groupby('empleado_id')['ordenes_completadas'].sum()

# 2. Eficiencia promedio por turno
eficiencia_por_turno = df.groupby('turno')['eficiencia'].mean()

# 3. Órdenes completadas por turno
ordenes_por_turno = df.groupby('turno')['ordenes_completadas'].sum()

# 4. Órdenes completadas por día (serie temporal)
ordenes_por_dia = df.groupby('fecha')['ordenes_completadas'].sum()

# ====== Visualización de los resultados ======

# Gráfico 1: Total de órdenes completadas por empleado
plt.figure(figsize=(10,6))
ordenes_por_empleado.plot(kind='bar', color='lightblue')
plt.title('Órdenes completadas por empleado')
plt.xlabel('ID Empleado')
plt.ylabel('Órdenes completadas')
plt.xticks(rotation=90)
plt.show()

# Gráfico 2: Eficiencia promedio por turno
plt.figure(figsize=(8,6))
eficiencia_por_turno.plot(kind='bar', color='green')
plt.title('Eficiencia promedio por turno')
plt.xlabel('Turno')
plt.ylabel('Eficiencia (%)')
plt.xticks(rotation=0)
plt.show()

# Gráfico 3: Órdenes completadas por turno
plt.figure(figsize=(8,6))
ordenes_por_turno.plot(kind='bar', color='orange')
plt.title('Órdenes completadas por turno')
plt.xlabel('Turno')
plt.ylabel('Órdenes completadas')
plt.xticks(rotation=0)
plt.show()

# Gráfico 4: Órdenes completadas por día
plt.figure(figsize=(10,6))
ordenes_por_dia.plot(kind='line', color='purple')
plt.title('Órdenes completadas por día')
plt.xlabel('Fecha')
plt.ylabel('Órdenes completadas')
plt.xticks(rotation=45)
plt.show()

# Predicción (Modelo básico de tendencia)
# Usamos una regresión lineal para predecir el número de órdenes futuras

# Convertimos las fechas a formato numérico para el modelo
df['fecha_num'] = df['fecha'].map(datetime.toordinal)

# Definimos las variables X (fecha) e y (órdenes completadas)
X = df[['fecha_num']]
y = df['ordenes_completadas']

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Hacemos predicciones para las próximas 30 fechas
fechas_futuras = pd.date_range(start=df['fecha'].max(), periods=30, freq='D')
fechas_futuras_ordinal = fechas_futuras.map(datetime.toordinal)
predicciones = modelo.predict(np.array(fechas_futuras_ordinal).reshape(-1, 1))

# Graficar las predicciones
plt.figure(figsize=(10,6))
plt.plot(df['fecha'], df['ordenes_completadas'], label='Datos históricos', color='blue')
plt.plot(fechas_futuras, predicciones, label='Predicción', color='red', linestyle='--')
plt.title('Predicción de órdenes completadas')
plt.xlabel('Fecha')
plt.ylabel('Órdenes completadas')
plt.xticks(rotation=45)
plt.legend()
plt.show()
