import psycopg2

def get_db_connection():
    """Establece y devuelve una conexión a la base de datos PostgreSQL."""
    hostname = 'localhost'  # Cambia esto si es necesario
    database = 'NttArneses'
    username = 'postgres'
    password = 'Temerario123'
    port = '5432'  # Puerto por defecto de PostgreSQL

    try:
        # Establecer la conexión
        conn = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=password,
            port=port
        )
        print("Conexión a la base de datos establecida.")
        return conn
    except Exception as error:
        print("Error al conectar a la base de datos:", error)
        return None

def close_db_connection(conn):
    """Cierra la conexión a la base de datos."""
    if conn:
        conn.close()
        print("Conexión a la base de datos cerrada.")


