from telebot.types import KeyboardButton, WebAppInfo
from telebot.types import InlineKeyboardButton

def getLangKeys():
    return [
        KeyboardButton('ru 🇷🇺'),
        KeyboardButton('en 🇺🇸'),
        KeyboardButton('es 🇪🇸')]

def getFunctionKeys(lc):
    return [
        KeyboardButton(lc["Natal_chart"]),
        KeyboardButton(lc["PredictionsTaro"]),
        KeyboardButton(lc["Horoscopus"]),
        KeyboardButton(lc["Taro"]),
        KeyboardButton(lc["Color"]),
        KeyboardButton(lc["Number"]),
        KeyboardButton(lc["MainMenu"])
    ]

def getPredictionsTaroButtons(lc):
    return [
        KeyboardButton(lc["OneCardSpread"]),
        KeyboardButton(lc["ThreeCardSpread"]),
        KeyboardButton(lc["MainMenu"])
    ]


def getNatalChartKeysBeforeWebApp(lc, url_profile):
    return [KeyboardButton(lc['Profiles'], web_app = WebAppInfo(url_profile)),
            KeyboardButton(lc['GetNatalChartExample']),
            KeyboardButton(lc["MainMenu"])]

def getNatalChartKeysAfterWebApp(lc, url_profile):
    return [KeyboardButton(lc['Generate']),
            KeyboardButton(lc['ChangeProfile'], web_app = WebAppInfo(url_profile)),
            KeyboardButton(lc['GetNatalChartExample']),
            KeyboardButton(lc["MainMenu"])]

def getStartPageKeyboard(lc):
    return [InlineKeyboardButton(lc["Natal_chart"], callback_data = "natal_chart"),
            InlineKeyboardButton(lc["Plans"], callback_data = "plans")]

def getMenuButtons(lc):
    return [KeyboardButton(lc["Abilities"]),
            KeyboardButton(lc["Settings"]),
            KeyboardButton(lc["Plans"]),
            KeyboardButton(lc["MyOrders"]),
            KeyboardButton(lc["Support"]),
            KeyboardButton(lc["Topics"]),
            KeyboardButton(lc["WhatIsNatalChart"])]

def add_admin_panel(func,lc):
    def wrapper():
        admin_keyboard = func(lc)
        admin_keyboard.append(KeyboardButton(lc["AdminPanel"]))
        return admin_keyboard
    return wrapper()
   
def getSettingsButtonUnSubsribe(lc):
    return [KeyboardButton(lc["ChangeLanguage"]),
            KeyboardButton(lc["UnsubscribeNews"]),
            KeyboardButton(lc["MainMenu"])]

def getSettingsButtonSubsribe(lc):
    return [KeyboardButton(lc["ChangeLanguage"]),
            KeyboardButton(lc["SubscribeNews"]),
            KeyboardButton(lc["MainMenu"])]



def getPlansButtons(lc):
    return [
            [InlineKeyboardButton(lc["StartStart"], callback_data = "plan_starstart"),],
            [InlineKeyboardButton(lc["AstralBloom"], callback_data = "plan_astralbloom"),],
            [InlineKeyboardButton(lc["WayToStars"], callback_data = "plan_waytostars"),]
        ]

def getHoroscopePlans(lc):
    return [KeyboardButton(lc["OneMonthH"]),
            KeyboardButton(lc["ThreeMonthH"]),
            KeyboardButton(lc["OneYearH"]),
            KeyboardButton(lc["MainMenu"])]

def getHoroscopePage(lc):
    return [KeyboardButton(lc["MyHoroscope"]),
            KeyboardButton(lc["ChangeZodiakSign"]),
            KeyboardButton(lc["HoroscopePlans"]),
            KeyboardButton(lc["MainMenu"])]

def getZodiakSings(lc):
    return [KeyboardButton(lc["aries"]),
            KeyboardButton(lc["taurus"]),
            KeyboardButton(lc["gemini"]),
            KeyboardButton(lc["cancer"]),
            KeyboardButton(lc["leo"]),
            KeyboardButton(lc["virgo"]),
            KeyboardButton(lc["libra"]),
            KeyboardButton(lc["scorpio"]),
            KeyboardButton(lc["sagittarius"]),
            KeyboardButton(lc["capricorn"]),
            KeyboardButton(lc["aquarius"]),
            KeyboardButton(lc["pisces"])]

def getAdminPanel(lc):
    return [KeyboardButton(lc["PostMessage"]),
            KeyboardButton(lc["GiftToUser"]),
            KeyboardButton(lc["Report"]),
            KeyboardButton(lc["MainMenu"])]

def getAnswerAdminPanel(lc):
    return [KeyboardButton(lc["yes"]),
            KeyboardButton(lc["no"]),
            KeyboardButton(lc["AdminPanel"]),
            KeyboardButton(lc["MainMenu"])]


def getChoosePaymentType(lc):
    return [KeyboardButton(lc["RUB"]),
            KeyboardButton(lc["CRYPTO"]),
            KeyboardButton(lc["Cancel"])]

def getCryptoCoinType(lc):
    return [KeyboardButton(lc["TON"]),
            KeyboardButton(lc["USDT"]),
            KeyboardButton(lc["BTC"]),
            KeyboardButton(lc["Cancel"]),]

def getCryptoPayKey(lc, pay_url):
    return [InlineKeyboardButton(lc["PAY"], url = pay_url)]

def getProductGift():
    return [InlineKeyboardButton(text = 'Натальная карта', callback_data = "gift natal_chart"),
            InlineKeyboardButton(text = 'Расклад Таро',callback_data = "gift three_taro_gen"),
            InlineKeyboardButton(text = 'Гороскоп на месяц',callback_data = "gift one_month_horoscope"),
            InlineKeyboardButton(text = 'Гороскоп на три месяца',callback_data = "gift three_month_horoscope"),
            InlineKeyboardButton(text = 'Гороскоп на год',callback_data = "gift one_year_horoscope"),
            InlineKeyboardButton(text = 'Пакет звездный старт',callback_data = "gift plan_starstart"),
            InlineKeyboardButton(text = 'Пакет астральный взрыв',callback_data = "gift plan_astralbloom"),
            InlineKeyboardButton(text = 'Пакет путь к звездам',callback_data = "gift plan_waytostars")]
