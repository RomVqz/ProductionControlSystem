from tkinter import ttk

def crear_pestana_materiales(notebook):
    frame_materiales = ttk.Frame(notebook, padding=20)
    frame_materiales.configure(relief='solid', borderwidth=1)

    marco_botones_materiales = ttk.Frame(frame_materiales)
    marco_botones_materiales.pack(side="top", fill="x", pady=10)

    marco_centrado = ttk.Frame(marco_botones_materiales)
    marco_centrado.pack(side="top")

    # Función para mostrar la tabla de productos
    def mostrar_tabla_productos():
        for widget in marco_tabla_productos.winfo_children():
            widget.destroy()

        tabla_productos = ttk.Treeview(marco_tabla_productos, columns=("id", "nombre", "descripcion", "precio"), show='headings')
        tabla_productos.heading("id", text="ID")
        tabla_productos.heading("nombre", text="Nombre")
        tabla_productos.heading("descripcion", text="Descripción")
        tabla_productos.heading("precio", text="Precio")

        tabla_productos.column("id", width=100, anchor="center")
        tabla_productos.column("nombre", width=150, anchor="center")
        tabla_productos.column("descripcion", width=250, anchor="center")
        tabla_productos.column("precio", width=100, anchor="center")

        productos = [
            (1, "Producto A", "Descripción del Producto A", "$100"),
            (2, "Producto B", "Descripción del Producto B", "$200"),
            (3, "Producto C", "Descripción del Producto C", "$150"),
        ]

        for producto in productos:
            tabla_productos.insert("", "end", values=producto)

        tabla_productos.pack(expand=True, fill="both", padx=10, pady=10)

    marco_tabla_productos = ttk.Frame(frame_materiales)
    marco_tabla_productos.pack(side="top", fill="both", expand=True)

    # Botón para mostrar la tabla de productos
    boton_productos = ttk.Button(marco_centrado, text="Productos", command=mostrar_tabla_productos)
    boton_productos.pack(side="left", padx=10)

    def mostrar_tabla_materia_prima():
        for widget in marco_tabla_productos.winfo_children():
            widget.destroy()

        tabla_materia_prima = ttk.Treeview(marco_tabla_productos, columns=("id", "nombre", "cantidad_disponible"), show='headings')
        tabla_materia_prima.heading("id", text="ID")
        tabla_materia_prima.heading("nombre", text="Nombre")
        tabla_materia_prima.heading("cantidad_disponible", text="Cantidad Disponible")

        tabla_materia_prima.column("id", width=100, anchor="center")
        tabla_materia_prima.column("nombre", width=150, anchor="center")
        tabla_materia_prima.column("cantidad_disponible", width=150, anchor="center")

        materia_prima = [
            (1, "Materia Prima A", 100),
            (2, "Materia Prima B", 200),
            (3, "Materia Prima C", 150),
        ]

        for item in materia_prima:
            tabla_materia_prima.insert("", "end", values=item)

        tabla_materia_prima.pack(expand=True, fill="both", padx=10, pady=10)

    boton_materia_prima = ttk.Button(marco_centrado, text="Materia Prima", command=mostrar_tabla_materia_prima)
    boton_materia_prima.pack(side="left", padx=10)

    # Mostrar la tabla de productos por defecto al iniciar
    mostrar_tabla_productos()

    return frame_materiales
