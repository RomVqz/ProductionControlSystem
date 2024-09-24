import tkinter as tk
from tkinter import ttk


class EmpleadoView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")

    def setup_ui(self, controller):
        """Configura la interfaz de usuario."""
        # Frame para la barra de búsqueda, filtros y botones CRUD
        search_frame = tk.Frame(self.frame, bg="white")
        search_frame.pack(side="top", fill="x", pady=10)

        # Barra de búsqueda
        search_label = tk.Label(search_frame, text="Buscar:", font=("Arial", 12), bg="white")
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
        self.search_entry.pack(side="left", padx=5)

        # Filtro por columnas
        filter_label = tk.Label(search_frame, text="Filtro:", font=("Arial", 12), bg="white")
        filter_label.pack(side="left", padx=5)

        self.filter_combobox = ttk.Combobox(search_frame, values=["ID", "Nombre", "Puesto"], font=("Arial", 12),
                                            width=15)
        self.filter_combobox.set("Seleccionar filtro")
        self.filter_combobox.pack(side="left", padx=5)

        # Botón de búsqueda
        search_button = tk.Button(search_frame, text="Buscar", command=controller.search_empleados, font=("Arial", 10),
                                  bg="#59708a", fg="white")
        search_button.pack(side="left", padx=5)

        # Botones CRUD
        crud_frame = tk.Frame(search_frame, bg="white")
        crud_frame.pack(side="right", padx=10)

        create_button = tk.Button(crud_frame, text="Crear", command=controller.create_empleado, font=("Arial", 10),
                                  bg="#59708a", fg="white", padx=10)
        create_button.pack(side="left", padx=5)

        update_button = tk.Button(crud_frame, text="Actualizar", command=controller.update_empleado, font=("Arial", 10),
                                  bg="#59708a", fg="white", padx=10)
        update_button.pack(side="left", padx=5)

        delete_button = tk.Button(crud_frame, text="Eliminar", command=controller.delete_empleado, font=("Arial", 10),
                                  bg="#59708a", fg="white", padx=10)
        delete_button.pack(side="left", padx=5)

        # Tabla de empleados
        self.container = tk.Frame(self.frame, bg="white")
        self.container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.container)
        self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def display_empleados(self, data):
        """Despliega la lista de empleados en la tabla."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Puesto"]
        for i, header in enumerate(headers):
            label = tk.Label(self.scrollable_frame, text=header, font=("Arial", 12, "bold"), bg="#d9d9d9", padx=10,
                             pady=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Filas de empleados
        for row_num, empleado in enumerate(data, start=1):
            tk.Label(self.scrollable_frame, text=empleado["ID"], font=("Arial", 10), bg="white", padx=10, pady=5).grid(
                row=row_num, column=0, sticky="nsew")
            tk.Label(self.scrollable_frame, text=empleado["Nombre"], font=("Arial", 10), bg="white", padx=10,
                     pady=5).grid(row=row_num, column=1, sticky="nsew")
            tk.Label(self.scrollable_frame, text=empleado["Puesto"], font=("Arial", 10), bg="white", padx=10,
                     pady=5).grid(row=row_num, column=2, sticky="nsew")

        # Redimensionar columnas
        for i in range(len(headers)):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)

    def get_frame(self):
        return self.frame
