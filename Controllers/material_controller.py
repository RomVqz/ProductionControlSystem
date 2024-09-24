from models.material_model import MaterialModel
from gui.windows.material_view import MaterialView

class MaterialController:
    def __init__(self, root):
        self.model = MaterialModel()
        self.view = MaterialView(root)
        self.view.setup_ui(self)

        # Define el modo inicial (puede ser materia prima o producto terminado)
        self.mode = "materia_prima"
        self.show_items()

    def show_items(self):
        """Muestra los elementos según el modo."""
        if self.mode == "materia_prima":
            data = self.model.get_materia_prima()
            self.view.display_materia_prima(data)
        else:
            data = self.model.get_producto_terminado()
            self.view.display_producto_terminado(data)

    def search(self):
        """Realiza la búsqueda en función del modo actual."""
        query = self.view.search_entry.get()
        column = self.view.filter_combobox.get().lower()

        if self.mode == "materia_prima":
            data = self.model.search_materia_prima(query, column)
            self.view.display_materia_prima(data)
        else:
            data = self.model.search_producto_terminado(query, column)
            self.view.display_producto_terminado(data)

    def create_item(self):
        """Lógica para crear un nuevo elemento."""
        # Ejemplo: Código para solicitar inputs y agregar un nuevo material
        pass

    def update_item(self):
        """Lógica para actualizar un elemento existente."""
        # Ejemplo: Código para seleccionar y actualizar un material existente
        pass

    def delete_item(self):
        """Lógica para eliminar un elemento."""
        # Ejemplo: Código para eliminar un material existente
        pass

    def get_view(self):
        return self.view.get_frame()
