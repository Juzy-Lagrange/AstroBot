from Bot.bot import *
from utility import GetLocalizationIfUserSession
from DB.init_db_models import GetAvailableProducts, GetAllUserPurchase
from telegram_objects.keyboards import getFunctionKeys, getSettingsButtonUnSubsribe, getSettingsButtonSubsribe, getPlansButtons

async def send_abilities(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    reply_abilities_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_abilities_markup.add(*getFunctionKeys(lc))

    await bot.send_message(user_id, lc["AbilitiesMSG"], parse_mode="HTML", reply_markup = reply_abilities_markup)

async def send_settings(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    user = telegram_user.get(telegram_user.chat_id == user_id)
    
    reply_settings_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if (user.subscribe_status == True):
        reply_settings_markup.add(*getSettingsButtonUnSubsribe(lc))
    else:
        reply_settings_markup.add(*getSettingsButtonSubsribe(lc))

    with open(r'./imgs/settings.jpg', "+rb") as photo:
        await bot.send_photo(user_id, photo = photo, caption = lc["SettingsText"], parse_mode = "HTML", reply_markup = reply_settings_markup)

async def send_plans(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    inline_plans_markup = InlineKeyboardMarkup(getPlansButtons(lc))
    lang = session.getLang(user_id)
    if (lang == 'ru'):
        with open(r'./imgs/PlansRu.jpg', '+rb') as photo:
            await bot.send_photo(user_id, caption = lc["PPlans"], photo = photo, parse_mode = "HTML", reply_markup = inline_plans_markup)
    else:
        with open(r'./imgs/Plans.jpg', '+rb') as photo:
            await bot.send_photo(user_id, caption = lc["PPlans"], photo = photo, parse_mode = "HTML", reply_markup = inline_plans_markup)


async def send_plans_callback(query, bot: AsyncTeleBot):
    user_id = query.message.chat.id
    lc = GetLocalizationIfUserSession(user_id, query.message)

    inline_plans_markup = InlineKeyboardMarkup(getPlansButtons(lc))
    
    if (lang == 'ru'):
        with open(r'./imgs/PlansRu.jpg', '+rb') as photo:
            await bot.send_photo(user_id, caption = lc["PPlans"], photo = photo, parse_mode = "HTML", reply_markup = inline_plans_markup)
    else:
        with open(r'./imgs/Plans.jpg', '+rb') as photo:
            await bot.send_photo(user_id, caption = lc["PPlans"], photo = photo, parse_mode = "HTML", reply_markup = inline_plans_markup)



async def send_user_orders(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    print(user_id)

    result_text = " "
    user_stats = GetAvailableProducts(user_id)[0]
    

    result_text += lc["query_available_products"].format(
        user_stats["horoscope_active_date"] if user_stats["horoscope_active_date"] != None else lc["no_horoscope"],
        user_stats["unlimited_taro"],
        user_stats["taro_count"],
        user_stats["natal_chart_count"],
    )
    result_text += '\n\n'
    purchases_query = GetAllUserPurchase(user_id)

    if (purchases_query[0]['creation_date'] == None):
        await bot.send_message(user_id, result_text + lc["no_purchases"])
        return None

    for invoice in purchases_query:
        result_text += lc["query_all_user_purchase"].format(
            invoice["creation_date"],
            lc[invoice["name"]],
            invoice["amount"],
            invoice["currency"])
        result_text += '\n\n'

    result_text = result_text.split('\n\n')

    msg_to_user = ''
    for i in result_text:
        msg_to_user += i
        msg_to_user += '\n\n'
        if (len(msg_to_user) > 2056):
            await bot.send_message(user_id, msg_to_user)
            msg_to_user = ''
    
    if (len(msg_to_user) > 0):
        await bot.send_message(user_id, msg_to_user)


async def send_supports(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.send_message(user_id, lc["SupportMessage"], parse_mode='MarkdownV2')


async def send_topics(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.send_message(user_id, lc["TopicsMessage"], parse_mode='MarkdownV2')


async def send_natal_chart_description(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    await bot.send_message(user_id, lc["WhatIsNatalChartMessage"], parse_mode='HTML')
