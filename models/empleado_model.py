class EmpleadoModel:
    def __init__(self):
        # Simulación de datos de empleados
        self.empleados = [
            {"ID": 1, "Nombre": "Juan", "Puesto": "Operador"},
            {"ID": 2, "Nombre": "Ana", "Puesto": "Supervisor"},
            {"ID": 3, "Nombre": "Luis", "Puesto": "Gerente"},
            {"ID": 4, "Nombre": "Marta", "Puesto": "Asistente"},
        ]

    def get_empleados(self):
        return self.empleados

    def search_empleados(self, query, column):
        """Realiza una búsqueda de empleados en función de la columna seleccionada."""
        return [empleado for empleado in self.empleados if query.lower() in str(empleado[column]).lower()]

    def add_empleado(self, id, nombre, puesto):
        """Agrega un nuevo empleado a la lista."""
        self.empleados.append({"ID": id, "Nombre": nombre, "Puesto": puesto})

    def update_empleado(self, id, nombre, puesto):
        """Actualiza un empleado existente."""
        for empleado in self.empleados:
            if empleado["ID"] == id:
                empleado["Nombre"] = nombre
                empleado["Puesto"] = puesto
                break

    def delete_empleado(self, id):
        """Elimina un empleado por su ID."""
        self.empleados = [empleado for empleado in self.empleados if empleado["ID"] != id]
