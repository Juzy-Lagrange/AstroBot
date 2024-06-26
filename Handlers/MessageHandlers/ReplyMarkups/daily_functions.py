import random

from Bot.bot import *
from utility import GetLocalizationIfUserSession
from taro_bot.infobase import card_desc, way, colors_array

async def day_arcane(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    if not (session.getFarcane(user_id)):
        session.setFArcane(user_id)
        temp_daycard = random.randint(0, 21)
        await bot.send_message(user_id, lc["YourDayArcane"] + str(temp_daycard))
        await bot.send_message(user_id, lc["YourDayArcaneDescription"],)
        img = open(way + str(temp_daycard) + '.jpeg', 'rb')
        await bot.send_photo(user_id, img, caption=card_desc[session.getLang(user_id)][temp_daycard])
    else:
        await bot.send_message(user_id, lc["OneTimeOnADayArcane"])


async def day_color(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    if not (session.getFColor(user_id)):
        session.setFColor(user_id)
        await bot.send_message(user_id, lc["DayDesicion"] + lc[str(random.choice(['yes','no']))] )
    else:
        await bot.send_message(user_id, lc["OneTimeDayDesicion"])


async def day_number(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    if not (session.getFNum(user_id)):
        session.setFNum(user_id)
        temp_daynum = random.randint(1, 77)
        await bot.send_message(message.chat.id, lc["YourDayNumber"] + str(temp_daynum))
    else:
        await bot.send_message(user_id, lc["OneTimeDayNumber"])