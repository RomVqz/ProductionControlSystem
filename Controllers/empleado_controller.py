from gui.windows.empleado_view import EmpleadoView
from models.empleado_model import EmpleadoModel


class EmpleadoController:
    def __init__(self, root):
        self.model = EmpleadoModel()
        self.view = EmpleadoView(root)
        self.view.setup_ui(self)

    def show_empleados(self):
        """Muestra todos los empleados."""
        empleados = self.model.get_empleados()
        self.view.display_empleados(empleados)

    def search_empleados(self):
        """Realiza la búsqueda de empleados."""
        query = self.view.search_entry.get()
        column = self.view.filter_combobox.get()

        if column == "Seleccionar filtro":
            print("Por favor, selecciona una columna para filtrar.")
            return

        # Obtener los resultados de búsqueda y mostrarlos
        resultados = self.model.search_empleados(query, column)
        self.view.display_empleados(resultados)

    def create_empleado(self):
        """Crea un nuevo empleado (simulado con valores fijos)."""
        self.model.add_empleado(5, "Nuevo Empleado", "Nuevo Puesto")
        self.show_empleados()

    def update_empleado(self):
        """Actualiza un empleado (simulado con valores fijos)."""
        self.model.update_empleado(1, "Juan Actualizado", "Operador Actualizado")
        self.show_empleados()

    def delete_empleado(self):
        """Elimina un empleado (simulado con ID fijo)."""
        self.model.delete_empleado(1)
        self.show_empleados()

    def get_view(self):
        return self.view.get_frame()

