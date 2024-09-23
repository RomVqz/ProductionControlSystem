import psycopg2
from config import get_db_connection, close_db_connection


# Función para crear las tablas
def create_tables():
    """Crear todas las tablas necesarias en la base de datos."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            contacto TEXT,
            telefono TEXT,
            direccion TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS maquinas (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            estado TEXT,
            last_maintenance DATE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio NUMERIC(10, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ordenes_produccion (
            id SERIAL PRIMARY KEY,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER,
            fecha_inicio DATE,
            fecha_fin DATE,
            estado TEXT,
            cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS empleados (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            puesto TEXT,
            turno TEXT,
            turno_id INTEGER REFERENCES turnos(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS turnos (
            id SERIAL PRIMARY KEY,
            nombre_turno TEXT NOT NULL,
            hora_inicio TIME,
            hora_fin TIME
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS inventario (
            id SERIAL PRIMARY KEY,
            material_id INTEGER REFERENCES materiales(id),
            fecha DATE,
            tipo_transaccion TEXT,
            cantidad INTEGER,
            empleado_id INTEGER REFERENCES empleados(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS materiales (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            cantidad_disponible INTEGER,
            stock_minimo INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS boms (
            id SERIAL PRIMARY KEY,
            producto_id INTEGER REFERENCES productos(id),
            cantidad INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS costos_produccion (
            id SERIAL PRIMARY KEY,
            orden_id INTEGER REFERENCES ordenes_produccion(id),
            costo_materiales NUMERIC(10, 2),
            costo_mano_obra NUMERIC(10, 2),
            costo_maquinaria NUMERIC(10, 2),
            total_costo NUMERIC(10, 2)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS asignaciones (
            id SERIAL PRIMARY KEY,
            empleado_id INTEGER REFERENCES empleados(id),
            maquina_id INTEGER REFERENCES maquinas(id),
            orden_id INTEGER REFERENCES ordenes_produccion(id),
            fecha_mantenimiento DATE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS mantenimientos (
            id SERIAL PRIMARY KEY,
            maquina_id INTEGER REFERENCES maquinas(id),
            fecha_mantenimiento DATE,
            tipo_mantenimiento TEXT,
            descripcion TEXT,
            tecnico TEXT,
            costo NUMERIC(10, 2)
        )
        """
    )

    # Establecer conexión a la base de datos
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Ejecutar cada comando SQL para crear tablas
        for command in commands:
            cursor.execute(command)

        # Guardar los cambios
        connection.commit()

        print("Tablas creadas correctamente.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error al crear tablas: {error}")
        if connection:
            connection.rollback()  # Revertir en caso de error
    finally:
        # Cerrar la conexión
        if connection:
            cursor.close()
            close_db_connection(connection)


# Ejecutar el script de creación de tablas
if __name__ == "__main__":
    create_tables()
