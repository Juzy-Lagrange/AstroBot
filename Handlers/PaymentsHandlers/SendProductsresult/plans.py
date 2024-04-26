from Bot.bot import Models
import datetime

days = 30
horoscope_mounth = {
    "waytostars": 6,
    "astralbloom":3,
    "starsstart": 1,
}

def buy_waytostars_package(user_id):    
    target_user = Models['telegram_user'].get(Models['telegram_user'].chat_id == user_id)
    new_taro_count = 30
    new_natal_chart_count = target_user.natal_chart_count + 3
    if target_user.horoscope_active_date != None:
        new_date = target_user.horoscope_active_date + datetime.timedelta(days * horoscope_mounth["waytostars"])
    else:
        new_date = datetime.date.today() + datetime.timedelta(days * horoscope_mounth["waytostars"])
    
    updated_fields = {
        "horoscope_active_date": new_date,
        "taro_count": new_taro_count,
        "unlimited_taro": 1,
        "natal_chart_count": new_natal_chart_count
    }
    target_user.update(updated_fields).where(Models['telegram_user'].chat_id == user_id).execute()


def buy_astral_bloom(user_id):
    target_user = Models['telegram_user'].get(Models['telegram_user'].chat_id == user_id)
    new_taro_count = target_user.taro_count + 10
    new_natal_chart_count = target_user.natal_chart_count + 1
    if target_user.horoscope_active_date != None:
        new_date = target_user.horoscope_active_date + datetime.timedelta(days * horoscope_mounth["astralbloom"])
    else:
        new_date = datetime.date.today() + datetime.timedelta(days * horoscope_mounth["astralbloom"])
    
    updated_fields = {
        "horoscope_active_date": new_date,
        "taro_count": new_taro_count,
        "natal_chart_count": new_natal_chart_count
    }
    target_user.update(updated_fields).where(Models['telegram_user'].chat_id == user_id).execute()


def buy_stars_start(user_id):
    target_user = Models['telegram_user'].get(Models['telegram_user'].chat_id == user_id)
    new_taro_count = target_user.taro_count + 10
    new_natal_chart_count = target_user.natal_chart_count + 1
    if target_user.horoscope_active_date != None:
        new_date = target_user.horoscope_active_date + datetime.timedelta(days * horoscope_mounth["starsstart"])
    else:
        new_date = datetime.date.today() + datetime.timedelta(days * horoscope_mounth["starsstart"])
    
    updated_fields = {
        "horoscope_active_date": new_date,
        "taro_count": new_taro_count,
        "natal_chart_count": new_natal_chart_count
    }
    target_user.update(updated_fields).where(Models['telegram_user'].chat_id == user_id).execute()