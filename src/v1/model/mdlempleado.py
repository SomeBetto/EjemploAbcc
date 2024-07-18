from src.v1.model.entity.empleado import Empleado
from src.v1.database.conexion import PostgreSQLConnection
class MdlEmpleado():
    def __init__(self):
        self._statusoperacion=None
        self.empleado=Empleado()