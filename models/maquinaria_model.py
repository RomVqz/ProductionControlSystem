class MaquinasModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.maquinas = [
            {"id": 1, "nombre": "Máquina A", "estado": "Operativa", "last_maintenance": "2023-08-20"},
            {"id": 2, "nombre": "Máquina B", "estado": "En reparación", "last_maintenance": "2023-09-15"}
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_maquinas(self):
        return self.maquinas

    def add_maquina(self, nombre, estado, last_maintenance):
        new_maquina = {
            "id": self.next_id,
            "nombre": nombre,
            "estado": estado,
            "last_maintenance": last_maintenance  # Fecha actual o proporcionada
        }
        self.maquinas.append(new_maquina)
        self.next_id += 1

    def update_maquina(self, maquina_id, nombre, estado, last_maintenance):
        for maquina in self.maquinas:
            if maquina["id"] == maquina_id:
                maquina["nombre"] = nombre
                maquina["estado"] = estado
                maquina["last_maintenance"] = last_maintenance
                break

    def delete_maquina(self, maquina_id):
        self.maquinas = [m for m in self.maquinas if m["id"] != maquina_id]

    def search_maquinas(self, search_term):
        return [m for m in self.maquinas if search_term.lower() in m["nombre"].lower()]