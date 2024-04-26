from Bot.bot import *
from utility import GetLocalizationIfUserSession, ChooseLang, zodiak_sings
from telegram_objects.keyboards import getHoroscopePage, getZodiakSings, getHoroscopePlans
from Bot.products_dict import costs

from Handlers.Choose_currency.choose_currency import choose_currency

async def send_horoscope(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add(*getHoroscopePage(lc))
    with open('./imgs/horoscope.jpg', '+rb') as photo:
        await bot.send_photo(user_id,photo=photo, caption=lc["HorosopeMessage"], parse_mode = "HTML", reply_markup = reply_markup)


async def send_my_horoscope(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    user = telegram_user.get(telegram_user.chat_id == str(user_id))
    zodiak_sign = lc[user.zodiak_sign]
    date = user.horoscope_active_date if (user.horoscope_active_date != None) else lc["NoActiveHoroscope"]

    text = lc["HoroscopeInfo"].format(user.username, zodiak_sign, date)

    await bot.send_message(user_id, text)

async def change_zodiak_sign(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add(*getZodiakSings(lc))
    await bot.send_message(user_id, lc["ChooseZodiakSign"], reply_markup=reply_markup)


async def set_zodiak_sign(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add(*getHoroscopePage(lc))

    await bot.send_message(user_id, lc["UChangeZodiakSign"],reply_markup=reply_markup)
    user = telegram_user.get(telegram_user.chat_id == str(user_id))
    user.zodiak_sign = lc[message.text]
    user.save()

async def buy_horoscope_plan(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add(*getHoroscopePlans(lc))
    await send_my_horoscope(message, bot)
    await bot.send_message(user_id,lc["ChooseHoroscopePlan"],reply_markup=reply_markup)

async def buy_one_month_plan(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["product_name"] = "one_month_horoscope"

    await choose_currency(message, bot)
    # invoice_parameters = ProductFabricMethod.getProduct('one_month_horoscope', session.getLang(user_id), costs["RUB"]["one_month_horoscope"])
    # await bot.send_invoice(user_id, **invoice_parameters.getProductParameters())

async def buy_three_month_plan(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["product_name"] = "three_month_horoscope"

    await choose_currency(message, bot)
    # invoice_parameters = ProductFabricMethod.getProduct('three_month_horoscope', session.getLang(user_id), costs["RUB"]["three_month_horoscope"])
    # await bot.send_invoice(user_id, **invoice_parameters.getProductParameters())

async def buy_one_year_plan(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["product_name"] = "one_year_horoscope"

    await choose_currency(message, bot)

    # invoice_parameters = ProductFabricMethod.getProduct('one_year_horoscope', session.getLang(user_id), costs["RUB"]["one_year_horoscope"])
    # await bot.send_invoice(user_id, **invoice_parameters.getProductParameters())