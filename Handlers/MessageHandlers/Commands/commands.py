from telegram_objects.keyboards import getLangKeys
from telebot.types import ReplyKeyboardMarkup
from telebot.async_telebot import AsyncTeleBot
from Handlers.MessageHandlers.ReplyMarkups.general import send_supports, send_natal_chart_description, send_plans

async def send_greetings(message, bot: AsyncTeleBot):
    lang_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_markup.add(*getLangKeys())
    with open('./imgs/start_img.jpg', '+rb') as photo:
        start_photo_path = photo
        await bot.send_photo(message.chat.id, start_photo_path, 
                             reply_to_message_id=message.id, caption = "Choose language:",
                             reply_markup = lang_markup)
        

async def send_help(message, bot: AsyncTeleBot):
    await send_supports(message, bot)

async def send_info(message, bot: AsyncTeleBot):
    await send_natal_chart_description(message, bot)


async def send_price(message, bot: AsyncTeleBot):
    await send_plans(message, bot)