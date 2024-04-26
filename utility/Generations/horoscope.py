from Bot.bot import *
from telegram_objects.keyboards import getHoroscopePage
import datetime

days = 31

async def add_one_month(user_id, lc, bot: AsyncTeleBot):
    user = telegram_user.get(telegram_user.chat_id == str(user_id))
    if (user.horoscope_active_date == None):
        user.horoscope_active_date = datetime.date.today() + datetime.timedelta(days * 1)
    else:
         user.horoscope_active_date += datetime.timedelta(days * 1)
    user.save()

async def add_three_month(user_id, lc, bot: AsyncTeleBot):
    user = telegram_user.get(telegram_user.chat_id == str(user_id))
    if (user.horoscope_active_date == None):
        user.horoscope_active_date = datetime.date.today() + datetime.timedelta(days * 3)
    else:
        user.horoscope_active_date += datetime.timedelta(days * 3)
    user.save()

async def add_one_year(user_id, lc, bot: AsyncTeleBot):
    user = telegram_user.get(telegram_user.chat_id == str(user_id))
    if (user.horoscope_active_date == None):
        user.horoscope_active_date = datetime.date.today() + datetime.timedelta(days * 12)
    else:
        user.horoscope_active_date += datetime.timedelta(days * 12)
    user.save()