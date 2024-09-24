import tkinter as tk
from tkinter import ttk

class Production_orderView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

    def display_production_order(self, data):
        # Limpiar el frame antes de mostrar nuevos datos
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Cantidad", "Fecha Inicio", "Fecha Fin", "Estado"]
        for i, header in enumerate(headers):
            label = tk.Label(self.frame, text=header, font=("Arial", 12, "bold"), bg="#d9d9d9", padx=10, pady=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Mostrar los datos
        for row_num, order in enumerate(data, start=1):
            tk.Label(self.frame, text=order["ID"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=0, sticky="nsew")
            tk.Label(self.frame, text=order["Nombre"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=1, sticky="nsew")
            tk.Label(self.frame, text=order["Cantidad"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=2, sticky="nsew")
            tk.Label(self.frame, text=order["Fecha Inicio"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=3, sticky="nsew")
            tk.Label(self.frame, text=order["Fecha Fin"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=4, sticky="nsew")
            tk.Label(self.frame, text=order["Estado"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(row=row_num, column=5, sticky="nsew")

        # Hacer que las columnas se adapten al tamaño del contenedor
        for i in range(len(headers)):
            self.frame.grid_columnconfigure(i, weight=1)

    def get_frame(self):
        return self.frame

    # Crear la barra de búsqueda y botones CRUD (Create, Read, Update, Delete)
    def create_search_bar(self, parent, search_callback):
        search_frame = tk.Frame(parent, bg="white")
        search_frame.pack(side="top", fill="x", pady=10)

        # Barra de búsqueda
        search_label = tk.Label(search_frame, text="Buscar:", font=("Arial", 12), bg="white")
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
        self.search_entry.pack(side="left", padx=5)

        # Filtro por columnas
        filter_label = tk.Label(search_frame, text="Filtro:", font=("Arial", 12), bg="white")
        filter_label.pack(side="left", padx=5)

        self.filter_combobox = ttk.Combobox(search_frame, values=["ID", "Nombre", "Cantidad", "Fecha Inicio", "Fecha Fin", "Estado"], font=("Arial", 12), width=15)
        self.filter_combobox.set("Seleccionar filtro")
        self.filter_combobox.pack(side="left", padx=5)

        # Botón de búsqueda
        search_button = tk.Button(search_frame, text="Buscar", command=search_callback, font=("Arial", 10), bg="#59708a", fg="white")
        search_button.pack(side="left", padx=5)

        # Botones CRUD
        crud_frame = tk.Frame(search_frame, bg="white")
        crud_frame.pack(side="right", padx=10)

        create_button = tk.Button(crud_frame, text="Crear", font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        create_button.pack(side="left", padx=5)

        update_button = tk.Button(crud_frame, text="Actualizar", font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        update_button.pack(side="left", padx=5)

        delete_button = tk.Button(crud_frame, text="Eliminar", font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        delete_button.pack(side="left", padx=5)

    def get_search_query(self):
        return self.search_entry.get(), self.filter_combobox.get()
