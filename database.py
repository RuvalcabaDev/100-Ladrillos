from peewee import Model
from peewee import CharField
from peewee import DateTimeField
from peewee import IntegerField
from peewee import ForeignKeyField
from peewee import DecimalField
from Connections import ConnectionMySQL
from datetime import datetime


database = ConnectionMySQL()


class User(Model):
    email = CharField(max_length=60, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email

    class Meta:
        database = database.mysql_connect()
        table_name = 'users'


class Property(Model):
    name = CharField(max_length=50)
    description = CharField(max_length=250)
    total_quantity = IntegerField(10)
    remaining_bricks = IntegerField(10)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        database = database.mysql_connect()
        table_name = 'properties'


class ShoppingCart(Model):
    user_id = ForeignKeyField(User)
    total = DecimalField(max_digits=25, decimal_places=2)
    created_at = DateTimeField(datetime.now)

    def __str__(self):
        return self.total

    class Meta:
        database = database
        table_name = 'shopping_cart'


class Brick(Model):
    property_id = ForeignKeyField(Property)
    description = CharField(max_length=250)
    price = DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.price

    class Meta:
        database = database
        table_name = 'bricks'


class OrderDetail(Model):
    brick_id = ForeignKeyField(Brick)
    shopping_cart_i = ForeignKeyField(ShoppingCart)
    price = DecimalField(max_digits=20, decimal_places=2)
    created_at = DateTimeField(datetime.now)

    def __str__(self):
        return self.price

    class Meta:
        database = database
        table_name = 'order_detail'


class PaymentMethods(Model):
    name = CharField(max_length=50, unique=True)
    description = CharField(max_length=250)
    created_at = DateTimeField(datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        database = database
        table_name = 'payment_methods'


class Transaction(Model):
    user_id = ForeignKeyField(User)
    payment_method_id = ForeignKeyField(PaymentMethods)
    total_paid = DecimalField(max_digits=25, decimal_places=2)
    created_at = DateTimeField(datetime.now)

    def __str__(self):
        return self.total_paid

    class Meta:
        database = database
        table_name = 'transactions'
