import tkinter as tk
from tkinter import ttk

class MaterialView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

    def setup_ui(self, controller):
        """Configura la interfaz de usuario."""
        # Frame para barra de búsqueda, filtros y botones CRUD
        search_frame = tk.Frame(self.frame)
        search_frame.pack(side="top", fill="x", pady=10)

        # Barra de búsqueda
        search_label = tk.Label(search_frame, text="Buscar:", font=("Arial", 12))
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
        self.search_entry.pack(side="left", padx=5)

        # Filtro por columnas
        filter_label = tk.Label(search_frame, text="Filtro:", font=("Arial", 12))
        filter_label.pack(side="left", padx=5)

        self.filter_combobox = ttk.Combobox(search_frame, values=["ID", "Nombre", "Cantidad"], font=("Arial", 12), width=15)
        self.filter_combobox.set("Seleccionar filtro")
        self.filter_combobox.pack(side="left", padx=5)

        # Botón de búsqueda
        search_button = tk.Button(search_frame, text="Buscar", command=controller.search, font=("Arial", 10), bg="#59708a", fg="white")
        search_button.pack(side="left", padx=5)

        # Botones CRUD
        crud_frame = tk.Frame(search_frame)
        crud_frame.pack(side="right", padx=10)

        create_button = tk.Button(crud_frame, text="Crear", command=controller.create_item, font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        create_button.pack(side="left", padx=5)

        update_button = tk.Button(crud_frame, text="Actualizar", command=controller.update_item, font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        update_button.pack(side="left", padx=5)

        delete_button = tk.Button(crud_frame, text="Eliminar", command=controller.delete_item, font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        delete_button.pack(side="left", padx=5)

        # Contenedor de materiales
        self.material_frame = tk.Frame(self.frame)
        self.material_frame.pack(fill="both", expand=True)

    def display_materia_prima(self, data):
        """Despliega la lista de materia prima."""
        for widget in self.material_frame.winfo_children():
            widget.destroy()

        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Cantidad"]
        for i, header in enumerate(headers):
            label = tk.Label(self.material_frame, text=header, font=("Arial", 12, "bold"), bg="#d9d9d9", padx=10, pady=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Filas de materia prima
        for row_num, mat in enumerate(data, start=1):
            tk.Label(self.material_frame, text=mat["ID"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=0, sticky="nsew")
            tk.Label(self.material_frame, text=mat["Nombre"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=1, sticky="nsew")
            tk.Label(self.material_frame, text=mat["Cantidad"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=2, sticky="nsew")

        # Redimensionar columnas
        for i in range(len(headers)):
            self.material_frame.grid_columnconfigure(i, weight=1)

    def display_producto_terminado(self, data):
        """Despliega la lista de producto terminado."""
        for widget in self.material_frame.winfo_children():
            widget.destroy()

        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Cantidad"]
        for i, header in enumerate(headers):
            label = tk.Label(self.material_frame, text=header, font=("Arial", 12, "bold"), bg="#d9d9d9", padx=10, pady=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Filas de producto terminado
        for row_num, prod in enumerate(data, start=1):
            tk.Label(self.material_frame, text=prod["ID"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=0, sticky="nsew")
            tk.Label(self.material_frame, text=prod["Nombre"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=1, sticky="nsew")
            tk.Label(self.material_frame, text=prod["Cantidad"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num, column=2, sticky="nsew")

        # Redimensionar columnas
        for i in range(len(headers)):
            self.material_frame.grid_columnconfigure(i, weight=1)

    def get_frame(self):
        return self.frame
