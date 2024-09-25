# models/statistics_model.py
import subprocess

class StatisticsModel:
    def __init__(self):
        self.scripts_path = 'StatisticsPredictions/'

    def run_production_history(self):
        result = subprocess.run(['python', f'{self.scripts_path}01_GenerarProducciónHistorica.py'], capture_output=True, text=True)
        return result.stdout

    def run_machine_inactivity(self):
        result = subprocess.run(['python', f'{self.scripts_path}02_GenerarTiempo_inactividad_maquinas.py'], capture_output=True, text=True)
        return result.stdout

    def run_employee_performance(self):
        result = subprocess.run(['python', f'{self.scripts_path}03_GenerarRendimiento_empleados.py'], capture_output=True, text=True)
        return result.stdout

    def run_production_kpis(self):
        result = subprocess.run(['python', f'{self.scripts_path}04_GenerarKpis_produccion.py'], capture_output=True, text=True)
        return result.stdout