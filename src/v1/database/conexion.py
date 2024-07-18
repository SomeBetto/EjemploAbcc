import psycopg2
from psycopg2 import Error

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Conexión exitosa a la base de datos PostgreSQL")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Desconexión de la base de datos PostgreSQL")

    def execute_query(self, query):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("Consulta ejecutada exitosamente")
                return cursor.fetchall()
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
        else:
            print("No hay conexión activa a la base de datos")