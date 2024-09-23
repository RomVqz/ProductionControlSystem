from database.queries import Queries

class OrdenModel:
    def __init__(self, id=None, producto_id=None, cantidad=None, fecha_inicio=None, fecha_fin=None, estado=None, cliente_id=None):
        self.id = id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.cliente_id = cliente_id

    @staticmethod
    def get_all_ordenes():
        query = "SELECT * FROM ordenes_produccion"
        return Queries.execute_read_query(query)

    @staticmethod
    def get_orden_by_id(orden_id):
        query = f"SELECT * FROM ordenes_produccion WHERE id = {orden_id}"
        return Queries.execute_read_query(query)

    @staticmethod
    def add_orden(producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        query = f"""
        INSERT INTO ordenes_produccion (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id) 
        VALUES ({producto_id}, {cantidad}, '{fecha_inicio}', '{fecha_fin}', '{estado}', {cliente_id})
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def update_orden(orden_id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        query = f"""
        UPDATE ordenes_produccion 
        SET producto_id = {producto_id}, cantidad = {cantidad}, fecha_inicio = '{fecha_inicio}', fecha_fin = '{fecha_fin}', 
            estado = '{estado}', cliente_id = {cliente_id}
        WHERE id = {orden_id}
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def delete_orden(orden_id):
        query = f"DELETE FROM ordenes_produccion WHERE id = {orden_id}"
        return Queries.execute_write_query(query)
