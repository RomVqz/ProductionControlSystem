from database.queries import Queries

class MantenimientoModel:
    def __init__(self, id=None, maquina_id=None, fecha_mantenimiento=None, tipo_mantenimiento=None, descripcion=None, tecnico=None, costo=None):
        self.id = id
        self.maquina_id = maquina_id
        self.fecha_mantenimiento = fecha_mantenimiento
        self.tipo_mantenimiento = tipo_mantenimiento
        self.descripcion = descripcion
        self.tecnico = tecnico
        self.costo = costo

    @staticmethod
    def get_all_mantenimientos():
        query = "SELECT * FROM mantenimientos"
        return Queries.execute_read_query(query)

    @staticmethod
    def get_mantenimiento_by_id(mantenimiento_id):
        query = f"SELECT * FROM mantenimientos WHERE id = {mantenimiento_id}"
        return Queries.execute_read_query(query)

    @staticmethod
    def add_mantenimiento(maquina_id, fecha_mantenimiento, tipo_mantenimiento, descripcion, tecnico, costo):
        query = f"""
        INSERT INTO mantenimientos (maquina_id, fecha_mantenimiento, tipo_mantenimiento, descripcion, tecnico, costo) 
        VALUES ({maquina_id}, '{fecha_mantenimiento}', '{tipo_mantenimiento}', '{descripcion}', '{tecnico}', {costo})
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def update_mantenimiento(mantenimiento_id, maquina_id, fecha_mantenimiento, tipo_mantenimiento, descripcion, tecnico, costo):
        query = f"""
        UPDATE mantenimientos 
        SET maquina_id = {maquina_id}, fecha_mantenimiento = '{fecha_mantenimiento}', tipo_mantenimiento = '{tipo_mantenimiento}', 
            descripcion = '{descripcion}', tecnico = '{tecnico}', costo = {costo}
        WHERE id = {mantenimiento_id}
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def delete_mantenimiento(mantenimiento_id):
        query = f"DELETE FROM mantenimientos WHERE id = {mantenimiento_id}"
        return Queries.execute_write_query(query)
