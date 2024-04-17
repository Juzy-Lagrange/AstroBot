from Bot.bot import *
from utility import GetLocalizationIfUserSession

async def horoscope(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.send_message(message.chat.id, "coming soon... (Horoscopus)")