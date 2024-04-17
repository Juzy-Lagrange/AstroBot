from telebot.types import KeyboardButton, WebAppInfo
from telebot.types import InlineKeyboardButton

def getLangKeys():
    return [
        KeyboardButton("ru"),
        KeyboardButton("en"),
        KeyboardButton("trk")
    ]

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
            KeyboardButton(lc["WhatIsNatalChart"])]\
            
def getSettingsButton(lc):
    return [KeyboardButton(lc["ChangeLanguage"]),
            KeyboardButton(lc["UnsubscribeNews"])]

def getPlansButtons(lc):
    return [InlineKeyboardButton(lc["StartStart"], callback_data = "plan_starstart"),
            InlineKeyboardButton(lc["AstralBloom"], callback_data = "plan_astralbloom"),
            InlineKeyboardButton(lc["WayToStars"], callback_data = "plan_waytostars")]