class MaterialModel:
    def __init__(self):
        # Simulación de datos de materia prima
        self.materia_prima = [
            {"ID": 1, "Nombre": "Acero", "Cantidad": 500},
            {"ID": 2, "Nombre": "Plástico", "Cantidad": 300}
        ]
        # Simulación de datos de producto terminado
        self.producto_terminado = [
            {"ID": 1, "Nombre": "Silla", "Cantidad": 100},
            {"ID": 2, "Nombre": "Mesa", "Cantidad": 50}
        ]

    def get_materia_prima(self):
        return self.materia_prima

    def get_producto_terminado(self):
        return self.producto_terminado

    def search_materia_prima(self, query, column):
        """Búsqueda en materia prima."""
        return [mat for mat in self.materia_prima if query.lower() in str(mat[column]).lower()]

    def search_producto_terminado(self, query, column):
        """Búsqueda en producto terminado."""
        return [prod for prod in self.producto_terminado if query.lower() in str(prod[column]).lower()]

    def add_materia_prima(self, id, nombre, cantidad):
        """Agrega una nueva materia prima."""
        self.materia_prima.append({"ID": id, "Nombre": nombre, "Cantidad": cantidad})

    def update_materia_prima(self, id, nombre, cantidad):
        """Actualiza la materia prima."""
        for mat in self.materia_prima:
            if mat["ID"] == id:
                mat["Nombre"] = nombre
                mat["Cantidad"] = cantidad
                break

    def delete_materia_prima(self, id):
        """Elimina una materia prima por su ID."""
        self.materia_prima = [mat for mat in self.materia_prima if mat["ID"] != id]

    def add_producto_terminado(self, id, nombre, cantidad):
        """Agrega un nuevo producto terminado."""
        self.producto_terminado.append({"ID": id, "Nombre": nombre, "Cantidad": cantidad})

    def update_producto_terminado(self, id, nombre, cantidad):
        """Actualiza el producto terminado."""
        for prod in self.producto_terminado:
            if prod["ID"] == id:
                prod["Nombre"] = nombre
                prod["Cantidad"] = cantidad
                break

    def delete_producto_terminado(self, id):
        """Elimina un producto terminado por su ID."""
        self.producto_terminado = [prod for prod in self.producto_terminado if prod["ID"] != id]
