# controllers/statistics_controller.py
from models.dashboard_model import StatisticsModel
from gui.windows.dashboard_view import StatisticsView

class StatisticsController:
    def __init__(self, root):
        self.root = root
        self.model = StatisticsModel()
        self.view = StatisticsView(root, self)

    def get_view(self):
        return self.view.get_frame()

    def run_production_history(self):
        result = self.model.run_production_history()
        self.view.display_result(result)

    def run_machine_inactivity(self):
        result = self.model.run_machine_inactivity()
        self.view.display_result(result)

    def run_employee_performance(self):
        result = self.model.run_employee_performance()
        self.view.display_result(result)

    def run_production_kpis(self):
        result = self.model.run_production_kpis()
        self.view.display_result(result)