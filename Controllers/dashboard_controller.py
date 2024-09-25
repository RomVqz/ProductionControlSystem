from models.dashboard_model import StatisticsModel
from gui.windows.dashboard_view import StatisticsView

class StatisticsController:
    def __init__(self, content_frame):  # Constructor corregido
        self.content_frame = content_frame  # Almacenar el frame de contenido
        self.model = StatisticsModel()  # Instanciar el modelo
        self.view = StatisticsView(content_frame, self)  # Usar content_frame en lugar de root

    def get_view(self):
        return self.view.get_frame()  # Retornar el frame de la vista

    def run_production_history(self):
        result = self.model.run_production_history()  # Ejecutar lógica del modelo
        self.view.display_result(result)  # Mostrar el resultado en la vista

    def run_machine_inactivity(self):
        result = self.model.run_machine_inactivity()
        self.view.display_result(result)

    def run_employee_performance(self):
        result = self.model.run_employee_performance()
        self.view.display_result(result)

    def run_production_kpis(self):
        result = self.model.run_production_kpis()
        self.view.display_result(result)

    def show_statistics_view(self):
        self.clear_frames()  # Limpiar vistas existentes
        self.view.get_frame().pack(fill="both", expand=True)  # Empacar la vista actual
        self.view.show()  # Mostrar la vista si hay lógica adicional en show()

    def clear_frames(self):
        """Limpiar todos los widgets del content_frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Destruir los widgets existentes
