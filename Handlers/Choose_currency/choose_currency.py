from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards import getChoosePaymentType, getCryptoCoinType

async def choose_currency(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    choose_currency = ReplyKeyboardMarkup(resize_keyboard=True)
    choose_currency.add(*getChoosePaymentType(lc))

    await bot.send_message(user_id, lc["ChooseGateWay"], reply_markup=choose_currency)

async def choose_crypte_currency(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    choose_currency = ReplyKeyboardMarkup(resize_keyboard=True)
    choose_currency.add(*getCryptoCoinType(lc))

    await bot.send_message(user_id, lc["ChooseCoinType"], reply_markup=choose_currency)

