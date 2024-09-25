
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime

# Cargar datos del CSV
df = pd.read_csv('C:/Users/mottu/PycharmProjects/ProductionControlSystem/utils/DATA/03_Rendimiento_empleados.csv')

# Convertir fechas a formato datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# Estadísticas básicas
# 1. Cumplimiento de órdenes promedio por producto
cumplimiento_por_producto = df.groupby('producto_id')['cumplimiento_ordenes'].mean()

# 2. Eficiencia de producción promedio por turno
eficiencia_por_turno = df.groupby('turno_mas_productivo')['eficiencia_produccion'].mean()

# 3. Costo promedio por unidad por producto
costo_por_producto = df.groupby('producto_id')['costo_por_unidad'].mean()

# 4. Defectos promedio por unidad por producto
defectos_por_producto = df.groupby('producto_id')['defectos_por_unidad'].mean()

# ====== Visualización de los resultados ======

# Gráfico 1: Cumplimiento de órdenes promedio por producto
plt.figure(figsize=(10,6))
cumplimiento_por_producto.plot(kind='bar', color='lightblue')
plt.title('Cumplimiento de órdenes promedio por producto')
plt.xlabel('Producto')
plt.ylabel('Cumplimiento (%)')
plt.xticks(rotation=0)
plt.show()

# Gráfico 2: Eficiencia de producción promedio por turno
plt.figure(figsize=(8,6))
eficiencia_por_turno.plot(kind='bar', color='green')
plt.title('Eficiencia de producción promedio por turno')
plt.xlabel('Turno')
plt.ylabel('Eficiencia')
plt.xticks(rotation=0)
plt.show()

# Gráfico 3: Costo promedio por unidad por producto
plt.figure(figsize=(8,6))
costo_por_producto.plot(kind='bar', color='orange')
plt.title('Costo promedio por unidad por producto')
plt.xlabel('Producto')
plt.ylabel('Costo por unidad (MXN)')
plt.xticks(rotation=0)
plt.show()

# Gráfico 4: Defectos promedio por unidad por producto
plt.figure(figsize=(8,6))
defectos_por_producto.plot(kind='bar', color='red')
plt.title('Defectos promedio por unidad por producto')
plt.xlabel('Producto')
plt.ylabel('Defectos por unidad')
plt.xticks(rotation=0)
plt.show()

# Predicción (Modelo básico de tendencia)
# Usamos una regresión lineal para predecir el cumplimiento de órdenes futuras

# Convertimos las fechas a formato numérico para el modelo
df['fecha_num'] = df['fecha'].map(datetime.toordinal)

# Definimos las variables X (fecha) e y (cumplimiento de órdenes)
X = df[['fecha_num']]
y = df['cumplimiento_ordenes']

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Hacemos predicciones para las próximas 30 fechas
fechas_futuras = pd.date_range(start=df['fecha'].max(), periods=30, freq='D')
fechas_futuras_ordinal = fechas_futuras.map(datetime.toordinal)
predicciones = modelo.predict(np.array(fechas_futuras_ordinal).reshape(-1, 1))

# Graficar las predicciones
plt.figure(figsize=(10,6))
plt.plot(df['fecha'], df['cumplimiento_ordenes'], label='Datos históricos', color='blue')
plt.plot(fechas_futuras, predicciones, label='Predicción', color='red', linestyle='--')
plt.title('Predicción de cumplimiento de órdenes')
plt.xlabel('Fecha')
plt.ylabel('Cumplimiento (%)')
plt.xticks(rotation=45)
plt.legend()
plt.show()
