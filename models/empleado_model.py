# models/empleado_model.py

class EmpleadoModel:
    def __init__(self):
        # Simulación de datos
        self.empleados = [
            {"id": 1, "nombre": "Juan Pérez", "puesto": "Gerente", "turno": "Mañana", "turno_id": 101},
            {"id": 2, "nombre": "Ana Gómez", "puesto": "Operador", "turno": "Noche", "turno_id": 102}
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_empleados(self):
        return self.empleados

    def add_empleado(self, nombre, puesto, turno, turno_id):
        nuevo_empleado = {
            "id": self.next_id,
            "nombre": nombre,
            "puesto": puesto,
            "turno": turno,
            "turno_id": turno_id
        }
        self.empleados.append(nuevo_empleado)
        self.next_id += 1

    def update_empleado(self, empleado_id, nombre, puesto, turno, turno_id):
        for empleado in self.empleados:
            if empleado["id"] == empleado_id:
                empleado["nombre"] = nombre
                empleado["puesto"] = puesto
                empleado["turno"] = turno
                empleado["turno_id"] = turno_id
                break

    def delete_empleado(self, empleado_id):
        self.empleados = [e for e in self.empleados if e["id"] != empleado_id]

    def search_empleados(self, search_term):
        return [e for e in self.empleados if search_term.lower() in e["nombre"].lower()]