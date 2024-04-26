from Bot.bot import *
from Bot.products_dict import costs
from utility import GetLocalizationIfUserSession
from utility.functions.other import send_gift_db_user
from utility.pdf_examples.chart_examples import examples
from telegram_objects.keyboards import getStartPageKeyboard, getMenuButtons, getAdminPanel
from Handlers.Choose_currency.choose_currency import choose_currency
from Handlers.MessageHandlers.ReplyMarkups.general import send_natal_chart_description
from Handlers.MessageHandlers.ReplyMarkups.natal_chart import natal_chart_gen

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
    
    product_name = query.data

    await bot.set_state(query.from_user.id, MyStates.choose_currency, query.message.chat.id)
    async with bot.retrieve_data(query.from_user.id, query.message.chat.id) as data:
        data["product_name"] = product_name

    await choose_currency(query.message, bot)

    # product = ProductFabricMethod.getProduct(data, session.getLang(user_id), costs["RUB"][data])
    # await bot.send_invoice(user_id, **product.getProductParameters())

async def send_gift_to_user(query, bot: AsyncTeleBot):
    user_id = query.from_user.id
    lc = GetLocalizationIfUserSession(user_id, query.message)

    product_name = query.data.split()[1]

    async with bot.retrieve_data(query.from_user.id, query.message.chat.id) as data:
        user = telegram_user.get(telegram_user.username == data["username"])

        reply_admin_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
        reply_admin_menu_markup.add(*getAdminPanel(lc))

        if user != None:
            await send_gift_db_user(user, product_name)
            await bot.send_message(user.chat_id, f"Вам выдана услуга {lc[product_name]}")
            await bot.send_message(user_id, f"Пользователю @{data['username']} выдана услуга {lc[product_name]}\n#ВыданаУслуга", reply_markup = reply_admin_menu_markup)
        else:
            await bot.send_message(user_id, f"Пользователь @{data['username']} не является пользователем бота", reply_markup = reply_admin_menu_markup)

        await bot.delete_state(query.message.from_user.id, query.message.chat.id)


async def send_natal_chart_menu_callback(query, bot: AsyncTeleBot):
    user_id = query.from_user.id
    lc = GetLocalizationIfUserSession(user_id, query.message)

    await natal_chart_gen(query.message, bot) 
