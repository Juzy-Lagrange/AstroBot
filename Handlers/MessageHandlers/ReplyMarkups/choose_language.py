from Bot.bot import *
from telegram_objects.keyboards import getFunctionKeys
from utility import getUserLocalization

async def choose_language(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    values = {
        'username': message.chat.username,
        'chat_id': message.chat.id,
        'lang': message.text
    }

    Models['telegram_user'].insert(values).on_conflict(
        update={Models['telegram_user'].lang: values["lang"]}
    ).execute()

    lc = getUserLocalization(user_id,values["lang"])
    data = dataMessage(message, lc['lang'])
    session.addUserFromMessage(data)

    function_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    function_markup.add(*getFunctionKeys(lc))
    await bot.send_message(message.chat.id, lc["Greetings"], reply_markup = function_markup)