from database.queries import Queries

class ProductoModel:
    def __init__(self, id=None, nombre=None, descripcion=None, precio=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    @staticmethod
    def get_all_productos():
        query = "SELECT * FROM productos"
        return Queries.execute_read_query(query)

    @staticmethod
    def get_producto_by_id(producto_id):
        query = f"SELECT * FROM productos WHERE id = {producto_id}"
        return Queries.execute_read_query(query)

    @staticmethod
    def add_producto(nombre, descripcion, precio):
        query = f"""
        INSERT INTO productos (nombre, descripcion, precio) 
        VALUES ('{nombre}', '{descripcion}', {precio})
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def update_producto(producto_id, nombre, descripcion, precio):
        query = f"""
        UPDATE productos 
        SET nombre = '{nombre}', descripcion = '{descripcion}', precio = {precio}
        WHERE id = {producto_id}
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def delete_producto(producto_id):
        query = f"DELETE FROM productos WHERE id = {producto_id}"
        return Queries.execute_write_query(query)
