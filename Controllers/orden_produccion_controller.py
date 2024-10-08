from models.orden_produccion_model import OrdenesProduccionModel
from gui.windows.orden_produccion_view import OrdenesProduccionView
import tkinter as tk
from tkinter import messagebox

class OrdenesProduccionController:
    def __init__(self, root):
        self.root = root
        self.model = OrdenesProduccionModel()
        self.view = OrdenesProduccionView(root, self)
        self.show_ordenes()

    def show_ordenes(self):
        """Obtiene todas las órdenes y las muestra en la vista."""
        data = self.model.get_ordenes()
        self.view.display_ordenes(data)

    def get_view(self):
        """Devuelve el frame de la vista para ser embebido en la ventana principal."""
        return self.view.get_frame()

    def add_orden(self):
        """Abre una ventana para agregar una nueva orden."""
        self.open_orden_form("Agregar Orden")

    def edit_orden(self):
        """Abre una ventana para editar la orden seleccionada."""
        selected = self.view.get_selected_orden()
        if selected:
            self.open_orden_form("Editar Orden", selected)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una orden para editar.")

    def delete_orden(self):
        """Elimina la orden seleccionada después de confirmar."""
        selected = self.view.get_selected_orden()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta orden?")
            if confirm:
                orden_id = selected[0]
                self.model.delete_orden(orden_id)
                self.show_ordenes()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una orden para eliminar.")

    def filter_ordenes(self):
        """Filtra las órdenes según el término de búsqueda."""
        search_term = self.view.get_search_entry()
        filtered_data = self.model.search_ordenes(search_term)
        self.view.display_ordenes(filtered_data)

    def clear_filters(self):
        """Limpia el campo de búsqueda y muestra todas las órdenes."""
        self.view.search_entry.delete(0, tk.END)
        self.show_ordenes()

    def open_orden_form(self, title, orden_data=None):
        """Abre un formulario de orden para agregar o editar órdenes."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x400")
        form.transient(self.root)
        form.grab_set()

        # Campos del formulario
        tk.Label(form, text="Producto ID:").pack(pady=5)
        producto_entry = tk.Entry(form)
        producto_entry.pack(pady=5)

        tk.Label(form, text="Cantidad:").pack(pady=5)
        cantidad_entry = tk.Entry(form)
        cantidad_entry.pack(pady=5)

        tk.Label(form, text="Fecha Inicio:").pack(pady=5)
        fecha_inicio_entry = tk.Entry(form)
        fecha_inicio_entry.pack(pady=5)

        tk.Label(form, text="Fecha Fin:").pack(pady=5)
        fecha_fin_entry = tk.Entry(form)
        fecha_fin_entry.pack(pady=5)

        tk.Label(form, text="Estado:").pack(pady=5)
        estado_entry = tk.Entry(form)
        estado_entry.pack(pady=5)

        tk.Label(form, text="Cliente ID:").pack(pady=5)
        cliente_entry = tk.Entry(form)
        cliente_entry.pack(pady=5)

        # Si es edición, rellenamos los campos
        if orden_data:
            producto_entry.insert(0, orden_data[1])
            cantidad_entry.insert(0, orden_data[2])
            fecha_inicio_entry.insert(0, orden_data[3])
            fecha_fin_entry.insert(0, orden_data[4])
            estado_entry.insert(0, orden_data[5])
            cliente_entry.insert(0, orden_data[6])

        def submit():
            producto_id = int(producto_entry.get())
            cantidad = int(cantidad_entry.get())
            fecha_inicio = fecha_inicio_entry.get()
            fecha_fin = fecha_fin_entry.get()
            estado = estado_entry.get()
            cliente_id = int(cliente_entry.get())

            if orden_data:
                # Actualización de orden
                self.model.update_orden(orden_data[0], producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id)
            else:
                # Agregar nueva orden
                self.model.add_orden(producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id)

            self.show_ordenes()
            form.destroy()

        # Botón de envío
        submit_button = tk.Button(form, text="Guardar", command=submit)
        submit_button.pack(pady=10)

        # Botón de cancelar
        cancel_button = tk.Button(form, text="Cancelar", command=form.destroy)
        cancel_button.pack(pady=5)