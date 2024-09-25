import tkinter as tk
from tkinter import ttk

class MaquinasView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent, bg="#f0f4f7")
        self.controller = controller

        # Barra de búsqueda
        search_frame = tk.Frame(self.frame, bg="#f0f4f7")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Buscar Máquina:", bg="#f0f4f7").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.controller.filter_maquinas)
        search_button.pack(side="left", padx=5)
        clear_button = tk.Button(search_frame, text="Limpiar", command=self.controller.clear_filters)
        clear_button.pack(side="left", padx=5)

        # Tabla de máquinas
        self.tree = ttk.Treeview(self.frame, columns=("id", "nombre", "estado", "last_maintenance"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("last_maintenance", text="Último Mantenimiento")

        self.tree.column("id", width=50)
        self.tree.column("nombre", width=150)
        self.tree.column("estado", width=150)
        self.tree.column("last_maintenance", width=150)

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Botones de acción
        button_frame = tk.Frame(self.frame, bg="#f0f4f7")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar Máquina", font=("Arial", 10, "bold"),
                               bg="#2196F3", fg="white", command=self.controller.add_maquina)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(button_frame, text="Editar Máquina", font=("Arial", 10, "bold"),
                                bg="#FFC107", fg="black", command=self.controller.edit_maquina)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar Máquina", font=("Arial", 10, "bold"),
                                  bg="#f44336", fg="white", command=self.controller.delete_maquina)
        delete_button.pack(side="left", padx=5)

    def display_maquinas(self, data):
        """Muestra las máquinas en la tabla"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for maquina in data:
            self.tree.insert("", "end", values=(maquina["id"], maquina["nombre"], maquina["estado"], maquina["last_maintenance"]))

    def get_search_entry(self):
        """Obtiene el texto ingresado en el campo de búsqueda."""
        return self.search_entry.get()

    def get_selected_maquina(self):
        """Obtiene la máquina seleccionada en la tabla."""
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item)['values']
        return None

    def get_frame(self):
        return self.frame