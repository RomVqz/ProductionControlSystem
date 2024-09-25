from models.material_model import MaterialModel
from gui.windows.material_view import MaterialView

class MaterialController:
    def __init__(self, root):
        self.model = MaterialModel()
        self.view = MaterialView(root)
        self.view.setup_ui(self)

        # Mostrar los materiales al iniciar
        self.show_items()

    def show_items(self):
        """Muestra los materiales."""
        data = self.model.get_materia_prima()
        self.view.display_materia_prima(data)

    def search(self):
        """Realiza la búsqueda en los materiales."""
        query = self.view.search_entry.get()
        column = self.view.filter_combobox.get().lower()
        data = self.model.search_materia_prima(query, column)
        self.view.display_materia_prima(data)

    def create_item(self):
        """Lógica para crear un nuevo material."""
        # Ejemplo: Código para solicitar inputs y agregar un nuevo material
        pass

    def update_item(self):
        """Lógica para actualizar un material existente."""
        pass

    def delete_item(self):
        """Lógica para eliminar un material."""
        pass

    def get_view(self):
        return self.view.get_frame()
