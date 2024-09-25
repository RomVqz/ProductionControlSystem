# models/empleado_model.py
from database.config import get_db_connection
import psycopg2
from tkinter import messagebox
from datetime import datetime

class EmpleadoModel:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def get_empleados(self):
        try:
            # Consulta SQL para obtener todos los empleados
            self.cursor.execute("SELECT id, nombre, puesto, turno, turno_id FROM empleados")
            rows = self.cursor.fetchall()

            # Convertir el resultado de la consulta a una lista de diccionarios
            empleados = []
            for row in rows:
                empleado = {
                    "id": row[0],
                    "nombre": row[1],
                    "puesto": row[2],
                    "turno": row[3],
                    "turno_id": row[4]
                }
                empleados.append(empleado)
            return empleados
        except psycopg2.Error as e:
            messagebox.showerror(f"Error al obtener los empleados: {e}")
            return []

    def add_empleado(self, nombre, puesto, turno, turno_id):
        try:
            # Consulta SQL para insertar un nuevo empleado
            insert_query = """
               INSERT INTO empleados (nombre, puesto, turno, turno_id)
               VALUES (%s, %s, %s, %s)
               """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(insert_query, (nombre, puesto, turno, turno_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo("Nuevo empleado agregado correctamente.")

        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al agregar el empleado: {e}")

    def update_empleado(self, empleado_id, nombre, puesto, turno, turno_id):
        try:
            # Consulta SQL para actualizar un empleado
            update_query = """
               UPDATE empleados
               SET nombre = %s, puesto = %s, turno = %s, turno_id = %s
               WHERE id = %s
               """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(update_query, (nombre, puesto, turno, turno_id, empleado_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo(f"Empleado con ID {empleado_id} actualizado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al actualizar el empleado: {e}")

    def delete_empleado(self, empleado_id):
        try:
            # Consulta SQL para eliminar un empleado por su ID
            delete_query = """
               DELETE FROM empleados
               WHERE id = %s
               """
            # Ejecutar la consulta con el ID correspondiente
            self.cursor.execute(delete_query, (empleado_id,))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            messagebox.showinfo(f"Empleado con ID {empleado_id} eliminado correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            messagebox.showerror(f"Error al eliminar el empleado: {e}")

    def search_empleados(self, search_term):
        search_term = search_term.lower()
        return [
            p for p in self.get_empleados()
            if (search_term in str(p["id"]).lower() or
                search_term in p["nombre"].lower())

        ]