from database.config import get_db_connection
import psycopg2
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class OrdenesProduccionModel:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def get_ordenes(self):
        try:
            # Consulta SQL para obtener todas las órdenes de producción
            self.cursor.execute("SELECT id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id FROM ordenes_produccion")
            rows = self.cursor.fetchall()

            # Convertir el resultado de la consulta a una lista de diccionarios
            ordenes = []
            for row in rows:
                orden = {
                    "id": row[0],
                    "producto_id": row[1],
                    "cantidad": row[2],
                    "fecha_inicio": row[3],
                    "fecha_fin": row[4],
                    "estado": row[5],
                    "cliente_id": row[6]
                }
                ordenes.append(orden)
            return ordenes
        except psycopg2.Error as e:
            messagebox.showerror(f"Error al obtener las órdenes: {e}")
            return []

    def add_orden(self, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        try:
            # Consulta SQL para insertar una nueva orden de producción
            insert_query = """
            INSERT INTO ordenes_produccion (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(insert_query, (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo("Exito", "Orden de produccion Creada con exito")

        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror("Error", f"{e}")


    def update_orden(self, orden_id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        try:
            # Consulta SQL para actualizar una orden de producción
            update_query = """
            UPDATE ordenes_produccion
            SET producto_id = %s, cantidad = %s, fecha_inicio = %s, fecha_fin = %s, estado = %s, cliente_id = %s
            WHERE id = %s
            """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(update_query, (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id, orden_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()

            messagebox.showinfo("Exito", f"Orden de producción con ID {orden_id} actualizada correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror("Error", f"{e}")

    def delete_orden(self, orden_id):
        try:
            # Consulta SQL para eliminar una orden de producción por su ID
            delete_query = """
            DELETE FROM ordenes_produccion
            WHERE id = %s
            """
            # Ejecutar la consulta con el ID correspondiente
            self.cursor.execute(delete_query, (orden_id,))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo("Exito", f"Orden de producción con ID {orden_id} eLiminada correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror("Error", f"{e}")

    def search_ordenes(self, search_term):
        search_term = search_term.lower()
        return [
            p for p in self.get_ordenes()
            if (search_term in str(p["id"]).lower() or
                search_term in p["estado"].lower())

        ]