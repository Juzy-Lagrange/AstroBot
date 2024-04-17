from Bot.bot import *
from utility import GetLocalizationIfUserSession, tryGenURLProfile
from utility.pdf_examples .chart_examples import examples
from telegram_objects.keyboards import getNatalChartKeysBeforeWebApp, getNatalChartKeysAfterWebApp
from utility import GeoModule as GM

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

    await bot.send_message(
        webAppMes.chat.id, 
        msg_txt.format(
            profile["name"],
            profile["birth_date"],
            profile["birth_time"],
            geomod.address
        ),
        reply_markup = befor_gen_markup 
    )

async def send_example_chart(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    
    url_profile = tryGenURLProfile(user_id)
    web_app_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_markup.add(*getNatalChartKeysBeforeWebApp(lc,url_profile))
    await bot.send_message(message.chat.id, examples['ru'], reply_markup = web_app_markup)


async def generate_natal_chart(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    
    await bot.send_message(user_id,lc["GetNatalChartData"])
    
    invoice_data = ProductFabricMethod.getProduct("natal_chart",session.getLang(user_id), 300).getProductParameters()
    await bot.send_invoice(user_id, **invoice_data)