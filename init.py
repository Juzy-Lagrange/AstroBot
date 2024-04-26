from Bot.bot import *
from Handlers import *
from Bot.products_dict import products
from utility import generateLocalRange, zodiak_sings

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from telebot.async_telebot import AsyncTeleBot
from Sheduled_tasks.send_horoscope import send_personal_horoscope, clean_old_horoscope, reset_horoscope_status, send_monthly_horoscope
from Sheduled_tasks.set_taro_limit import clean_taro_limit
from Sheduled_tasks.GetTransaction.get_transaction import check_active_invoices
from Sheduled_tasks.monthly_reports import send_monthly_reports

bot = AsyncTeleBot(BOT_TOKEN, state_storage=StateMemoryStorage())

#Default commands
bot.register_message_handler(greetings, commands=['start'], pass_bot=True)
bot.register_message_handler(send_help, commands=['help'], pass_bot=True)
bot.register_message_handler(send_info, commands=['info'], pass_bot=True)
bot.register_message_handler(send_price, commands=['price'], pass_bot=True)

#Localized_message
    #BaseLogic
#bot.register_message_handler(lambda x,b: print(x), pass_bot=True)
bot.register_message_handler(send_start_page, func = lambda message: message.text in  ["ru 🇷🇺", "en 🇺🇸", "es 🇪🇸"], pass_bot=True)
bot.register_message_handler(send_main_menu,  func = lambda message: message.text in generateLocalRange("MainMenu"), pass_bot=True)
bot.register_message_handler(send_main_menu,  func = lambda message: message.text in generateLocalRange("Cancel"), pass_bot=True)
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
bot.register_message_handler(send_horoscope, func = lambda message: message.text in generateLocalRange("Horoscopus"), pass_bot=True)
bot.register_message_handler(send_my_horoscope, func = lambda message: message.text in generateLocalRange("MyHoroscope"), pass_bot=True)
bot.register_message_handler(change_zodiak_sign, func = lambda message: message.text in generateLocalRange("ChangeZodiakSign"), pass_bot=True)
bot.register_message_handler(set_zodiak_sign, func = lambda message: message.text in zodiak_sings, pass_bot=True)
    #BuyPLan
bot.register_message_handler(buy_one_month_plan, func = lambda message: message.text in generateLocalRange("OneMonthH"), pass_bot=True)
bot.register_message_handler(buy_three_month_plan, func = lambda message: message.text in generateLocalRange("ThreeMonthH"), pass_bot=True)
bot.register_message_handler(buy_one_year_plan, func = lambda message: message.text in generateLocalRange("OneYearH"), pass_bot=True)
bot.register_message_handler(buy_horoscope_plan, func = lambda message: message.text in generateLocalRange("HoroscopePlans"), pass_bot=True)
        #CHOOSE_CURRENCY
bot.register_message_handler(send_rub_invoice, func = lambda message: message.text in generateLocalRange("RUB"), pass_bot=True)
bot.register_message_handler(choose_crypte_currency, func = lambda message: message.text in generateLocalRange("CRYPTO"), pass_bot=True)
bot.register_message_handler(send_crypto_invoice, func = lambda message: message.text in ["USDT","BTC","TON"], pass_bot=True)
bot.register_message_handler(choose_currency, state = MyStates.choose_currency, pass_bot=True)


    #Settings
bot.register_message_handler(change_language, func = lambda message: message.text in generateLocalRange("ChangeLanguage"), pass_bot=True)
bot.register_message_handler(change_subscribe_status, func = lambda message: message.text in generateLocalRange("UnsubscribeNews") or message.text in generateLocalRange("SubscribeNews"), pass_bot=True)
    #Payments
bot.register_message_handler(successful_payment, content_types=['successful_payment'], pass_bot=True)

#PreCheckoutQueryHandler
bot.register_pre_checkout_query_handler(checkout, func=lambda query: True, pass_bot=True)

#Callbacks
bot.register_callback_query_handler(main_menu_callback, func=lambda query: query.data == "mainmenu", pass_bot=True)
bot.register_callback_query_handler(send_natal_chart_menu_callback, func=lambda query: query.data == "natal_chart", pass_bot=True)
bot.register_callback_query_handler(send_plans_callback, func=lambda query: query.data == "plans", pass_bot=True)
bot.register_callback_query_handler(send_pay_invoice, func=lambda query: query.data in list(products['ru'].keys()), pass_bot=True)
bot.register_callback_query_handler(send_gift_to_user, func=lambda query: query.data.startswith('gift'), state=MyStates.send_gift, pass_bot=True)  

#AdminPanel 
bot.register_message_handler(send_admin_panel, func = lambda message: message.text in generateLocalRange("AdminPanel"), pass_bot=True)
bot.register_message_handler(post_message, func = lambda message: message.text in generateLocalRange("PostMessage"), pass_bot=True)
bot.register_message_handler(send_admin_panel, state=MyStates.prepare, func = lambda m: m in generateLocalRange("MainMenu"), pass_bot=True)
bot.register_message_handler(send_report, func = lambda message: message.text in generateLocalRange("Report"), pass_bot=True)


bot.register_message_handler(send_post_message, func = lambda m: (m.chat.id in admin_ids) and (m.text == "Да" or m.text == "Yes"), pass_bot=True)
bot.register_message_handler(unpost_post_message, func = lambda m: m.chat.id in admin_ids and (m.text == "Нет" or m.text == "No"), pass_bot=True)

bot.register_message_handler(get_post_message, state=MyStates.wait_for_message, 
                             func = lambda m: m.chat.id in admin_ids, content_types=['document', 'video', 'audio', 'voice', 'sticker', 'photo', 'text'],
                             pass_bot=True)


bot.register_message_handler(start_gift_process, func = lambda message: message.text in generateLocalRange("GiftToUser"), pass_bot=True)
bot.register_message_handler(get_user_name, state=MyStates.wait_for_user_name, pass_bot=True)


bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.add_custom_filter(ForwardFilter())


async def main_loop():

    scheduler = AsyncIOScheduler() #job_defaults={'max_instances': 2}

    scheduler.add_job(send_monthly_reports, 'cron', month = '*', day='1',     args=[bot])
    scheduler.add_job(send_monthly_horoscope,'cron', week='1-53', hour= '*',  args=[bot])  #second='*/30'
    scheduler.add_job(send_personal_horoscope,'cron', day='*', hour= '*',     args=[bot])  #second='*/7', 
    scheduler.add_job(clean_old_horoscope, 'cron', hour=0, minute=0) 
    scheduler.add_job(clean_taro_limit, 'cron',  hour=0, minute=0)
    scheduler.add_job(check_active_invoices, 'cron', second = '*/3', args=[bot])
    scheduler.add_job(reset_horoscope_status, 'cron', day='*', hour=0, minute=0)
    
    scheduler.start()

    await bot.polling(none_stop=True)

    while True:
        await async_sleep(1000)
    

import asyncio
if __name__ == "__main__":
    asyncio.run(main_loop())