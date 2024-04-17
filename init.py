from Bot.bot import *
from Handlers import *
from Bot.products_dict import products
from utility import generateLocalRange

from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot(BOT_TOKEN)

#Default commands
bot.register_message_handler(greetings, commands=['start','help'], pass_bot=True)

#Localized_message
    #BaseLogic
bot.register_message_handler(send_start_page, func = lambda message: message.text in  ["ru","en","trk"], pass_bot=True)
bot.register_message_handler(send_main_menu,  func = lambda message: message.text in generateLocalRange("MainMenu"), pass_bot=True)
    #NatalChartLogic
bot.register_message_handler(natal_chart_gen, func = lambda message: message.text in generateLocalRange("Natal_chart"), pass_bot=True)
bot.register_message_handler(get_webapp_data, content_types="web_app_data", pass_bot=True)
bot.register_message_handler(send_example_chart, func = lambda message: message.text in generateLocalRange("GetNatalChartExample"), pass_bot=True)
bot.register_message_handler(generate_natal_chart, func = lambda message: message.text in generateLocalRange("Generate"), pass_bot=True)
    #TaroLogic
bot.register_message_handler(send_one_card_taro_spread, func = lambda message: message.text in generateLocalRange("OneCardSpread"), pass_bot=True)
bot.register_message_handler(send_three_card_taro_spread, func = lambda message: message.text in generateLocalRange("ThreeCardSpread"), pass_bot=True)
bot.register_message_handler(taro_predictions, func = lambda message: message.text in generateLocalRange("PredictionsTaro"), pass_bot=True)
    #DailyLogic
bot.register_message_handler(day_arcane, func = lambda message: message.text in generateLocalRange("Taro"), pass_bot=True)
bot.register_message_handler(day_color, func = lambda message: message.text in generateLocalRange("Color"), pass_bot=True)
bot.register_message_handler(day_number, func = lambda message: message.text in generateLocalRange("Number"), pass_bot=True)
    #General
bot.register_message_handler(send_abilities, func = lambda message: message.text in generateLocalRange("Abilities"), pass_bot=True)
bot.register_message_handler(send_settings, func = lambda message: message.text in generateLocalRange("Settings"), pass_bot=True)
bot.register_message_handler(send_plans, func = lambda message: message.text in generateLocalRange("Plans"), pass_bot=True)
bot.register_message_handler(send_user_orders, func = lambda message: message.text in generateLocalRange("MyOrders"), pass_bot=True)
bot.register_message_handler(send_supports, func = lambda message: message.text in generateLocalRange("Support"), pass_bot=True)
bot.register_message_handler(send_topics, func = lambda message: message.text in generateLocalRange("Topics"), pass_bot=True)
bot.register_message_handler(send_natal_chart_description, func = lambda message: message.text in generateLocalRange("WhatIsNatalChart"), pass_bot=True)

    #Horoscop
bot.register_message_handler(horoscope, func = lambda message: message.text in generateLocalRange("Horoscopus"), pass_bot=True)

    #Payments
bot.register_message_handler(successful_payment, content_types=['successful_payment'], pass_bot=True)

#PreCheckoutQueryHandler
bot.register_pre_checkout_query_handler(checkout, func=lambda query: True, pass_bot=True)

#Callbacks
bot.register_callback_query_handler(main_menu_callback, func=lambda query: query.data == "mainmenu", pass_bot=True) 
bot.register_callback_query_handler(send_pay_invoice, func=lambda query: query.data in list(products['ru'].keys()), pass_bot=True)    

import asyncio
if __name__ == "__main__":
    asyncio.run(bot.polling())