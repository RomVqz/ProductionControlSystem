from tkinter import ttk
from models.ordenesModel import OrdenModel  # Ajuste de importación

def crear_pestana_ordenes(notebook):
    frame = ttk.Frame(notebook, padding=20)
    frame.configure(relief='solid', borderwidth=1)

    frame_principal = ttk.Frame(frame, padding=20)
    frame_principal.pack(expand=True, fill="both", padx=10, pady=10)

    label_buscar = ttk.Label(frame_principal, text="Buscar Orden:")
    label_buscar.pack(pady=(0, 5))
    entry_buscar = ttk.Entry(frame_principal, width=50)
    entry_buscar.pack(pady=(0, 10))

    frame_tabla = ttk.Frame(frame_principal)
    frame_tabla.pack(expand=True, fill="both")

    scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
    scrollbar_x.pack(side="bottom", fill="x")

    tabla = ttk.Treeview(frame_tabla, columns=("id", "producto_id", "cantidad", "fecha_inicio", "fecha_fin", "estado", "cliente_id"), show='headings', xscrollcommand=scrollbar_x.set)

    for column in tabla["columns"]:
        tabla.heading(column, text=column.capitalize())
        tabla.column(column, anchor="center")

    tabla.pack(expand=True, fill="both", padx=10, pady=10)
    scrollbar_x.config(command=tabla.xview)

    ordenes = OrdenModel.get_all_ordenes()
    for orden in ordenes:
        tabla.insert("", "end", values=orden)

    def buscar_orden(event=None):
        query = entry_buscar.get().lower()
        for item in tabla.get_children():
            values = tabla.item(item, 'values')
            if query in (value.lower() for value in values):
                tabla.selection_set(item)
            else:
                tabla.selection_remove(item)

    entry_buscar.bind("<KeyRelease>", buscar_orden)
    return frame
