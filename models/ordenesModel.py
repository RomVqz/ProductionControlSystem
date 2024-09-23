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
        try:
            return Queries().execute_read_query(query)
        except Exception as e:
            print(f"Error al obtener todas las órdenes: {e}")
            return []

    @staticmethod
    def add_orden(producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        query = """
        INSERT INTO ordenes_produccion (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id)
        try:
            Queries().execute_write_query(query, values)
            return True
        except Exception as e:
            print(f"Error al agregar la nueva orden: {e}")
            return False

    @staticmethod
    def update_orden(orden_id, producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id):
        query = """
        UPDATE ordenes_produccion 
        SET producto_id = %s, cantidad = %s, fecha_inicio = %s, fecha_fin = %s, 
            estado = %s, cliente_id = %s
        WHERE id = %s
        """
        values = (producto_id, cantidad, fecha_inicio, fecha_fin, estado, cliente_id, orden_id)
        try:
            Queries().execute_write_query(query, values)
            return True
        except Exception as e:
            print(f"Error al actualizar la orden: {e}")
            return False

    @staticmethod
    def delete_orden(orden_id):
        query = "DELETE FROM ordenes_produccion WHERE id = %s"
        try:
            Queries().execute_write_query(query, (orden_id,))
            return True
        except Exception as e:
            print(f"Error al eliminar la orden: {e}")
            return False
