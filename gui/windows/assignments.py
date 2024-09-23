import tkinter as tk
from tkinter import ttk

def abrir_ventana_empleados(ventana):
    ventana_empleados = tk.Toplevel(ventana)
    ventana_empleados.title("Empleados")
    ventana_empleados.geometry("600x400")
    ventana_empleados.configure(bg='#e8f5e9')

    frame_principal = ttk.Frame(ventana_empleados, padding=20)
    frame_principal.pack(expand=True, fill="both", padx=10, pady=10)

    label_buscar = ttk.Label(frame_principal, text="Buscar Empleado:")
    label_buscar.pack(pady=(0, 5))
    entry_buscar = ttk.Entry(frame_principal, width=50)
    entry_buscar.pack(pady=(0, 10))

    tabla = ttk.Treeview(frame_principal, columns=("id", "nombre", "puesto", "turno"), show='headings')
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("puesto", text="Puesto")
    tabla.heading("turno", text="Turno")

    tabla.column("id", width=100, anchor="center")
    tabla.column("nombre", width=150, anchor="center")
    tabla.column("puesto", width=150, anchor="center")
    tabla.column("turno", width=150, anchor="center")

    tabla.pack(expand=True, fill="both", padx=10, pady=10)

    def buscar_empleado(event=None):
        query = entry_buscar.get().lower()
        for item in tabla.get_children():
            values = tabla.item(item, 'values')
            if query in (value.lower() for value in values):
                tabla.selection_set(item)
            else:
                tabla.selection_remove(item)

    entry_buscar.bind("<KeyRelease>", buscar_empleado)

def abrir_ventana_maquinaria(ventana):
    ventana_maquinaria = tk.Toplevel(ventana)
    ventana_maquinaria.title("Maquinaria")
    ventana_maquinaria.geometry("600x400")
    ventana_maquinaria.configure(bg='#e8f5e9')

    frame_principal = ttk.Frame(ventana_maquinaria, padding=20)
    frame_principal.pack(expand=True, fill="both", padx=10, pady=10)

    # Crear un frame para la tabla y la barra de desplazamiento
    frame_tabla = ttk.Frame(frame_principal)
    frame_tabla.pack(expand=True, fill="both")

    # Barra de desplazamiento horizontal
    scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
    scrollbar_x.pack(side="bottom", fill="x")

    # Tabla con los nuevos datos de maquinaria
    tabla = ttk.Treeview(frame_tabla, columns=("id", "maquina_id", "fecha_mantenimiento", "tipo_mantenimiento", "descripcion", "tecnico", "costo"), show='headings', xscrollcommand=scrollbar_x.set)
    scrollbar_x.config(command=tabla.xview)

    tabla.heading("id", text="ID")
    tabla.heading("maquina_id", text="Máquina ID")
    tabla.heading("fecha_mantenimiento", text="Fecha Mantenimiento")
    tabla.heading("tipo_mantenimiento", text="Tipo Mantenimiento")
    tabla.heading("descripcion", text="Descripción")
    tabla.heading("tecnico", text="Técnico")
    tabla.heading("costo", text="Costo")

    # Ajustar el ancho de las columnas
    tabla.column("id", width=50, anchor="center")
    tabla.column("maquina_id", width=100, anchor="center")
    tabla.column("fecha_mantenimiento", width=150, anchor="center")
    tabla.column("tipo_mantenimiento", width=150, anchor="center")
    tabla.column("descripcion", width=200, anchor="center")
    tabla.column("tecnico", width=100, anchor="center")
    tabla.column("costo", width=100, anchor="center")

    tabla.pack(expand=True, fill="both", padx=10, pady=10)

    # Configurar la barra de desplazamiento para que funcione con la tabla
    tabla.configure(xscrollcommand=scrollbar_x.set)

    # Ejemplo de cómo agregar datos a la tabla
    datos_ejemplo_maquinaria = [
        (1, "M001", "2024-09-20", "Preventivo", "Cambio de aceite", "Juan Pérez", 150.00),
        (2, "M002", "2024-09-21", "Correctivo", "Reemplazo de manguera", "Ana García", 250.00),
        (3, "M003", "2024-09-22", "Preventivo", "Revisión general", "Luis Torres", 100.00),
    ]

    for dato in datos_ejemplo_maquinaria:
        tabla.insert("", "end", values=dato)

def crear_tabla_asignaciones(ventana):
    frame = ttk.Frame(ventana, padding=20)

    # Botones para abrir ventanas
    marco_botones = ttk.Frame(frame)
    marco_botones.pack(pady=(0, 10))

    boton_empleados = ttk.Button(marco_botones, text="Empleados", command=lambda: abrir_ventana_empleados(ventana))
    boton_empleados.grid(row=0, column=0, padx=10, pady=5)

    boton_maquinaria = ttk.Button(marco_botones, text="Maquinaria", command=lambda: abrir_ventana_maquinaria(ventana))
    boton_maquinaria.grid(row=0, column=1, padx=10, pady=5)

    # Tabla en la pestaña de asignaciones
    tabla = ttk.Treeview(frame, columns=("id", "empleado", "maquinaria", "estado"), show='headings')
    tabla.heading("id", text="ID")
    tabla.heading("empleado", text="Empleado")
    tabla.heading("maquinaria", text="Maquinaria")
    tabla.heading("estado", text="Estado")

    tabla.column("id", width=100, anchor="center")
    tabla.column("empleado", width=200, anchor="center")
    tabla.column("maquinaria", width=200, anchor="center")
    tabla.column("estado", width=100, anchor="center")

    tabla.pack(expand=True, fill="both", padx=10, pady=10)

    return frame