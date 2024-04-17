from Bot.bot import *
from Bot.products_dict import costs
from utility import GetLocalizationIfUserSession
from utility.pdf_examples.chart_examples import examples
from telegram_objects.keyboards import getStartPageKeyboard, getMenuButtons


async def main_menu_callback(query, bot: AsyncTeleBot):
    user_id = query.from_user.id
    message = query.message
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
    reply_menu_markup.add(*getMenuButtons(lc))
    await bot.send_message(user_id, lc["MainMenu"], reply_markup = reply_menu_markup)


async def send_pay_invoice(query, bot: AsyncTeleBot):
    user_id = query.from_user.id
    lc = GetLocalizationIfUserSession(user_id, query.message)

    data = query.data 
    product = ProductFabricMethod.getProduct(data, session.getLang(user_id),costs[data])
    await bot.send_invoice(user_id, **product.getProductParameters())