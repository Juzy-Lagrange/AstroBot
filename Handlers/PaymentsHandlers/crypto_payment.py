from Bot.bot import *
from DB.tranzactions import addTranzactions
from Handlers.MessageHandlers.ReplyMarkups.horoscope import send_my_horoscope
from Handlers.PaymentsHandlers.SendProductsresult.plans import *

from utility import getUserLocalization, tryGenURLProfile, GenerateNatalChart
from utility import generate_one_card, generate_three_cards
from utility import add_one_month, add_three_month, add_one_year
from utility import GeoModule as GM

from utility.constants.db_constant import *
from telegram_objects.keyboards import getChoosePaymentType
from asyncio import sleep as async_sleep

async def successful_payment(chat_id, product_name, total_amount, currency, bot: AsyncTeleBot):
    message = ""
    user_id = int(chat_id)
    lc = getUserLocalization(user_id)

    text = lc["SuccessPayment"]+'\n'+lc["YourProduct"].format(lc[product_name], total_amount, currency)
    await bot.send_message(user_id, text=text)

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

    if product_name == "three_month_horoscope":
        await add_three_month(user_id, lc, bot)

    if product_name == "one_year_horoscope":
        await add_one_year(user_id,lc,bot)

    if product_name == "natal_chart":
        await async_sleep(1.3)
        user_pdf_link = GenerateNatalChart(user_id,lc,bot)
        await bot.send_message(user_id,f"[{lc['SuccesfulyGenerated']}]({user_pdf_link})", parse_mode='MarkdownV2')
