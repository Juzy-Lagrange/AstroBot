from Bot.bot import *
from utility import GetLocalizationIfUserSession
from utility.pdf_examples.chart_examples import examples
from Handlers.MessageHandlers.ReplyMarkups.choose_language import choose_language
from telegram_objects.keyboards import getStartPageKeyboard, getMenuButtons, add_admin_panel


async def send_start_page(message, bot: AsyncTeleBot):
    await choose_language(message)
    #print(message.text[0:1])
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    inline_start_markup = InlineKeyboardMarkup()
    inline_start_markup.add(*getStartPageKeyboard(lc))

    await bot.delete_state(message.from_user.id, message.chat.id)
    txt = lc["Greetings"]   #.format(examples['ru']) #CHANGE session.getLand(user_id)
    with open(r"imgs\baba_gadalka.jpg","+rb") as photo:
        await bot.send_photo(message.chat.id, caption = txt, photo = photo, parse_mode='HTML', reply_markup = inline_start_markup)
    await send_main_menu(message, bot)

async def send_main_menu(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)

    if user_id in admin_ids:
        reply_menu_markup.add(*add_admin_panel(getMenuButtons, lc))
    else:
        reply_menu_markup.add(*getMenuButtons(lc))
    
    await bot.delete_state(message.from_user.id, message.chat.id)

    txt = lc["MainMenu"]
    await bot.send_message(message.chat.id, txt, parse_mode='MarkdownV2', reply_markup = reply_menu_markup)