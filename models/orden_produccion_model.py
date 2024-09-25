class OrdenesProduccionModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.ordenes = [
            {
                "id": 1, "producto_id": 101, "cantidad": 50, 
                "fecha_inicio": "2023-09-20", "fecha_fin": "2023-09-25", 
                "estado": "En Progreso", "cliente_id": 1001
            },
            {
                "id": 2, "producto_id": 102, "cantidad": 20, 
                "fecha_inicio": "2023-09-22", "fecha_fin": "2023-09-26", 
                "estado": "Completado", "cliente_id": 1002
            }
        ]
        self.next_id = 3

    def get_ordenes(self):
        return self.ordenes

    def add_orden(self, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        new_orden = {
            "id": self.next_id,
            "producto_id": producto_id,
            "cantidad": cantidad,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "estado": estado,
            "cliente_id": cliente_id
        }
        self.ordenes.append(new_orden)
        self.next_id += 1

    def update_orden(self, orden_id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        for orden in self.ordenes:
            if orden["id"] == orden_id:
                orden["producto_id"] = producto_id
                orden["cantidad"] = cantidad
                orden["fecha_inicio"] = fecha_inicio
                orden["fecha_fin"] = fecha_fin
                orden["estado"] = estado
                orden["cliente_id"] = cliente_id
                break

    def delete_orden(self, orden_id):
        self.ordenes = [o for o in self.ordenes if o["id"] != orden_id]

    def search_ordenes(self, search_term):
        return [o for o in self.ordenes if search_term.lower() in o["estado"].lower()]