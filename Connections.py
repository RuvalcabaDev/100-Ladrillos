import pymysql
import os
from fastapi import FastAPI
from database import User
from database import Property
from database import ShoppingCart
from database import Brick
from database import OrderDetail
from database import PaymentMethods
from database import Transaction

app = FastAPI()


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


@app.on_event('startup')
def startup():
    if ConnectionMySQL.mysql_close():
        ConnectionMySQL.mysql_connect()
    ConnectionMySQL.create_tables([User, Property, ShoppingCart, Brick, OrderDetail, PaymentMethods, Transaction])


@app.on_event('shutdown')
def shutdown():
    if not ConnectionMySQL.mysql_close():
        ConnectionMySQL.mysql_close()
