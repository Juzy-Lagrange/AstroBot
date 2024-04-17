from playhouse.reflection import generate_models
from peewee_async import Manager, MySQLDatabase
import peewee


database  = MySQLDatabase('astro-bot', user='root', 
                          password='root', host='localhost')
database.connect()
Models = generate_models(database)
database.close()
