from Bot.bot import *
from utility import GetLocalizationIfUserSession
from Bot.products_dict import costs
from utility.constants.db_constant import *
from telegram_objects.keyboards import getMenuButtons
from DB.invoice import addInvoice
import datetime

async def send_rub_invoice(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.currency_rub, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        #addPurchase

        if not("product_name" in data):
            reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.add(*getMenuButtons(lc))
            await bot.send_message(user_id, lc["ProductIsNotDefined"],reply_markup=reply_markup)
            return None

        invoice_parameters = ProductFabricMethod.getProduct(data['product_name'], session.getLang(user_id), costs["RUB"][data['product_name']]).getProductParameters()

        creation_date = datetime.datetime.today()
        expired_data = creation_date + datetime.timedelta(minutes=15)
        poduct_id = products.get(products.name == data['product_name'])
        gateway = PaymentType.FIAT
        currency = CurrencyType.RUB
        amount = costs["RUB"][data['product_name']]
        status = InvoiceStatus.ACTIVE

        invoice_id = addInvoice(user_id, poduct_id, creation_date, expired_data, gateway, currency, amount, status)
        invoice_parameters['invoice_payload'] += f"|{invoice_id}"
        
        await bot.send_invoice(user_id, **invoice_parameters)
        active_invoices.status = True

        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.add(*getMenuButtons(lc))
        await bot.send_message(user_id, lc["MainMenu"],reply_markup=reply_markup)


#1 -> invoice(new)
#2 send to user -> invoice(status=pending)

# NEW tranzactions -> invoice(status=success)
# 
