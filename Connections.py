import pymysql
import os


class ConnectionMySQL:
    cursor = None
    connection = None

    def mysql_connect(self):
        self.connection = pymysql.connect(
            host=os.environ.get('DATABASE_HOST'),
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            port=int(os.environ.get('DATABASE_PORT')),
            db=os.environ.get('DATABASE_NAME')
        )
        self.cursor = self.connection.cursor()
        print("Conexión establecida!")

    def mysql_close(self):
        print("Conexión cerrada!")
        self.connection.close()
