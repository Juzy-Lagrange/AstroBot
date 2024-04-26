from Bot.bot import *
import datetime

async def clean_taro_limit():
    query = (telegram_user
             .update(taro_limit = 0).execute())