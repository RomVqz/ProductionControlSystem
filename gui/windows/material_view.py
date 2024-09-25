# gui/windows/materiales_view.py

import tkinter as tk
from tkinter import ttk

class MaterialsView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent, bg="#f0f4f7")
        self.controller = controller

        # Barra de búsqueda
        search_frame = tk.Frame(self.frame, bg="#f0f4f7")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Buscar Material:", bg="#f0f4f7").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.controller.filter_materiales)
        search_button.pack(side="left", padx=5)
        clear_button = tk.Button(search_frame, text="Limpiar", command=self.controller.clear_filters)
        clear_button.pack(side="left", padx=5)

        # Tabla de materiales
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Cantidad_Disponible", "Stock_Minimo"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad_Disponible", text="Cantidad Disponible")
        self.tree.heading("Stock_Minimo", text="Stock Mínimo")

        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Cantidad_Disponible", width=150)
        self.tree.column("Stock_Minimo", width=150)

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Botones de acción
        button_frame = tk.Frame(self.frame, bg="#f0f4f7")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar Material", font=("Arial", 10, "bold"),
                               bg="#2196F3", fg="white", command=self.controller.add_material)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(button_frame, text="Editar Material", font=("Arial", 10, "bold"),
                                bg="#FFC107", fg="black", command=self.controller.edit_material)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar Material", font=("Arial", 10, "bold"),
                                  bg="#f44336", fg="white", command=self.controller.delete_material)
        delete_button.pack(side="left", padx=5)

    def display_materiales(self, data):
        """Muestra los materiales en la tabla"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for material in data:
            self.tree.insert("", "end", values=(material["ID"], material["Nombre"], material["Cantidad_Disponible"], material["Stock_Minimo"]))

    def get_search_entry(self):
        """Obtiene el texto ingresado en el campo de búsqueda."""
        return self.search_entry.get()

    def get_selected_material(self):
        """Obtiene el material seleccionado en la tabla."""
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item)['values']
        return None

    def get_frame(self):
        return self.frame
