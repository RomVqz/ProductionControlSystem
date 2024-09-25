# models/material_model.py
from database.config import get_db_connection
import psycopg2
from datetime import datetime

class MaterialsModel:
    def __init__(self):
            self.connection = get_db_connection()
            self.cursor = self.connection.cursor()

    def get_materials(self):
        try:
            # Consulta SQL para obtener todos los materiales
            self.cursor.execute("SELECT id, nombre, cantidad_disponible, stock_minimo FROM materiales")
            rows = self.cursor.fetchall()

            # Convertir el resultado de la consulta a una lista de diccionarios
            materiales = []
            for row in rows:
                material = {
                    "ID": row[0],
                    "Nombre": row[1],
                    "Cantidad_Disponible": row[2],
                    "Stock_Minimo": row[3]
                }
                materiales.append(material)
            return materiales
        except psycopg2.Error as e:
            print(f"Error al obtener los materiales: {e}")
            return []

    def add_material(self, nombre, cantidad_disponible, stock_minimo):
        try:
            # Consulta SQL para insertar un nuevo material
            insert_query = """
               INSERT INTO materiales (nombre, cantidad_disponible, stock_minimo)
               VALUES (%s, %s, %s)
               """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(insert_query, (nombre, cantidad_disponible, stock_minimo))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Material '{nombre}' agregado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al agregar el material: {e}")

    def update_material(self, material_id, nombre, cantidad_disponible, stock_minimo):
        try:
            # Consulta SQL para actualizar un material
            update_query = """
               UPDATE materiales
               SET nombre = %s, cantidad_disponible = %s, stock_minimo = %s
               WHERE id = %s
               """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(update_query, (nombre, cantidad_disponible, stock_minimo, material_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Material con ID {material_id} actualizado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al actualizar el material: {e}")

    def delete_material(self, material_id):
        try:
            # Consulta SQL para eliminar un material por su ID
            delete_query = """
               DELETE FROM materiales
               WHERE id = %s
               """
            # Ejecutar la consulta con el ID correspondiente
            self.cursor.execute(delete_query, (material_id,))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Material con ID {material_id} eliminado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al eliminar el material: {e}")

    def search_materials(self, search_term):
        search_term = search_term.lower()
        return [
            p for p in self.get_materials()
            if (search_term in str(p["ID"]).lower() or
                search_term in p["Nombre"].lower())

        ]