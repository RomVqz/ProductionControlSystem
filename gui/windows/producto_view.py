# gui/windows/producto_view.py

import tkinter as tk
from tkinter import ttk


class ProductsView:
    def __init__(self, parent):
        """
        Inicializa la vista de productos, crea un frame donde se mostrará la tabla de productos.
        """
        self.frame = tk.Frame(parent)
        self.create_table()

    def create_table(self):
        """
        Crea una tabla con encabezados donde se mostrarán los datos de los productos.
        """
        columns = ('ID', 'Nombre', 'Categoría')

        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Categoría', text='Categoría')

        # Añadir scroll vertical
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.pack(expand=True, fill="both")

    def display_products(self, data):
        """
        Limpia la tabla y muestra los productos pasados como argumento.
        """
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la tabla
        for item in data:
            self.tree.insert('', tk.END, values=(item['ID'], item['Nombre'], item['Categoría']))

    def get_frame(self):
        """
        Retorna el frame que contiene la vista de productos.
        """
        return self.frame
