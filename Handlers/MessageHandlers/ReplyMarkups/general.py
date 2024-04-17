from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards import getFunctionKeys, getSettingsButton, getPlansButtons

async def send_abilities(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_abilities_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_abilities_markup.add(*getFunctionKeys(lc))

    await bot.send_message(user_id, lc["Abilities"], reply_markup = reply_abilities_markup)

async def send_settings(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_settings_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_settings_markup.add(*getSettingsButton(lc))

    await bot.send_message(user_id, lc["Settings"], reply_markup = reply_settings_markup)

async def send_plans(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    inline_plans_markup = InlineKeyboardMarkup()
    inline_plans_markup.add(*getPlansButtons(lc))
    await bot.send_message(user_id, lc["Plans"], reply_markup = inline_plans_markup)

async def send_user_orders(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

async def send_supports(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

async def send_topics(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

async def send_natal_chart_description(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
