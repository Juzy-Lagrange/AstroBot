from Bot.bot import *
from utility import GetLocalizationIfUserSession
from utility.pdf_examples.chart_examples import examples
from telegram_objects.keyboards import getStartPageKeyboard, getMenuButtons


async def send_start_page(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    inline_start_markup = InlineKeyboardMarkup()
    inline_start_markup.add(*getStartPageKeyboard(lc))
    txt = lc["Greetings"].format(examples[session.getLang(user_id)])
    await bot.send_message(message.chat.id, txt, parse_mode='MarkdownV2', reply_markup = inline_start_markup)

    await send_main_menu(message, bot)


async def send_main_menu(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
    reply_menu_markup.add(*getMenuButtons(lc))

    txt = lc["MainMenu"]
    await bot.send_message(message.chat.id, txt, parse_mode='MarkdownV2', reply_markup = reply_menu_markup)