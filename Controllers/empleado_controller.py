# controllers/empleado_controller.py

from models.empleado_model import EmpleadoModel
from gui.windows.empleado_view import EmpleadoView
import tkinter as tk
from tkinter import messagebox

class EmpleadoController:
    def __init__(self, root):
        self.root = root
        self.model = EmpleadoModel()
        self.view = EmpleadoView(root, self)
        self.show_empleados()

    def show_empleados(self):
        """Obtiene todos los empleados y los muestra en la vista."""
        data = self.model.get_empleados()
        self.view.display_empleados(data)

    def get_view(self):
        """Devuelve el frame de la vista para ser embebido en la ventana principal."""
        return self.view.get_frame()

    def add_empleado(self):
        """Abre una ventana para agregar un nuevo empleado."""
        self.open_empleado_form("Agregar Empleado")

    def edit_empleado(self):
        """Abre una ventana para editar el empleado seleccionado."""
        selected = self.view.get_selected_empleado()
        if selected:
            self.open_empleado_form("Editar Empleado", selected)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para editar.")

    def delete_empleado(self):
        """Elimina el empleado seleccionado después de confirmar."""
        selected = self.view.get_selected_empleado()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este empleado?")
            if confirm:
                empleado_id = selected[0]
                self.model.delete_empleado(empleado_id)
                self.show_empleados()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para eliminar.")

    def filter_empleados(self):
        """Filtra los empleados según el término de búsqueda."""
        search_term = self.view.get_search_entry()
        filtered_data = self.model.search_empleados(search_term)
        self.view.display_empleados(filtered_data)

    def clear_filters(self):
        """Limpia el campo de búsqueda y muestra todos los empleados."""
        self.view.search_entry.delete(0, tk.END)
        self.show_empleados()

    def open_empleado_form(self, title, empleado_data=None):
        """Abre un formulario de empleado para agregar o editar empleados."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x300")
        form.transient(self.root)
        form.grab_set()

        # Campos del formulario
        tk.Label(form, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(form)
        name_entry.pack(pady=5)

        tk.Label(form, text="Puesto:").pack(pady=5)
        puesto_entry = tk.Entry(form)
        puesto_entry.pack(pady=5)

        tk.Label(form, text="Turno:").pack(pady=5)
        turno_entry = tk.Entry(form)
        turno_entry.pack(pady=5)

        tk.Label(form, text="Turno ID:").pack(pady=5)
        turno_id_entry = tk.Entry(form)
        turno_id_entry.pack(pady=5)

        # Si es edición, rellenamos los campos
        if empleado_data:
            name_entry.insert(0, empleado_data[1])
            puesto_entry.insert(0, empleado_data[2])
            turno_entry.insert(0, empleado_data[3])
            turno_id_entry.insert(0, empleado_data[4])

        def submit():
            nombre = name_entry.get()
            puesto = puesto_entry.get()
            turno = turno_entry.get()
            try:
                turno_id = int(turno_id_entry.get())
            except ValueError:
                messagebox.showerror("Error", "El Turno ID debe ser un número válido.")
                return

            if not nombre or not puesto or not turno:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if empleado_data:
                # Actualización de empleado
                self.model.update_empleado(empleado_data[0], nombre, puesto, turno, turno_id)
            else:
                # Agregar nuevo empleado
                self.model.add_empleado(nombre, puesto, turno, turno_id)

            self.show_empleados()
            form.destroy()

        # Botón de envío
        submit_button = tk.Button(form, text="Guardar", command=submit)
        submit_button.pack(pady=10)

        # Botón de cancelar
        cancel_button = tk.Button(form, text="Cancelar", command=form.destroy)
        cancel_button.pack(pady=5)