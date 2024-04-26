from Bot.bot import *
from telegram_objects.keyboards import getLangKeys
from Handlers.MessageHandlers.ReplyMarkups.choose_language import choose_language

async def change_language(message, bot: AsyncTeleBot):
    lang_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_markup.add(*getLangKeys())
    await bot.reply_to(message, "Choose language:", reply_markup = lang_markup)