class Production_orderModel:
    def __init__(self):
        # Simulación de datos de órdenes de producción
        self.production_order = [
            {"ID": 1, "Nombre": "Producto A", "Cantidad": 100, "Fecha Inicio": "2024-09-01", "Fecha Fin": "2024-09-10", "Estado": "Completado"},
            {"ID": 2, "Nombre": "Producto B", "Cantidad": 50, "Fecha Inicio": "2024-09-05", "Fecha Fin": "2024-09-15", "Estado": "En Proceso"},
            {"ID": 3, "Nombre": "Producto C", "Cantidad": 75, "Fecha Inicio": "2024-09-08", "Fecha Fin": "2024-09-18", "Estado": "Pendiente"},
            {"ID": 4, "Nombre": "Producto D", "Cantidad": 200, "Fecha Inicio": "2024-09-03", "Fecha Fin": "2024-09-20", "Estado": "Completado"},
        ]

    def get_production_orders(self):
        return self.production_order
