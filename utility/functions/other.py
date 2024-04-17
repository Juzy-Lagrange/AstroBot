from Bot.bot import *

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

def getUserLocalization(chat_id, input_lang=None, default_lang='ru'):
    lang = (Models['telegram_user'].get_or_none(Models['telegram_user'].chat_id == chat_id)).lang
    if (lang == None):
        lang = input_lang if (input_lang != None) else default_lang
        return ChooseLang(lang)
    else:
        return ChooseLang(lang)

def generateLocalRange(phrase):
    return [localization['language'][i][phrase] for i in ["ru","en","trk"]]

def tryGenURLProfile(user_id):
    WEB_APP_URL = getenv("WEB_APP_URL")
    return WEB_APP_URL + f"/profile/select/{user_id}"

def ChooseLang (local = 'ru'):
    return localization['language'][local]