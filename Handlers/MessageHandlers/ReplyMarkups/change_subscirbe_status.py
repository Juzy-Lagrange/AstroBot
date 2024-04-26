from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards.keyboards import getSettingsButtonUnSubsribe, getSettingsButtonSubsribe

async def change_subscribe_status(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    current_user = telegram_user.get(telegram_user.chat_id ==  user_id)
    current_user.subscribe_status = not(current_user.subscribe_status)

    reply_settings_markup = ReplyKeyboardMarkup(resize_keyboard=True)

    if (current_user.subscribe_status == True):
        reply_settings_markup.add(*getSettingsButtonUnSubsribe(lc))
    else:
        reply_settings_markup.add(*getSettingsButtonSubsribe(lc))

    if (current_user.subscribe_status):
        await bot.send_message(user_id, lc["Subscribe"], reply_markup = reply_settings_markup)
    else:
        await bot.send_message(user_id, lc["Unsubscribe"], reply_markup = reply_settings_markup)
    current_user.save()