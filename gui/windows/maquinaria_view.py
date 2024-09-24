import tkinter as tk
from tkinter import ttk


class MaquinariaView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

    def setup_ui(self, controller):
        """Configura la interfaz de usuario."""
        # Frame para la barra de búsqueda, filtros y botones CRUD
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

        self.filter_combobox = ttk.Combobox(search_frame, values=["ID", "Nombre", "Estado"], font=("Arial", 12),
                                            width=15)
        self.filter_combobox.set("Seleccionar filtro")
        self.filter_combobox.pack(side="left", padx=5)

        # Botón de búsqueda
        search_button = tk.Button(search_frame, text="Buscar", command=controller.search_maquinaria, font=("Arial", 10),
                                  bg="#59708a", fg="white")
        search_button.pack(side="left", padx=5)

        # Botones CRUD
        crud_frame = tk.Frame(search_frame)
        crud_frame.pack(side="right", padx=10)

        create_button = tk.Button(crud_frame, text="Crear", command=controller.create_maquinaria, font=("Arial", 10),
                                  bg="#59708a", fg="white", padx=10)
        create_button.pack(side="left", padx=5)

        update_button = tk.Button(crud_frame, text="Actualizar", command=controller.update_maquinaria,
                                  font=("Arial", 10), bg="#59708a", fg="white", padx=10)
        update_button.pack(side="left", padx=5)

        delete_button = tk.Button(crud_frame, text="Eliminar", command=controller.delete_maquinaria, font=("Arial", 10),
                                  bg="#59708a", fg="white", padx=10)
        delete_button.pack(side="left", padx=5)

        # Contenedor de maquinaria
        self.maquinaria_frame = tk.Frame(self.frame)
        self.maquinaria_frame.pack(fill="both", expand=True)

    def display_maquinaria(self, data):
        """Despliega la lista de maquinaria."""
        for widget in self.maquinaria_frame.winfo_children():
            widget.destroy()

        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Estado"]
        for i, header in enumerate(headers):
            label = tk.Label(self.maquinaria_frame, text=header, font=("Arial", 12, "bold"), bg="#d9d9d9", padx=10,
                             pady=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Filas de maquinaria
        for row_num, maq in enumerate(data, start=1):
            tk.Label(self.maquinaria_frame, text=maq["ID"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num,
                                                                                                      column=0,
                                                                                                      sticky="nsew")
            tk.Label(self.maquinaria_frame, text=maq["Nombre"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num,
                                                                                                          column=1,
                                                                                                          sticky="nsew")
            tk.Label(self.maquinaria_frame, text=maq["Estado"], font=("Arial", 10), padx=10, pady=5).grid(row=row_num,
                                                                                                          column=2,
                                                                                                          sticky="nsew")

        # Redimensionar columnas
        for i in range(len(headers)):
            self.maquinaria_frame.grid_columnconfigure(i, weight=1)

    def get_frame(self):
        return self.frame
