# models/producto_model.py

class ProductsModel:
    def __init__(self):
        # Simulación de datos de productos
        self.products = [
            {"ID": 1, "Nombre": "Producto A", "Categoría": "Electrónica"},
            {"ID": 2, "Nombre": "Producto B", "Categoría": "Automotriz"}
        ]

    def get_products(self):
        """
        Retorna todos los productos disponibles en la simulación.
        """
        return self.products
