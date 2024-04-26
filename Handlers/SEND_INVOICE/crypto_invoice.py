from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards import getCryptoPayKey, getMenuButtons
from Bot.products_dict import costs
from crypto_payments.crypro_payments import *
from DB.invoice import addInvoice
from utility.constants.db_constant import *
import datetime

async def send_crypto_invoice(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.currency_crypto, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        
        if not("product_name" in data):
            reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.add(*getMenuButtons(lc))
            await bot.send_message(user_id, lc["ProductIsNotDefined"],reply_markup=reply_markup)
            return None

        reply_markup = InlineKeyboardMarkup()
        currency = message.text

        exchanges_rates = await cryptoPay.get_exchange_rates()

        
        if currency == "USDT":
            sum = costs["RUB"][data['product_name']] / exchanges_rates[0].rate
            print(exchanges_rates[0])

        elif currency == "TON":
            sum = costs["RUB"][data['product_name']] / exchanges_rates[20].rate
            print(exchanges_rates[20])

        elif currency == "BTC":
            sum = costs["RUB"][data['product_name']] / exchanges_rates[60].rate
            print(exchanges_rates[60])


        paid_btn_name = PaidButtons.CALLBACK

        invoice = await cryptoPay.create_invoice(asset=currency, amount=sum, 
                                                 paid_btn_name = paid_btn_name, 
                                                 paid_btn_url = "https://t.me/NatalChartGenBot",
                                                 payload = data['product_name'])
        
        active_invoices.status = True

        crypto_url = invoice.bot_invoice_url
        reply_markup.add(*getCryptoPayKey(lc, crypto_url))

        await bot.send_message(user_id, lc["InvoiceForPayment"].format(lc[data['product_name']],sum, currency), reply_markup=reply_markup)

        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.add(*getMenuButtons(lc))
        await bot.send_message(user_id, lc["MainMenu"],reply_markup=reply_markup)
            
        
        crypto_invoice_id = invoice.invoice_id
        creation_date = datetime.datetime.today()
        expired_date = creation_date + datetime.timedelta(minutes=15)
        poduct_id = products.get(products.name == data['product_name'])
        gateway = PaymentType.CRYPTO
        currency = invoice.asset
        amount = sum
        status = InvoiceStatus.ACTIVE    

        invoice_id = addInvoice(
            chat_id=user_id,
            product_id=poduct_id,
            creation_date=creation_date,
            expired_date=expired_date,
            gateway=gateway,
            currency=currency,
            amount=amount,
            status=status,
            crypto_invoice_id=crypto_invoice_id
        )