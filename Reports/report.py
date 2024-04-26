import pandas as pd
import datetime as dt
from Bot.bot import telegram_user, invoices, products, tranzactions, ledger
from peewee import JOIN

#Generate xlsx invoice report|| return (path_to_file: str)
def generate_invoice_report(start_date, end_date) -> str:
    invoice_query = (invoices.select(
                        invoices.id, 
                        invoices.crypto_invoice_id, 
                        invoices.chat_id,
                        telegram_user.username,
                        products.name, 
                        invoices.creation_date, 
                        invoices.expired_date, 
                        invoices.gateway, 
                        invoices.currency, 
                        invoices.amount, 
                        invoices.status, 
                        invoices.comment)
                .join(telegram_user, join_type=JOIN.LEFT_OUTER, on=(invoices.chat_id == telegram_user.chat_id))
                .join(products, join_type=JOIN.LEFT_OUTER, on=(invoices.product_id == products.id))
                .where(invoices.creation_date.between(start_date, end_date)))
    column_names = {
        'chat': 'chat_id',
        'name': 'product_name'
    }
    invoice_df = pd.DataFrame(list(invoice_query.dicts())).rename(columns = column_names)

    excel_path = fr'Reports\invoices\invoices_report_{start_date.date()}_{end_date.date()}.xlsx'
    invoice_df.to_excel(excel_path, sheet_name='invoices_spreadsheet')
    return excel_path


#Generate xlsx invoice report|| return (path_to_file: str)
def generate_transactions_report(start_date, end_date) -> str:
    transactions_query = (tranzactions.select(
                            tranzactions.id, 
                            tranzactions.invoice_id,
                            tranzactions.paid_amount,
                            tranzactions.currency,
                            tranzactions.usd_rate,
                            tranzactions.currency_fee,
                            tranzactions.fee_amount,
                            tranzactions.status
                            ).join(invoices, JOIN.LEFT_OUTER, on=(tranzactions.invoice_id == invoices.id))
                            .where(invoices.creation_date.between(start_date, end_date))
                        )
    transactions_df = pd.DataFrame(list(transactions_query.dicts()))

    excel_path = fr'Reports\transactions\transactions_report_{start_date.date()}_{end_date.date()}.xlsx'
    transactions_df.to_excel(excel_path, sheet_name='transactions_spreadsheet')
    return excel_path




#Generate xlsx invoice report|| return (path_to_file: str)
def generate_ledger_report(start_date, end_date) -> str:
    ledger_query = (ledger.select().where(ledger.created_at.between(start_date, end_date)))
    ledger_df = pd.DataFrame(list(ledger_query.dicts()))

    excel_path = fr'Reports\ledger\ledger_report_{start_date.date()}_{end_date.date()}.xlsx'
    ledger_df.to_excel(excel_path, sheet_name='ledger_spreadsheet')
    return excel_path