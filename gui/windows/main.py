import tkinter as tk
from tkinter import Menu
from Controllers.material_controller import MaterialController
from Controllers.empleado_controller import EmpleadoController
from Controllers.maquinaria_controller import MaquinariaController
from Controllers.orden_produccion_controller import Production_orderController
from Controllers.producto_controller import ProductoController

def show_material_menu():
    clear_container()
    material_controller = MaterialController(content_frame)
    material_controller.show_items()
    material_controller.get_view().pack(expand=True, fill="both")

def show_product_menu():
    clear_container()  # Limpiar el frame antes de agregar contenido nuevo
    producto_controller = ProductoController(content_frame)
    producto_controller.show_products()
    producto_controller.get_view().pack(expand=True, fill="both")


# Función para mostrar empleados
def show_employee_menu():
    clear_container()
    empleado_controller = EmpleadoController(content_frame)
    empleado_controller.show_empleados()
    empleado_controller.get_view().pack(expand=True, fill="both")

# Función para mostrar maquinaria
def show_machinery_menu():
    clear_container()
    maquinaria_controller = MaquinariaController(content_frame)
    maquinaria_controller.show_maquinaria()
    maquinaria_controller.get_view().pack(expand=True, fill="both")

# Función para desplegar el menú "Materia" con subopciones "Materiales" y "Productos"
def show_materia_menu():
    materia_menu = Menu(materia_button, tearoff=0)
    materia_menu.add_command(label="Materiales", command=show_material_menu)
    materia_menu.add_command(label="Productos", command=show_product_menu)
    materia_menu.post(materia_button.winfo_rootx(), materia_button.winfo_rooty() + materia_button.winfo_height())

# Función para desplegar el menú "Asignación" con subopciones "Empleados" y "Maquinaria"
def show_assignment_menu():
    assignment_menu = Menu(assignment_button, tearoff=0)
    assignment_menu.add_command(label="Empleados", command=show_employee_menu)
    assignment_menu.add_command(label="Maquinaria", command=show_machinery_menu)
    assignment_menu.post(assignment_button.winfo_rootx(), assignment_button.winfo_rooty() + assignment_button.winfo_height())

# Función para mostrar el dashboard
def show_dashboard():
    clear_container()
    label = tk.Label(content_frame, text="Dashboard", font=("Arial", 24), fg="#333")
    label.pack(expand=True)

# Función para mostrar la orden de producción
def show_production_order():
    clear_container()
    orden_produccion_controller = Production_orderController(content_frame)
    orden_produccion_controller.show_production_order()
    orden_produccion_controller.get_view().pack(expand=True, fill="both")

# Función para limpiar el contenido del container central
def clear_container():
    for widget in content_frame.winfo_children():
        widget.destroy()

# Configuración principal de la ventana
root = tk.Tk()
root.title("Production Control System")
root.geometry("1280x720")
root.configure(bg="#a5b1be")  # Fondo de la ventana principal

# Frame superior para los botones
button_frame = tk.Frame(root, bg="#59708a", height=50)
button_frame.pack(side="top", fill="x")

# Creación de botones con estilo
button_style = {"font": ("Arial bold", 11), "bg": "#bfc8d2", "fg": "black", "width": 20, "height": 1}

# Botón "Orden de Producción"
production_button = tk.Button(button_frame, text="Orden de Producción", command=show_production_order, **button_style)
production_button.grid(row=0, column=0, padx=10, pady=5)

# Botón "Materia" que despliega las opciones "Materiales" y "Productos"
materia_button = tk.Button(button_frame, text="Materia", command=show_materia_menu, **button_style)
materia_button.grid(row=0, column=1, padx=10, pady=5)

# Botón "Asignación" que despliega las opciones "Empleados" y "Maquinaria"
assignment_button = tk.Button(button_frame, text="Asignación", command=show_assignment_menu, **button_style)
assignment_button.grid(row=0, column=2, padx=10, pady=5)

# Botón "Dashboard"
dashboard_button = tk.Button(button_frame, text="Dashboard", command=show_dashboard, **button_style)
dashboard_button.grid(row=0, column=3, padx=10, pady=5)

# Frame central para mostrar el contenido dinámico
content_frame = tk.Frame(root, bg="white", relief="sunken", bd=2)
content_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Ejecutar la ventana principal
root.mainloop()
