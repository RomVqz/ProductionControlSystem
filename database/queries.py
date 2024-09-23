import psycopg2
from psycopg2 import sql
from database.config import config

class Queries:
    def __init__(self):
        # Inicializa la conexión con la base de datos PostgreSQL
        self.connection = None
        try:
            params = config()  # Obtiene la configuración de la conexión desde config.py
            self.connection = psycopg2.connect(**params)
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error al conectar a la base de datos: {error}")
            raise error

    def execute_read_query(self, query):
        """Ejecuta una consulta de lectura (SELECT) y devuelve los resultados."""
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error al ejecutar la consulta: {error}")
            raise error

    def execute_write_query(self, query):
        """Ejecuta una consulta de escritura (INSERT, UPDATE, DELETE) y guarda los cambios."""
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error al ejecutar la consulta: {error}")
            self.connection.rollback()
            raise error

    def close_connection(self):
        """Cierra la conexión con la base de datos."""
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
