# models/materiales_model.py

class MaterialsModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.materiales = [
            {"ID": 1, "Nombre": "Material A", "Cantidad_Disponible": 50, "Stock_Minimo": 10},
            {"ID": 2, "Nombre": "Material B", "Cantidad_Disponible": 100, "Stock_Minimo": 20}
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_materiales(self):
        return self.materiales

    def add_material(self, nombre, cantidad_disponible, stock_minimo):
        new_material = {
            "ID": self.next_id,
            "Nombre": nombre,
            "Cantidad_Disponible": cantidad_disponible,
            "Stock_Minimo": stock_minimo
        }
        self.materiales.append(new_material)
        self.next_id += 1

    def update_material(self, material_id, nombre, cantidad_disponible, stock_minimo):
        for material in self.materiales:
            if material["ID"] == material_id:
                material["Nombre"] = nombre
                material["Cantidad_Disponible"] = cantidad_disponible
                material["Stock_Minimo"] = stock_minimo
                break

    def delete_material(self, material_id):
        self.materiales = [m for m in self.materiales if m["ID"] != material_id]

    def search_materiales(self, search_term):
        return [m for m in self.materiales if search_term.lower() in m["Nombre"].lower()]
