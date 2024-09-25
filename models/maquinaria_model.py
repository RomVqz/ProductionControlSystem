from database.config import get_db_connection
import psycopg2

class MaquinasModel:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def get_maquinas(self):
        try:
            # Consulta SQL para obtener todas las máquinas
            self.cursor.execute("SELECT id, nombre, estado, last_maintenance FROM maquinas")
            rows = self.cursor.fetchall()

            # Convertir el resultado de la consulta a una lista de diccionarios
            maquinas = []
            for row in rows:
                maquina = {
                    "id": row[0],
                    "nombre": row[1],
                    "estado": row[2],
                    "last_maintenance": row[3]
                }
                maquinas.append(maquina)
            return maquinas
        except psycopg2.Error as e:
            print(f"Error al obtener las máquinas: {e}")
            return []

    def add_maquina(self, nombre, estado, last_maintenance):
        try:
            # Consulta SQL para insertar una nueva máquina
            insert_query = """
            INSERT INTO maquinas (nombre, estado, last_maintenance)
            VALUES (%s, %s, %s)
            """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(insert_query, (nombre, estado, last_maintenance))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print("Nueva máquina agregada correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al agregar la máquina: {e}")

    def update_maquina(self, maquina_id, nombre, estado, last_maintenance):
        try:
            # Consulta SQL para actualizar una máquina
            update_query = """
            UPDATE maquinas
            SET nombre = %s, estado = %s, last_maintenance = %s
            WHERE id = %s
            """
            # Ejecutar la consulta con los valores correspondientes
            self.cursor.execute(update_query, (nombre, estado, last_maintenance, maquina_id))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Máquina con ID {maquina_id} actualizada correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al actualizar la máquina: {e}")

    def delete_maquina(self, maquina_id):
        try:
            # Consulta SQL para eliminar una máquina por su ID
            delete_query = """
            DELETE FROM maquinas
            WHERE id = %s
            """
            # Ejecutar la consulta con el ID correspondiente
            self.cursor.execute(delete_query, (maquina_id,))

            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Máquina con ID {maquina_id} eliminada correctamente.")
        except psycopg2.Error as e:
            # En caso de error, hacer rollback para deshacer la transacción
            self.connection.rollback()
            print(f"Error al eliminar la máquina: {e}")

    def search_maquinas(self, search_term):
        search_term = search_term.lower()
        return [
            p for p in self.get_maquinas()
            if (search_term in str(p["id"]).lower() or
                search_term in p["nombre"].lower()or
                search_term in p["estado"].lower() )

        ]