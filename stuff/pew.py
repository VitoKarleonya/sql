from peewee import *

conn = SqliteDataBase('db1.sqlite')

class User(Model):
	firstname = CharField(column_name = 'firstname')
	lastname = CharField(column_name = 'lastname')
	age = IntegerField(column_name = 'age')

	class Meta:
		database = conn


class Product(Model):
	name = CharField(column_name = 'name')
	category = IntegerField(column_name = 'category')
	price = IntegerField(column_name = 'price')

	class Meta:
		database = conn

User.createTable()
Product.createTable()

