# gui/windows/statistics_view.py
import tkinter as tk
from tkinter import ttk

class StatisticsView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent)
        self.controller = controller

        # Título
        tk.Label(self.frame, text="Dashboard de Estadísticas", font=("Arial", 16)).pack(pady=10)

        # Botones para ejecutar los diferentes scripts
        tk.Button(self.frame, text="Generar Producción Histórica", command=self.controller.run_production_history).pack(pady=5)
        tk.Button(self.frame, text="Generar Inactividad de Máquinas", command=self.controller.run_machine_inactivity).pack(pady=5)
        tk.Button(self.frame, text="Generar Rendimiento de Empleados", command=self.controller.run_employee_performance).pack(pady=5)
        tk.Button(self.frame, text="Generar KPIs de Producción", command=self.controller.run_production_kpis).pack(pady=5)

        # Área de texto para mostrar resultados
        self.text_area = tk.Text(self.frame, height=15, width=60)
        self.text_area.pack(pady=10)

    def display_result(self, result):
        """Muestra los resultados en el área de texto."""
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def get_frame(self):
        return self.frame