# models/producto_model.py

class ProductsModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.products = [
            {"ID": 1, "Nombre": "Producto A", "Descripción": "Descripción A", "Precio": 100.50, "Created_At": "2023-09-20", "Updated_At": "2023-09-21"},
            {"ID": 2, "Nombre": "Producto B", "Descripción": "Descripción B", "Precio": 200.75, "Created_At": "2023-09-18", "Updated_At": "2023-09-19"}
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_products(self):
        return self.products

    def add_product(self, nombre, descripcion, precio):
        new_product = {
            "ID": self.next_id,
            "Nombre": nombre,
            "Descripción": descripcion,
            "Precio": precio,
            "Created_At": "2023-09-24",  # Fecha actual (puedes reemplazar con fecha actual real)
            "Updated_At": "2023-09-24"
        }
        self.products.append(new_product)
        self.next_id += 1

    def update_product(self, product_id, nombre, descripcion, precio):
        for product in self.products:
            if product["ID"] == product_id:
                product["Nombre"] = nombre
                product["Descripción"] = descripcion
                product["Precio"] = precio
                product["Updated_At"] = "2023-09-24"  # Fecha actual (puedes reemplazar con fecha actual real)
                break

    def delete_product(self, product_id):
        self.products = [p for p in self.products if p["ID"] != product_id]

    def search_products(self, search_term):
        return [p for p in self.products if search_term.lower() in p["Nombre"].lower()]
