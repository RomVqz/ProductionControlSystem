# controllers/producto_controller.py

from models.producto_model import ProductsModel
from gui.windows.producto_view import ProductsView
import tkinter as tk
from tkinter import messagebox

class ProductoController:
    def __init__(self, root):
        self.root = root
        self.model = ProductsModel()
        self.view = ProductsView(root, self)
        self.show_products()

    def show_products(self):
        """Obtiene todos los productos y los muestra en la vista."""
        data = self.model.get_products()
        self.view.display_products(data)

    def get_view(self):
        """Devuelve el frame de la vista para ser embebido en la ventana principal."""
        return self.view.get_frame()

    def add_product(self):
        """Abre una ventana para agregar un nuevo producto."""
        self.open_product_form("Agregar Producto")

    def edit_product(self):
        """Abre una ventana para editar el producto seleccionado."""
        selected = self.view.get_selected_product()
        if selected:
            self.open_product_form("Editar Producto", selected)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un producto para editar.")

    def delete_product(self):
        """Elimina el producto seleccionado después de confirmar."""
        selected = self.view.get_selected_product()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este producto?")
            if confirm:
                product_id = selected[0]
                self.model.delete_product(product_id)
                self.show_products()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un producto para eliminar.")

    def filter_products(self):
        """Filtra los productos según el término de búsqueda."""
        search_term = self.view.get_search_entry()
        filtered_data = self.model.search_products(search_term)
        self.view.display_products(filtered_data)

    def clear_filters(self):
        """Limpia el campo de búsqueda y muestra todos los productos."""
        self.view.search_entry.delete(0, tk.END)
        self.show_products()

    def open_product_form(self, title, product_data=None):
        """Abre un formulario de producto para agregar o editar productos."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x300")
        form.transient(self.root)  # Mantiene el formulario sobre la ventana principal
        form.grab_set()  # Bloquea la interacción con la ventana principal hasta cerrar el formulario

        # Campos del formulario
        tk.Label(form, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(form)
        name_entry.pack(pady=5)

        tk.Label(form, text="Descripción:").pack(pady=5)
        description_entry = tk.Entry(form)
        description_entry.pack(pady=5)

        tk.Label(form, text="Precio:").pack(pady=5)
        price_entry = tk.Entry(form)
        price_entry.pack(pady=5)

        # Si es edición, rellenamos los campos
        if product_data:
            name_entry.insert(0, product_data[1])
            description_entry.insert(0, product_data[2])
            price_entry.insert(0, product_data[3])

        def submit():
            name = name_entry.get()
            description = description_entry.get()
            try:
                price = float(price_entry.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
                return

            if not name or not description:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if product_data:
                # Actualización de producto
                self.model.update_product(product_data[0], name, description, price)
            else:
                # Agregar nuevo producto
                self.model.add_product(name, description, price)

            self.show_products()  # Actualizar la vista con los datos
            form.destroy()  # Cerrar el formulario

        # Botón de envío
        submit_button = tk.Button(form, text="Guardar", command=submit)
        submit_button.pack(pady=10)

        # Botón de cancelar
        cancel_button = tk.Button(form, text="Cancelar", command=form.destroy)
        cancel_button.pack(pady=5)
