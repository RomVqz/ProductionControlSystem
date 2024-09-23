from database.queries import Queries

class EmpleadoModel:
    def __init__(self, id=None, nombre=None, puesto=None, turno_id=None):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto
        self.turno_id = turno_id

    @staticmethod
    def get_all_empleados():
        query = "SELECT * FROM empleados"
        return Queries.execute_read_query(query)

    @staticmethod
    def get_empleado_by_id(empleado_id):
        query = f"SELECT * FROM empleados WHERE id = {empleado_id}"
        return Queries.execute_read_query(query)

    @staticmethod
    def add_empleado(nombre, puesto, turno, turno_id):
        query = f"""
        INSERT INTO empleados (nombre, puesto, turno, turno_id) 
        VALUES ('{nombre}', '{puesto}', '{turno}', {turno_id})
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def update_empleado(empleado_id, nombre, puesto, turno, turno_id):
        query = f"""
        UPDATE empleados 
        SET nombre = '{nombre}', puesto = '{puesto}', turno = '{turno}', turno_id = {turno_id}
        WHERE id = {empleado_id}
        """
        return Queries.execute_write_query(query)

    @staticmethod
    def delete_empleado(empleado_id):
        query = f"DELETE FROM empleados WHERE id = {empleado_id}"
        return Queries.execute_write_query(query)
