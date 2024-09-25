from models.maquinaria_model  import MaquinasModel
from gui.windows.maquinaria_view  import MaquinasView
import tkinter as tk
from tkinter import messagebox

class MaquinaController:
    def __init__(self, root):
        self.root = root
        self.model = MaquinasModel()
        self.view = MaquinasView(root, self)
        self.show_maquinas()

    def show_maquinas(self):
        """Obtiene todas las máquinas y las muestra en la vista."""
        data = self.model.get_maquinas()
        self.view.display_maquinas(data)

    def get_view(self):
        """Devuelve el frame de la vista para ser embebido en la ventana principal."""
        return self.view.get_frame()

    def add_maquina(self):
        """Abre una ventana para agregar una nueva máquina."""
        self.open_maquina_form("Agregar Máquina")

    def edit_maquina(self):
        """Abre una ventana para editar la máquina seleccionada."""
        selected = self.view.get_selected_maquina()
        if selected:
            self.open_maquina_form("Editar Máquina", selected)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una máquina para editar.")

    def delete_maquina(self):
        """Elimina la máquina seleccionada después de confirmar."""
        selected = self.view.get_selected_maquina()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta máquina?")
            if confirm:
                maquina_id = selected[0]
                self.model.delete_maquina(maquina_id)
                self.show_maquinas()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una máquina para eliminar.")

    def filter_maquinas(self):
        """Filtra las máquinas según el término de búsqueda."""
        search_term = self.view.get_search_entry()
        filtered_data = self.model.search_maquinas(search_term)
        self.view.display_maquinas(filtered_data)

    def clear_filters(self):
        """Limpia el campo de búsqueda y muestra todas las máquinas."""
        self.view.search_entry.delete(0, tk.END)
        self.show_maquinas()

    def open_maquina_form(self, title, maquina_data=None):
        """Abre un formulario de máquina para agregar o editar máquinas."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x300")
        form.transient(self.root)
        form.grab_set()

        # Campos del formulario
        tk.Label(form, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(form)
        name_entry.pack(pady=5)

        tk.Label(form, text="Estado:").pack(pady=5)
        estado_entry = tk.Entry(form)
        estado_entry.pack(pady=5)

        tk.Label(form, text="Último Mantenimiento (YYYY-MM-DD):").pack(pady=5)
        last_maintenance_entry = tk.Entry(form)
        last_maintenance_entry.pack(pady=5)

        # Si es edición, rellenamos los campos
        if maquina_data:
            name_entry.insert(0, maquina_data[1])
            estado_entry.insert(0, maquina_data[2])
            last_maintenance_entry.insert(0, maquina_data[3])

        def submit():
            nombre = name_entry.get()
            estado = estado_entry.get()
            last_maintenance = last_maintenance_entry.get()

            if not nombre or not estado or not last_maintenance:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if maquina_data:
                # Actualización de máquina
                self.model.update_maquina(maquina_data[0], nombre, estado, last_maintenance)
            else:
                # Agregar nueva máquina
                self.model.add_maquina(nombre, estado, last_maintenance)

            self.show_maquinas()
            form.destroy()

        # Botón de envío
        submit_button = tk.Button(form, text="Guardar", command=submit)
        submit_button.pack(pady=10)

        # Botón de cancelar
        cancel_button = tk.Button(form, text="Cancelar", command=form.destroy)
        cancel_button.pack(pady=5)