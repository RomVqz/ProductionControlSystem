class ProductsModel:
    def __init__(self):
        # Simulación de datos de empleados
        self.products = [{"ID": 1, "Nombre": "Juan", "Puesto": "Operador"},
                          {"ID": 2, "Nombre": "Ana", "Puesto": "Supervisor"}]

    def get_products(self):
        return self.products
