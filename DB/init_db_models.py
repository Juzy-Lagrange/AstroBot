from playhouse.reflection import generate_models
from peewee_async import Manager, MySQLDatabase

from peewee import *
import datetime


database  = MySQLDatabase('astro-bot', user='root', 
                          password='root', host='localhost')
database.connect()
Models = generate_models(database)
database.close()

ledger = Models['ledger']
telegram_user = Models['telegram_user']
products = Models['products']
invoices = Models['invoices']
tranzactions = Models['tranzactions']

# def write_purchase(user_id, total_amount, product_name):
#     product_id = Models['product_types'].get(Models['product_types'].name == product_name).id
#     purchase = {
#         'chat_id': user_id,
#         'product_type': product_id,  
#         'date': datetime.date.today().__str__(),
#         'sum': total_amount,
#     }
#     Models['purchases'].insert(purchase).execute()


# SELECT tu.username, pu.date, pu.sum/100, pt.name  
# FROM `astro-bot`.telegram_user AS tu
# LEFT JOIN  `astro-bot`.purchases AS pu ON (tu.chat_id = pu.chat_id)
# LEFT JOIN  `astro-bot`.product_types AS pt ON (pu.product_type = pt.id)
# WHERE tu.chat_id = "718202048";


def GetAvailableProducts(user_id):
    query_available_products = (telegram_user
                    .select(telegram_user.horoscope_active_date, telegram_user.taro_count, telegram_user.unlimited_taro, telegram_user.natal_chart_count)
                    .where(telegram_user.chat_id == user_id).dicts())
    
    query_available_products = [i for i in query_available_products]
    return query_available_products

def GetAllUserPurchase(user_id):
    query_all_user_purchase = (telegram_user
                .select(telegram_user.username, invoices.creation_date, invoices.amount, invoices.currency, products.name)
                .join(invoices, join_type=JOIN.LEFT_OUTER, on=(telegram_user.chat_id == invoices.chat_id))
                .join(products, join_type=JOIN.LEFT_OUTER, on=(invoices.product_id == products.id))
                .where(telegram_user.chat_id == user_id).dicts())
    
    query_all_user_purchase = [i for i in query_all_user_purchase]
    return query_all_user_purchase
