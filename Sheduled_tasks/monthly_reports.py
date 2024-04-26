from Bot.bot import *
from Reports.report import *
import datetime

async def send_monthly_reports(bot: AsyncTeleBot):
    start_date = datetime.datetime.today() - datetime.timedelta(days=31)
    end_date = datetime.datetime.today()

    reports_list = [
        generate_invoice_report(start_date, end_date),
        generate_transactions_report(start_date, end_date),
        generate_ledger_report(start_date, end_date)
    ]


    for admin in admin_ids:
        await bot.send_message(admin,"Ежемесячный отчет")
        for document in reports_list:
            await bot.send_document(admin, InputFile(document))