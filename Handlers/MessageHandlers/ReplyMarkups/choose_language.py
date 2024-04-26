from Bot.bot import *
from telegram_objects.keyboards import getFunctionKeys
from utility import getUserLocalization

async def choose_language(message):
    user_id = message.chat.id
    
    values = {
        'username': message.chat.username,
        'chat_id': message.chat.id,
        'lang': message.text[0:2]
    }

    telegram_user.insert(values).on_conflict(
        update={telegram_user.lang: values["lang"]}
    ).execute()
    
    lc = getUserLocalization(user_id, values["lang"])
    data = dataMessage(message, lc['lang'])
    session.addUserFromMessage(data)
    session.setLang(user_id, values['lang'])