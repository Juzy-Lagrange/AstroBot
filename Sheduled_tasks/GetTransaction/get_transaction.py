from Bot.bot import *
from peewee import *
from utility.constants.db_constant import InvoiceStatus
from DB.invoice import updInvoiceStatus
from DB.tranzactions import addTranzactions
from Handlers.PaymentsHandlers.crypto_payment import successful_payment
import datetime

async def add_crypto_transactions(bot: AsyncTeleBot):
    queried_invoices = (invoices
                        .select(invoices.crypto_invoice_id)
                        .where((invoices.status == InvoiceStatus.ACTIVE) &
                              (invoices.crypto_invoice_id != None))).execute()
    
    crypto_invoice_ids = []

    if (len(queried_invoices) == 0):
        active_invoices.status = False
        return None

    for crypto_invoice in queried_invoices:
        if(crypto_invoice.crypto_invoice_id != None):
           crypto_invoice_ids.append(crypto_invoice.crypto_invoice_id)

    crypto_invoices_list = ','.join(map(str,crypto_invoice_ids))

    crypto_transactions = await cryptoPay.get_invoices(
        invoice_ids = crypto_invoices_list, 
        status=InvoiceStatus.PAID)

    if (crypto_transactions == None):
        #print("NO paid transactions")
        return None

    print(crypto_transactions, type(crypto_transactions))

    for crypto_transaction in crypto_transactions:
        print("NEW CRYPTO TRANSACTION")

        invoice, transaction = addTranzactions(
            invoice_id = invoices.get(invoices.crypto_invoice_id == crypto_transaction.invoice_id),
            paid_amount=crypto_transaction.paid_amount,
            currency=crypto_transaction.asset,
            usd_rate=crypto_transaction.paid_usd_rate,
            currency_fee=crypto_transaction.fee_asset,
            fee_amount=crypto_transaction.fee_amount
        )
        await send_product_for_paid_invoice(invoice, transaction, bot)
        

async def send_product_for_paid_invoice(invoice, transaction, bot: AsyncTeleBot):
    print(invoice)
    product_info_params = {
        "chat_id" : invoice.chat_id,
        "product_name" : products.get(products.id == invoice.product_id).name,
        "total_amount" : transaction.paid_amount,
        "currency": transaction.currency,
        "bot" : bot}

    print(product_info_params)
    await successful_payment(**product_info_params)




async def check_active_invoices(bot:AsyncTeleBot):
    
    if not(active_invoices.status):
        return None
    
    await add_crypto_transactions(bot)


    queried_invoices = (invoices
                        .select()
                        .where((invoices.status == InvoiceStatus.ACTIVE) & 
                               (datetime.datetime.today()>invoices.expired_date))).execute()
 
    if (len(queried_invoices) != 0):
        for invoice in queried_invoices:
            updInvoiceStatus(invoice, InvoiceStatus.EXPIRED)
    
