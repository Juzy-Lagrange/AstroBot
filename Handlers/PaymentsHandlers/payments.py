from Bot.bot import *
from DB.tranzactions import addTranzactions
from Handlers.MessageHandlers.ReplyMarkups.horoscope import send_my_horoscope
from Handlers.PaymentsHandlers.SendProductsresult.plans import *

from utility import GetLocalizationIfUserSession, tryGenURLProfile, GenerateNatalChart
from utility import generate_one_card, generate_three_cards
from utility import add_one_month, add_three_month, add_one_year
from utility import GeoModule as GM

from utility.constants.db_constant import *
from telegram_objects.keyboards import getChoosePaymentType
from asyncio import sleep as async_sleep

CONST_CONVERT_TO_RUB = 100

async def successful_payment(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    
    payment_info = message.successful_payment

    payload_list = payment_info.invoice_payload.split('|')
    product_name = payload_list[0]
    invoice_id = int(payload_list[1])
    total_amount = payment_info.total_amount/CONST_CONVERT_TO_RUB

    print(payload_list,"\n\n",payment_info)

    text = lc["SuccessPayment"]+'\n'+lc["YourProduct"].format(product_name, total_amount ,'RUB')
    await bot.send_message(user_id, text)

    addTranzactions(
        invoice_id=invoice_id,
        paid_amount=total_amount,
        currency=CurrencyType.RUB,
        currency_fee=CurrencyType.RUB,
        fee_amount=0, usd_rate=0
    )

    if product_name == "plan_waytostars":
        buy_waytostars_package(user_id)

    if product_name == "plan_astralbloom":
        buy_astral_bloom(user_id)

    if product_name == "plan_starstart":
        buy_stars_start(user_id)

    if product_name == "one_taro_gen":
        await generate_one_card(user_id, lc, bot)

    if product_name == "three_taro_gen":
        await generate_three_cards(user_id, lc, bot)

    if product_name == "one_month_horoscope":
        await add_one_month(user_id, lc, bot)
        await send_my_horoscope(message,bot)

    if product_name == "three_month_horoscope":
        await add_three_month(user_id, lc, bot)
        await send_my_horoscope(message,bot)

    if product_name == "one_year_horoscope":
        await add_one_year(user_id,lc,bot)
        await send_my_horoscope(message,bot)

    if product_name == "natal_chart":
        await async_sleep(1.3)
        user_pdf_link = GenerateNatalChart(user_id,lc,bot)
        await bot.send_message(user_id,f"[{lc['SuccesfulyGenerated']}]({user_pdf_link})", parse_mode='MarkdownV2')
    