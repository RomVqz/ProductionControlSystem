import tkinter as tk
from tkinter import ttk
from gui.windows.productionOrders import crear_pestana_ordenes
from gui.windows.assignments import crear_tabla_asignaciones
from gui.windows.materials import crear_pestana_materiales
from models.ordenesModel import OrdenModel  # Asegúrate de que esto esté correcto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Producción")
ventana.geometry("800x600")
ventana.configure(bg='#e8f5e9')

# Crear el notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both", padx=20, pady=20)

# Añadir la pestaña de órdenes de producción
notebook.add(crear_pestana_ordenes(notebook), text="Órdenes de Producción")

# Crear la pestaña de asignaciones
notebook.add(crear_tabla_asignaciones(ventana), text="Asignaciones")

# Crear la pestaña de materiales
notebook.add(crear_pestana_materiales(notebook), text="Materiales")

# Iniciar el bucle principal de la ventana
ventana.mainloop()
