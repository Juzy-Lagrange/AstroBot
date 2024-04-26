from Bot.bot import *
from utility import GetLocalizationIfUserSession
from utility import generate_one_card, generate_three_cards
from telegram_objects.keyboards import getPredictionsTaroButtons
from Handlers.Choose_currency.choose_currency import choose_currency
from Bot.products_dict import costs


async def taro_predictions(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    taro_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    taro_markup.add(*getPredictionsTaroButtons(lc))
    await bot.send_message(message.chat.id,lc["TaroChooseFunc"],reply_markup = taro_markup)


async def send_one_card_taro_spread(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    
    user = telegram_user.get(telegram_user.chat_id == str(user_id))

    if (user.unlimited_taro):
        if (user.taro_limit < 30):
            await generate_one_card(user_id, lc, bot)
            user.taro_limit += 1
            user.save()
        else:
            await bot.send_message(user_id, lc["Limit30Cards"])
    else:
        if (user.taro_count > 0):
            await generate_one_card(user_id, lc, bot)
            user.taro_count -= 1
            user.taro_limit += 1
            user.save()
            
        else:
            await bot.send_message(user_id, lc["NoTaroGenerations"])

            await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
            async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data["product_name"] = "one_taro_gen"

            await choose_currency(message, bot)
            # invoice_parameters = ProductFabricMethod.getProduct("one_taro_gen", session.getLang(user_id), costs["RUB"]["one_taro_gen"]).getProductParameters()
            # await bot.send_invoice(user_id, **invoice_parameters)
            

async def send_three_card_taro_spread(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    user = telegram_user.get(telegram_user.chat_id == str(user_id))

    if (user.unlimited_taro):
        if (user.taro_limit < 30):
            await generate_three_cards(user_id, lc, bot)
            user.taro_limit += 3
            user.save()
        else:
            await bot.send_message(user_id, lc["Limit30Cards"])
    else:
        if (user.taro_count > 2):
            await generate_three_cards(user_id, lc, bot)
            user.taro_count -= 3
            user.taro_limit += 3
            user.save()
            
        else:
            await bot.send_message(user_id, lc["NoTaroGenerations"])
            #print(costs["RUB"]["three_taro_gen"])
            
            
            await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
            async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data["product_name"] = "three_taro_gen"

            await choose_currency(message, bot)

            # invoice_parameters = ProductFabricMethod.getProduct("three_taro_gen", session.getLang(user_id), costs["RUB"]["three_taro_gen"]).getProductParameters()
            # await bot.send_invoice(user_id, **invoice_parameters)