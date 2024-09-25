# gui/windows/ordenes_produccion_view.py
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class OrdenesProduccionView:
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent, bg="#f0f4f7")
        self.controller = controller  # Referencia al controlador

        # Barra de búsqueda
        search_frame = tk.Frame(self.frame, bg="#f0f4f7")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Buscar Orden:", bg="#f0f4f7").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Buscar", command=self.controller.filter_ordenes)
        search_button.pack(side="left", padx=5)
        clear_button = tk.Button(search_frame, text="Limpiar", command=self.controller.clear_filters)
        clear_button.pack(side="left", padx=5)

        # Tabla de órdenes
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Producto_ID", "Cantidad", "Fecha_Inicio", "Fecha_Fin", "Estado", "Cliente_ID"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto_ID", text="Producto_ID")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Fecha_Inicio", text="Fecha Inicio")
        self.tree.heading("Fecha_Fin", text="Fecha Fin")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Cliente_ID", text="Cliente_ID")

        self.tree.column("ID", width=50)
        self.tree.column("Producto_ID", width=100)
        self.tree.column("Cantidad", width=100)
        self.tree.column("Fecha_Inicio", width=150)
        self.tree.column("Fecha_Fin", width=150)
        self.tree.column("Estado", width=100)
        self.tree.column("Cliente_ID", width=100)

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Botones de acción
        button_frame = tk.Frame(self.frame, bg="#f0f4f7")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar Orden", font=("Arial", 10, "bold"), bg="#2196F3", fg="white", command=self.controller.add_orden)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(button_frame, text="Editar Orden", font=("Arial", 10, "bold"), bg="#FFC107", fg="black", command=self.controller.edit_orden)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar Orden", font=("Arial", 10, "bold"), bg="#f44336", fg="white", command=self.controller.delete_orden)
        delete_button.pack(side="left", padx=5)

    def display_ordenes(self, data):
        """Muestra las órdenes en la tabla."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for orden in data:
            self.tree.insert("", "end", values=(orden["ID"], orden["Producto_ID"], orden["Cantidad"], orden["Fecha_Inicio"], orden["Fecha_Fin"], orden["Estado"], orden["Cliente_ID"]))

    def get_search_entry(self):
        """Obtiene el texto ingresado en el campo de búsqueda."""
        return self.search_entry.get()

    def get_selected_orden(self):
        """Obtiene la orden seleccionada en la tabla."""
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item)['values']
        return None

    def get_frame(self):
        return self.frame
