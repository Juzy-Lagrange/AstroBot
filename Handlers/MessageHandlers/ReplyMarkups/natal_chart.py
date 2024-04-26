from Bot.bot import *
from utility import GetLocalizationIfUserSession, tryGenURLProfile, GenerateNatalChart
from utility.pdf_examples .chart_examples import examples
from DB.init_db_models import GetAvailableProducts
from telegram_objects.keyboards import getNatalChartKeysBeforeWebApp, getNatalChartKeysAfterWebApp 
from utility import GeoModule as GM
from asyncio import sleep as async_sleep
import datetime

from Handlers.Choose_currency.choose_currency import choose_currency

async def natal_chart_gen(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    url_profile = tryGenURLProfile(user_id)

    web_app_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_markup.add(*getNatalChartKeysBeforeWebApp(lc,url_profile))
    await bot.send_message(message.chat.id, lc["ChooseProfile"], reply_markup = web_app_markup)


async def get_webapp_data(webAppMes, bot: AsyncTeleBot):
    user_id = webAppMes.chat.id
    lc = GetLocalizationIfUserSession(user_id, webAppMes)

    json_data = json.loads(webAppMes.web_app_data.data)
    await bot.send_message(webAppMes.chat.id, lc["GetData"])

    session.trySetProfile(
        id=int(json_data["data"]["tgId"]),
        name=json_data["data"]["name"],
        male=json_data["data"]["sex"],
        birth_date=json_data["data"]["birthDate"],
        birth_time=json_data["data"]["birthTime"],
        birth_city=json_data["data"]["birthCity"])

    profile = session.getProfile(user_id)
    geomod = GM(profile["birth_city"]).GetGeoInfo()
    msg_txt = lc["ProfileData"]

    befor_gen_markup = ReplyKeyboardMarkup(resize_keyboard=True)

    url_profile = tryGenURLProfile(user_id)
    befor_gen_markup.add(*getNatalChartKeysAfterWebApp(lc, url_profile))

    address = ''
    if (geomod != None):
        address = geomod.address
    else:
        address = profile["birth_city"]
    

    await bot.send_message(
        webAppMes.chat.id, 
        msg_txt.format(
            profile["name"],
            profile["birth_date"],
            profile["birth_time"],
            address        
        ),
        reply_markup = befor_gen_markup 
    )

async def send_example_chart(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    
    url_profile = tryGenURLProfile(user_id)
    web_app_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_markup.add(*getNatalChartKeysBeforeWebApp(lc,url_profile))
    lang = session.getLang(user_id) if session.getLang(user_id) != 'es' else 'en'
    await bot.send_message(message.chat.id,f"[{lc['GetNatalChartExample']}]({examples[lang]})", parse_mode = "MarkdownV2", reply_markup = web_app_markup)


async def generate_natal_chart(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    if (session.getProfile(user_id) == {}):
        url_profile = tryGenURLProfile(user_id)
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.add(*getNatalChartKeysBeforeWebApp(lc,url_profile))
        await bot.send_message(user_id, lc["ProfileIsNotDefined"],reply_markup=reply_markup)
        return None

    await bot.send_message(user_id,lc["GetNatalChartData"])

    user = telegram_user.get(telegram_user.chat_id == str(user_id))

    if (user.natal_chart_count == 0):
        await bot.send_message(user_id, lc['NoNatalChartGenerations'])

        await bot.set_state(message.from_user.id, MyStates.choose_currency, message.chat.id)
        async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["product_name"] = "natal_chart"
        await choose_currency(message, bot)

    else:
        user.natal_chart_count -= 1
        user.save()
          
        user_pdf_link = GenerateNatalChart(user_id, lc, bot)
        await async_sleep(1.3)
        print(user_pdf_link)
        await bot.send_message(user_id,f"[{lc['SuccesfulyGenerated']}]({user_pdf_link})", parse_mode='MarkdownV2')