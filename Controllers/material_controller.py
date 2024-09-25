# controllers/materiales_controller.py

from models.material_model import MaterialsModel
from gui.windows.material_view import MaterialsView
import tkinter as tk
from tkinter import messagebox

class MaterialsController:
    def __init__(self, root):
        self.root = root
        self.model = MaterialsModel()
        self.view = MaterialsView(root, self)
        self.show_materiales()

    def show_materiales(self):
        """Obtiene todos los materiales y los muestra en la vista."""
        data = self.model.get_materiales()
        self.view.display_materiales(data)

    def get_view(self):
        """Devuelve el frame de la vista para ser embebido en la ventana principal."""
        return self.view.get_frame()

    def add_material(self):
        """Abre una ventana para agregar un nuevo material."""
        self.open_material_form("Agregar Material")

    def edit_material(self):
        """Abre una ventana para editar el material seleccionado."""
        selected = self.view.get_selected_material()
        if selected:
            self.open_material_form("Editar Material", selected)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un material para editar.")

    def delete_material(self):
        """Elimina el material seleccionado después de confirmar."""
        selected = self.view.get_selected_material()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este material?")
            if confirm:
                material_id = selected[0]
                self.model.delete_material(material_id)
                self.show_materiales()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un material para eliminar.")

    def filter_materiales(self):
        """Filtra los materiales según el término de búsqueda."""
        search_term = self.view.get_search_entry()
        filtered_data = self.model.search_materiales(search_term)
        self.view.display_materiales(filtered_data)

    def clear_filters(self):
        """Limpia el campo de búsqueda y muestra todos los materiales."""
        self.view.search_entry.delete(0, tk.END)
        self.show_materiales()

    def open_material_form(self, title, material_data=None):
        """Abre un formulario de material para agregar o editar materiales."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x300")
        form.transient(self.root)
        form.grab_set()

        # Campos del formulario
        tk.Label(form, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(form)
        name_entry.pack(pady=5)

        tk.Label(form, text="Cantidad Disponible:").pack(pady=5)
        cantidad_entry = tk.Entry(form)
        cantidad_entry.pack(pady=5)

        tk.Label(form, text="Stock Mínimo:").pack(pady=5)
        stock_entry = tk.Entry(form)
        stock_entry.pack(pady=5)

        if material_data:
            name_entry.insert(0, material_data[1])
            cantidad_entry.insert(0, material_data[2])
            stock_entry.insert(0, material_data[3])

        def submit():
            name = name_entry.get()
            try:
                cantidad_disponible = int(cantidad_entry.get())
                stock_minimo = int(stock_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Los campos de cantidad y stock deben ser números válidos.")
                return

            if not name:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if material_data:
                self.model.update_material(material_data[0], name, cantidad_disponible, stock_minimo)
            else:
                self.model.add_material(name, cantidad_disponible, stock_minimo)

            self.show_materiales()
            form.destroy()

        submit_button = tk.Button(form, text="Guardar", command=submit)
        submit_button.pack(pady=10)
