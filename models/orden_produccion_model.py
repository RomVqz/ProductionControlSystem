# models/ordenes_produccion_model.py
class OrdenesProduccionModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.ordenes = [
            {
                "ID": 1, "Producto_ID": 1, "Cantidad": 100, "Fecha_Inicio": "2023-09-20",
                "Fecha_Fin": "2023-09-25", "Estado": "En Proceso", "Cliente_ID": 1
            },
            {
                "ID": 2, "Producto_ID": 2, "Cantidad": 50, "Fecha_Inicio": "2023-09-18",
                "Fecha_Fin": "2023-09-20", "Estado": "Completado", "Cliente_ID": 2
            }
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_ordenes(self):
        return self.ordenes

    def add_orden(self, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        nueva_orden = {
            "ID": self.next_id,
            "Producto_ID": producto_id,
            "Cantidad": cantidad,
            "Fecha_Inicio": fecha_inicio,
            "Fecha_Fin": fecha_fin,
            "Estado": estado,
            "Cliente_ID": cliente_id
        }
        self.ordenes.append(nueva_orden)
        self.next_id += 1

    def update_orden(self, orden_id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        for orden in self.ordenes:
            if orden["ID"] == orden_id:
                orden["Producto_ID"] = producto_id
                orden["Cantidad"] = cantidad
                orden["Fecha_Inicio"] = fecha_inicio
                orden["Fecha_Fin"] = fecha_fin
                orden["Estado"] = estado
                orden["Cliente_ID"] = cliente_id
                break

    def delete_orden(self, orden_id):
        self.ordenes = [o for o in self.ordenes if o["ID"] != orden_id]

    def search_ordenes(self, search_term):
        return [o for o in self.ordenes if search_term.lower() in o["Estado"].lower()]
