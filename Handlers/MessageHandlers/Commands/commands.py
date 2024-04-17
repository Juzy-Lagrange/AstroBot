from telegram_objects.keyboards import getLangKeys
from telebot.types import ReplyKeyboardMarkup
from telebot.async_telebot import AsyncTeleBot

async def send_greetings(message, bot: AsyncTeleBot):
    lang_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_markup.add(*getLangKeys())
    await bot.reply_to(message, "Choose language:", reply_markup = lang_markup)