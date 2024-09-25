# models/producto_model.py
from database.config import get_db_connection
import psycopg2
from datetime import datetime
from tkinter import messagebox
from datetime import datetime


class ProductsModel:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()


    def get_products(self):
        try:
            # Consulta SQL para obtener todos los productos
            self.cursor.execute("SELECT id, nombre, descripcion, precio, created_at, updated_at FROM productos")
            rows = self.cursor.fetchall()

            # Convertir el resultado de la consulta a una lista de diccionarios
            products = []
            for row in rows:
                product = {
                    "ID": row[0],
                    "Nombre": row[1],
                    "Descripción": row[2],
                    "Precio": row[3],
                    "Created_At": row[4],
                    "Updated_At": row[5]
                }
                products.append(product)
            return products
        except psycopg2.Error as e:
            messagebox.showerror(f"Error al obtener los productos: {e}")
            return []
        finally:
            # No cerramos la conexión aquí para mantenerla abierta mientras el modelo esté en uso
            pass

    def add_product(self, nombre, descripcion, precio):
        try:
            # Fecha actual para 'Created_At' y 'Updated_At'
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Consulta SQL para insertar un nuevo producto
            insert_query = """
               INSERT INTO productos (nombre, descripcion, precio, created_at, updated_at)
               VALUES (%s, %s, %s, %s, %s)
               """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(insert_query, (nombre, descripcion, precio, current_date, current_date))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo(f"Producto '{nombre}' agregado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al agregar el producto: {e}")

    def update_product(self, product_id, nombre, descripcion, precio):
        try:
            # Fecha actual para 'Updated_At'
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Consulta SQL para actualizar un producto
            update_query = """
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio = %s, updated_at = %s
            WHERE id = %s
            """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(update_query, (nombre, descripcion, precio, current_date, product_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo(f"Producto con ID {product_id} actualizado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al actualizar el producto: {e}")

    def delete_product(self, product_id):
        try:
            # Consulta SQL para eliminar un producto por su ID
            delete_query = """
            DELETE FROM productos
            WHERE id = %s
            """
            # Ejecutar la consulta con el ID correspondiente
            self.cursor.execute(delete_query, (product_id,))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo(f"Producto con ID {product_id} eliminado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al eliminar el producto: {e}")

    def search_products(self, search_term):
        search_term = search_term.lower()
        return [
            p for p in self.get_products()
            if (search_term in str(p["ID"]).lower() or
                search_term in p["Nombre"].lower())

        ]