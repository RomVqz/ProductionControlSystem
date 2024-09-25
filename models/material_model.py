# models/material_model.py

class MaterialsModel:
    def __init__(self):
        # Simulación de datos en lugar de una base de datos real
        self.materials = [
            {"ID": 1, "Nombre": "Acero", "Cantidad_Disponible": 500, "Stock_Minimo": 100},
            {"ID": 2, "Nombre": "Madera", "Cantidad_Disponible": 300, "Stock_Minimo": 50}
        ]
        self.next_id = 3  # Para asignar IDs únicos

    def get_materials(self):
        return self.materials

    def add_material(self, nombre, cantidad_disponible, stock_minimo):
        new_material = {
            "ID": self.next_id,
            "Nombre": nombre,
            "Cantidad_Disponible": cantidad_disponible,
            "Stock_Minimo": stock_minimo
        }
        self.materials.append(new_material)
        self.next_id += 1

    def update_material(self, material_id, nombre, cantidad_disponible, stock_minimo):
        for material in self.materials:
            if material["ID"] == material_id:
                material["Nombre"] = nombre
                material["Cantidad_Disponible"] = cantidad_disponible
                material["Stock_Minimo"] = stock_minimo
                break

    def delete_material(self, material_id):
        self.materials = [m for m in self.materials if m["ID"] != material_id]

    def search_materials(self, search_term):
        return [m for m in self.materials if search_term.lower() in m["Nombre"].lower()]