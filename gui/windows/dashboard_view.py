import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


class StatisticsView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent)
        self.controller = controller

        # Título
        tk.Label(self.frame, text="Dashboard de Estadísticas", font=("Arial", 16)).pack(pady=10)

        # Botones para ejecutar los diferentes scripts
        tk.Button(self.frame, text="Generar Producción Histórica", command=self.run_production_history).pack(pady=5)
        tk.Button(self.frame, text="Generar Inactividad de Máquinas", command=self.run_machine_inactivity).pack(pady=5)
        tk.Button(self.frame, text="Generar Rendimiento de Empleados", command=self.run_employee_performance).pack(
            pady=5)
        tk.Button(self.frame, text="Generar KPIs de Producción", command=self.run_production_kpis).pack(pady=5)

    def get_frame(self):
        """Devuelve el marco de esta vista."""
        return self.frame

    def display_result(self, result):
        """Muestra los resultados en el área de texto."""
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def plot_graph(self, figure):
        """Dibuja la gráfica en el dashboard."""
        canvas = FigureCanvasTkAgg(figure, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def run_production_history(self):
        """Ejecuta el script de Producción Histórica y muestra las gráficas."""
        df = pd.read_csv('C:/Users/lenovo/Desktop/NTT/ProductionControlSystem/utils/DATA/01_produccion_historica.csv')
        df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

        # Generar gráficas
        fig, axs = plt.subplots(3, 2, figsize=(12, 8))

        # Producción diaria
        produccion_diaria = df.groupby('fecha')['cantidad_producida'].sum()
        axs[0, 0].plot(produccion_diaria.index, produccion_diaria.values)
        axs[0, 0].set_title('Producción Diaria')
        axs[0, 0].set_xlabel('Fecha')
        axs[0, 0].set_ylabel('Cantidad Producida')

        # Producción mensual
        df['mes'] = df['fecha'].dt.to_period('M')
        produccion_mensual = df.groupby('mes')['cantidad_producida'].sum()
        axs[0, 1].bar(produccion_mensual.index.astype(str), produccion_mensual.values)
        axs[0, 1].set_title('Producción Mensual')
        axs[0, 1].set_xlabel('Mes')
        axs[0, 1].set_ylabel('Cantidad Producida')

        # Comparativa por turnos
        produccion_por_turno = df.groupby('turno')['cantidad_producida'].sum()
        axs[1, 0].bar(produccion_por_turno.index, produccion_por_turno.values)
        axs[1, 0].set_title('Producción por Turno')
        axs[1, 0].set_xlabel('Turno')
        axs[1, 0].set_ylabel('Cantidad Producida')

        # Comparativa por planta
        produccion_por_planta = df.groupby('planta')['cantidad_producida'].sum()
        axs[1, 1].bar(produccion_por_planta.index, produccion_por_planta.values)
        axs[1, 1].set_title('Producción por Planta')
        axs[1, 1].set_xlabel('Planta')
        axs[1, 1].set_ylabel('Cantidad Producida')

        plt.tight_layout()
        self.plot_graph(fig)

    def run_machine_inactivity(self):
        """Ejecuta el script de Inactividad de Máquinas y muestra las gráficas."""
        df = pd.read_csv(
            'C:/Users/lenovo/Desktop/NTT/ProductionControlSystem/utils/DATA/02_tiempo_inactividad_maquinas.csv')
        df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'], format='%d/%m/%Y %H:%M')
        df['fecha_fin'] = pd.to_datetime(df['fecha_fin'], format='%d/%m/%Y %H:%M')
        df['duracion_inactividad'] = (df['fecha_fin'] - df['fecha_inicio']).dt.total_seconds() / 3600

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # Tiempo total de inactividad por máquina
        tiempo_inactividad_por_maquina = df.groupby('maquina_id')['duracion_inactividad'].sum()
        axs[0, 0].bar(tiempo_inactividad_por_maquina.index, tiempo_inactividad_por_maquina.values, color='skyblue')
        axs[0, 0].set_title('Tiempo total de inactividad por máquina (horas)')
        axs[0, 0].set_xlabel('ID Máquina')
        axs[0, 0].set_ylabel('Horas de Inactividad')

        # Frecuencia de las razones de inactividad
        razones_frecuencia = df['razon'].value_counts()
        axs[0, 1].bar(razones_frecuencia.index, razones_frecuencia.values, color='salmon')
        axs[0, 1].set_title('Frecuencia de las razones de inactividad')
        axs[0, 1].set_xlabel('Razón de Inactividad')
        axs[0, 1].set_ylabel('Frecuencia')

        # Tiempo promedio de inactividad por máquina
        promedio_inactividad_por_maquina = df.groupby('maquina_id')['duracion_inactividad'].mean()
        axs[1, 0].bar(promedio_inactividad_por_maquina.index, promedio_inactividad_por_maquina.values,
                      color='lightgreen')
        axs[1, 0].set_title('Tiempo promedio de inactividad por máquina (horas)')
        axs[1, 0].set_xlabel('ID Máquina')
        axs[1, 0].set_ylabel('Horas Promedio de Inactividad')

        # Probabilidad de inactividad por máquina
        probabilidad_inactividad = df.groupby('maquina_id').apply(lambda x: len(x) / len(df))
        axs[1, 1].bar(probabilidad_inactividad.index, probabilidad_inactividad.values, color='orange')
        axs[1, 1].set_title('Probabilidad de inactividad por máquina')
        axs[1, 1].set_xlabel('ID Máquina')
        axs[1, 1].set_ylabel('Probabilidad')

        plt.tight_layout()
        self.plot_graph(fig)

    def run_employee_performance(self):
        """Ejecuta el script de Rendimiento de Empleados y muestra las gráficas."""
        df = pd.read_csv('C:/Users/lenovo/Desktop/NTT/ProductionControlSystem/utils/DATA/03_Rendimiento_empleados.csv')
        df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # Total de órdenes completadas por empleado
        ordenes_por_empleado = df.groupby('empleado_id')['ordenes_completadas'].sum()
        axs[0, 0].bar(ordenes_por_empleado.index, ordenes_por_empleado.values, color='lightblue')
        axs[0, 0].set_title('Órdenes completadas por empleado')
        axs[0, 0].set_xlabel('ID Empleado')
        axs[0, 0].set_ylabel('Órdenes completadas')

        # Eficiencia promedio por turno
        eficiencia_por_turno = df.groupby('turno')['eficiencia'].mean()
        axs[0, 1].bar(eficiencia_por_turno.index, eficiencia_por_turno.values, color='green')
        axs[0, 1].set_title('Eficiencia promedio por turno')
        axs[0, 1].set_xlabel('Turno')
        axs[0, 1].set_ylabel('Eficiencia (%)')

        # Órdenes completadas por día
        ordenes_por_dia = df.groupby('fecha')['ordenes_completadas'].sum()
        axs[1, 0].plot(ordenes_por_dia.index, ordenes_por_dia.values, color='purple')
        axs[1, 0].set_title('Órdenes completadas por día')
        axs[1, 0].set_xlabel('Fecha')
        axs[1, 0].set_ylabel('Órdenes completadas')

        # Predecir y graficar
        # Suponiendo que tienes un modelo de regresión ya ajustado
        # Asegúrate de que `y_pred` tenga la misma longitud que `ordenes_por_dia.index`
        # Si usas un modelo de regresión lineal, verifica cómo estás creando `y_pred`

        # Ejemplo:
        from sklearn.linear_model import LinearRegression

        # X es la cantidad de días desde la primera fecha
        X = np.array((ordenes_por_dia.index - ordenes_por_dia.index[0]).days).reshape(-1, 1)
        y = ordenes_por_dia.values

        model = LinearRegression().fit(X, y)
        y_pred = model.predict(X)

        # Verificar longitud
        print(f"Longitudes: x: {len(ordenes_por_dia.index)}, y: {len(y_pred)}")

        if len(ordenes_por_dia.index) == len(y_pred):
            axs[1, 0].plot(ordenes_por_dia.index, y_pred, color='red', label='Predicción')
            axs[1, 0].legend()
        else:
            print("Error: Las longitudes de las series no coinciden.")

        plt.tight_layout()
        self.plot_graph(fig)

    def run_production_kpis(self):
        """Ejecuta el script de KPIs de Producción y muestra las gráficas."""
        df = pd.read_csv('C:/Users/lenovo/Desktop/NTT/ProductionControlSystem/utils/DATA/04_kpis_produccion.csv')

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # KPIs generales
        # Cambia 'produccion_total' por columnas que existen en tu CSV
        axs[0, 0].bar(['Cumplimiento de Órdenes', 'Eficiencia de Producción'],
                      [df['cumplimiento_ordenes'].mean(), df['eficiencia_produccion'].mean()],
                      color='orange')

        axs[0, 0].set_title('KPIs Generales')
        axs[0, 0].set_ylabel('Valores')

        # Cumplimiento por planta
        cumplimiento_por_producto = df.groupby('producto_id')['cumplimiento_ordenes'].mean()
        axs[0, 1].bar(cumplimiento_por_producto.index, cumplimiento_por_producto.values, color='blue')
        axs[0, 1].set_title('Cumplimiento por Planta')
        axs[0, 1].set_ylabel('Cumplimiento (%)')

        # Eficiencia por turno
        eficiencia_por_turno = df.groupby('turno_mas_productivo')['eficiencia_produccion'].mean()
        axs[1, 0].bar(eficiencia_por_turno.index, eficiencia_por_turno.values, color='cyan')
        axs[1, 0].set_title('Eficiencia por Turno')
        axs[1, 0].set_ylabel('Eficiencia (%)')

        # Tendencia de producción
        df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True)
        produccion_diaria = df.groupby(df['fecha'].dt.date)['cumplimiento_ordenes'].sum()
        axs[1, 1].plot(produccion_diaria.index, produccion_diaria.values, color='green')
        axs[1, 1].set_title('Tendencia de Producción Diaria')
        axs[1, 1].set_xlabel('Fecha')
        axs[1, 1].set_ylabel('Producción')

        plt.tight_layout()
        self.plot_graph(fig)
