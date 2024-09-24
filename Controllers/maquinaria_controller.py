from models.maquinaria_model import MaquinariaModel
from gui.windows.maquinaria_view import MaquinariaView

class MaquinariaController:
    def __init__(self, root):
        self.model = MaquinariaModel()
        self.view = MaquinariaView(root)
        self.view.setup_ui(self)

    def show_maquinaria(self):
        """Muestra toda la maquinaria."""
        data = self.model.get_maquinaria()
        self.view.display_maquinaria(data)

    def search_maquinaria(self):
        """Realiza la búsqueda de maquinaria."""
        query = self.view.search_entry.get()
        column = self.view.filter_combobox.get()

        if column == "Seleccionar filtro":
            print("Por favor, selecciona una columna para filtrar.")
            return

        # Obtener los resultados de búsqueda y mostrarlos
        resultados = self.model.search_maquinaria(query, column)
        self.view.display_maquinaria(resultados)

    def create_maquinaria(self):
        """Crea una nueva maquinaria (simulado con valores fijos)."""
        self.model.add_maquinaria(3, "Nueva Maquinaria", "Operativo")
        self.show_maquinaria()

    def update_maquinaria(self):
        """Actualiza una maquinaria (simulado con valores fijos)."""
        self.model.update_maquinaria(1, "Torno Actualizado", "Mantenimiento")
        self.show_maquinaria()

    def delete_maquinaria(self):
        """Elimina una maquinaria (simulado con ID fijo)."""
        self.model.delete_maquinaria(1)
        self.show_maquinaria()

    def get_view(self):
        return self.view.get_frame()
