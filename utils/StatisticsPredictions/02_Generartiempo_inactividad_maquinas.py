
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Cargar datos del CSV
df = pd.read_csv('C:/Users/mottu/PycharmProjects/ProductionControlSystem/utils/DATA/02_tiempo_inactividad_maquinas.csv')

# Convertir fechas a formato datetime
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'], format='%d/%m/%Y %H:%M')
df['fecha_fin'] = pd.to_datetime(df['fecha_fin'], format='%d/%m/%Y %H:%M')

# Calcular tiempo de inactividad en horas
df['duracion_inactividad'] = (df['fecha_fin'] - df['fecha_inicio']).dt.total_seconds() / 3600

# Estadísticas básicas
# 1. Tiempo total de inactividad por máquina
tiempo_inactividad_por_maquina = df.groupby('maquina_id')['duracion_inactividad'].sum()

# 2. Frecuencia de las razones de inactividad
razones_frecuencia = df['razon'].value_counts()

# 3. Tiempo promedio de inactividad por máquina
promedio_inactividad_por_maquina = df.groupby('maquina_id')['duracion_inactividad'].mean()

# 4. Calcular la cantidad total de registros
num_datos = len(df)

# 5. Probabilidad de inactividad por máquina
probabilidad_inactividad = df.groupby('maquina_id').apply(lambda x: len(x) / num_datos)

# ====== Visualización de los resultados ======

# Gráfico 1: Tiempo total de inactividad por máquina
plt.figure(figsize=(10,6))
tiempo_inactividad_por_maquina.plot(kind='bar', color='skyblue')
plt.title('Tiempo total de inactividad por máquina (horas)')
plt.xlabel('ID Máquina')
plt.ylabel('Horas de Inactividad')
plt.xticks(rotation=0)
plt.show()

# Gráfico 2: Frecuencia de las razones de inactividad
plt.figure(figsize=(8,6))
razones_frecuencia.plot(kind='bar', color='salmon')
plt.title('Frecuencia de las razones de inactividad')
plt.xlabel('Razón de Inactividad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=0)
plt.show()

# Gráfico 3: Tiempo promedio de inactividad por máquina
plt.figure(figsize=(10,6))
promedio_inactividad_por_maquina.plot(kind='bar', color='lightgreen')
plt.title('Tiempo promedio de inactividad por máquina (horas)')
plt.xlabel('ID Máquina')
plt.ylabel('Horas Promedio de Inactividad')
plt.xticks(rotation=0)
plt.show()

# Gráfico 4: Probabilidad de inactividad por máquina
plt.figure(figsize=(10,6))
probabilidad_inactividad.plot(kind='bar', color='orange')
plt.title('Probabilidad de inactividad por máquina')
plt.xlabel('ID Máquina')
plt.ylabel('Probabilidad')
plt.xticks(rotation=0)
plt.show()
