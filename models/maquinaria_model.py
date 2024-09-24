class MaquinariaModel:
    def __init__(self):
        # Simulación de datos de maquinaria
        self.maquinaria = [
            {"ID": 1, "Nombre": "Torno", "Estado": "Operativo"},
            {"ID": 2, "Nombre": "Fresadora", "Estado": "Mantenimiento"}
        ]

    def get_maquinaria(self):
        return self.maquinaria

    def search_maquinaria(self, query, column):
        """Realiza una búsqueda de maquinaria en función de la columna seleccionada."""
        return [maq for maq in self.maquinaria if query.lower() in str(maq[column]).lower()]

    def add_maquinaria(self, id, nombre, estado):
        """Agrega nueva maquinaria a la lista."""
        self.maquinaria.append({"ID": id, "Nombre": nombre, "Estado": estado})

    def update_maquinaria(self, id, nombre, estado):
        """Actualiza una maquinaria existente."""
        for maq in self.maquinaria:
            if maq["ID"] == id:
                maq["Nombre"] = nombre
                maq["Estado"] = estado
                break

    def delete_maquinaria(self, id):
        """Elimina una maquinaria por su ID."""
        self.maquinaria = [maq for maq in self.maquinaria if maq["ID"] != id]
