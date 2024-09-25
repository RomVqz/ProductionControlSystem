class MaterialModel:
    def __init__(self):
        # Simulación de datos de materiales
        self.materia_prima = [
            {"ID": 1, "Nombre": "Acero", "Cantidad": 500},
            {"ID": 2, "Nombre": "Plástico", "Cantidad": 300}
        ]

    def get_materia_prima(self):
        return self.materia_prima

    def search_materia_prima(self, query, column):
        """Búsqueda en materiales."""
        return [mat for mat in self.materia_prima if query.lower() in str(mat[column]).lower()]

    def add_materia_prima(self, id, nombre, cantidad):
        """Agrega un nuevo material."""
        self.materia_prima.append({"ID": id, "Nombre": nombre, "Cantidad": cantidad})

    def update_materia_prima(self, id, nombre, cantidad):
        """Actualiza el material."""
        for mat in self.materia_prima:
            if mat["ID"] == id:
                mat["Nombre"] = nombre
                mat["Cantidad"] = cantidad
                break

    def delete_materia_prima(self, id):
        """Elimina un material por su ID."""
        self.materia_prima = [mat for mat in self.materia_prima if mat["ID"] != id]
