from Bot.bot import *
from Handlers.PaymentsHandlers.SendProductsresult.plans import *
from utility.Generations.horoscope import *
import datetime

def GetLocalizationIfUserSession(user_id, message):
    if (session.userInPool(user_id)):
        lc = getUserLocalization(user_id, session.getLang(user_id))
    else:
        lc = getUserLocalization(user_id)
        values = dataMessage(message, lc['lang'])
        session.addUserFromMessage(values)
    return lc


with open('./localization/local.json', encoding="utf-8") as localization:
    content = localization.read()
    localization = json.loads(content)
    globals().update(localization)


def getUserLocalization(chat_id, input_lang=None, default_lang='ru'):
    lang = (telegram_user.get_or_none(telegram_user.chat_id == chat_id)).lang
    if (lang == None):
        lang = input_lang[0:1] if (input_lang != None) else default_lang
        return ChooseLang(lang)
    else:
        return ChooseLang(lang)


def generateLocalRange(phrase):
    return [localization['language'][i][phrase] for i in ["ru","en","es"]]


def tryGenURLProfile(user_id):
    WEB_APP_URL = getenv("WEB_APP_URL")
    return WEB_APP_URL + f"/profile/select/{user_id}" #/#AUTH_TOKEN


def ChooseLang (local = 'ru'):
    return localization['language'][local]


zodiak_sings = [ChooseLang(i)[j] for i in ["ru","en","es"] for j 
                in ["aries","taurus","gemini",
                    "cancer","leo","virgo",
                    "libra", "scorpio", "sagittarius",
                    "capricorn", "aquarius", "pisces"]]

async def send_gift_db_user(user, product_name):
    if (product_name=='natal_chart'):
        user.natal_chart_count += 1
        user.save()

    elif (product_name=='three_taro_gen'):
        user.taro_count += 3
        user.save()

    elif (product_name=='one_month_horoscope'):
        if user.horoscope_active_date == None:
            user.horoscope_active_date = datetime.datetime.today() + datetime.timedelta(days=31)
            user.save()
        else:
            user.horoscope_active_date += datetime.timedelta(days=31)
            user.save()

    elif (product_name=='three_month_horoscope'):
        if user.horoscope_active_date == None:
            user.horoscope_active_date = datetime.datetime.today() + datetime.timedelta(days=31*3)
            user.save()
        else:
            user.horoscope_active_date += datetime.timedelta(days=31*3)
            user.save()

    elif (product_name=='one_year_horoscope'):
        if user.horoscope_active_date == None:
            user.horoscope_active_date = datetime.datetime.today() + datetime.timedelta(days=31*12)
            user.save()
        else:
            user.horoscope_active_date += datetime.timedelta(days=31*12)
            user.save()

    elif (product_name=='plan_starstart'):
        buy_stars_start(user.chat_id)

    elif (product_name=='plan_astralbloom'):
        buy_astral_bloom(user.chat_id)

    elif (product_name=='plan_waytostars'):
        buy_waytostars_package(user.chat_id)
    
    