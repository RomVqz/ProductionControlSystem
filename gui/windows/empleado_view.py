# gui/windows/empleado_view.py

import tkinter as tk
from tkinter import ttk

class EmpleadoView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent, bg="#f0f4f7")
        self.controller = controller

        # Barra de búsqueda
        search_frame = tk.Frame(self.frame, bg="#f0f4f7")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Buscar Empleado:", bg="#f0f4f7").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.controller.filter_empleados)
        search_button.pack(side="left", padx=5)
        clear_button = tk.Button(search_frame, text="Limpiar", command=self.controller.clear_filters)
        clear_button.pack(side="left", padx=5)

        # Tabla de empleados
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Puesto", "Turno", "Turno_ID"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Puesto", text="Puesto")
        self.tree.heading("Turno", text="Turno")
        self.tree.heading("Turno_ID", text="Turno ID")

        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Puesto", width=150)
        self.tree.column("Turno", width=100)
        self.tree.column("Turno_ID", width=80)

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Botones de acción
        button_frame = tk.Frame(self.frame, bg="#f0f4f7")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar Empleado", font=("Arial", 10, "bold"),
                               bg="#2196F3", fg="white", command=self.controller.add_empleado)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(button_frame, text="Editar Empleado", font=("Arial", 10, "bold"),
                                bg="#FFC107", fg="black", command=self.controller.edit_empleado)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar Empleado", font=("Arial", 10, "bold"),
                                  bg="#f44336", fg="white", command=self.controller.delete_empleado)
        delete_button.pack(side="left", padx=5)

    def display_empleados(self, data):
        """Muestra los empleados en la tabla"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for empleado in data:
            self.tree.insert("", "end", values=(empleado["id"], empleado["nombre"], empleado["puesto"], empleado["turno"], empleado["turno_id"]))

    def get_search_entry(self):
        """Obtiene el texto ingresado en el campo de búsqueda."""
        return self.search_entry.get()

    def get_selected_empleado(self):
        """Obtiene el empleado seleccionado en la tabla."""
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item)['values']
        return None

    def get_frame(self):
        return self.frame