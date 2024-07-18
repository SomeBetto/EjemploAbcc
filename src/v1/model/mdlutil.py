from src.v1.database.conexion import PostgreSQLConnection
class MdlUtil():
    def __init__(self):
        self._statusoperacion=None
    @staticmethod
    def validarconexiondb():
        try:
            # Instanciar la clase
            connection = PostgreSQLConnection(
                dbname='postgres',
                user='postgres',
                password='postgress'
            )

            # Conectar a la base de datos
            connection.connect()

            # Ejecutar una consulwta
            query = "SELECT 'OK';"
            resultado=None
            results = connection.execute_query(query)
            if results:
                print("Resultados de la consulta:")
                for row in results:
                    print(row)
                    resultado=row

            # Desconectar de la base de datos
            connection.disconnect()
            return resultado
        except Exception as e:
            return e
    @staticmethod
    def check_api_health():
        return 'API is healthy'
    