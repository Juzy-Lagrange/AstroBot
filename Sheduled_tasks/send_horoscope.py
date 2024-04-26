from Bot.bot import *
from utility.horoscope.generate_horoscope import generate_horoscope, generate_monthly_horoscope
import datetime


def format(text):
    text = text.replace('#','')
    text = text.replace('.','\.')
    text = text.replace('*','')
    text = text.replace('_','')
    text = text.replace('`','')
    text = text.replace('@','')
    text = text.replace('-','')
    text = text.replace('(','\(')
    text = text.replace(')','\)')
    text = text.replace(']','\]')
    text = text.replace('[','\[')
    text = text.replace('!','\\!')
    text = text.replace('|','')
    return text

async def send_personal_horoscope(bot: AsyncTeleBot):

    get_user_for_sending_horoscope = (telegram_user
                .select()
                .where((telegram_user.horoscope_active_date >= datetime.date.today()) & 
                       (telegram_user.horoscope_active_date != None) & 
                       (telegram_user.got_horoscope == 0)).execute())


    for user in get_user_for_sending_horoscope:
        print(f"send_horoscope to: username: {user.username} id: {user.chat_id}")
        try:
            horoscope_text = await generate_horoscope(date = datetime.date.today(), username = user.username, zodiak_sign = user.zodiak_sign, lang=user.lang)
            horoscope_text = format(horoscope_text)
            try:
                await bot.send_message(user.chat_id, text = horoscope_text, parse_mode="MarkdownV2")
                user.got_horoscope = 1
                user.save()
            except Exception as e:
                print(e)

        except Exception as e:
            print(f"Horoscope Generation Exception:\n{e}")

async def clean_old_horoscope():
    query = (telegram_user
             .update(horoscope_active_date = None)
             .where(telegram_user.horoscope_active_date < datetime.date.today()).execute())
             
async def reset_horoscope_status():
    upd_got_horoscope_status = (telegram_user
                                    .update(got_horoscope=0, monthly_horoscope=False)
                                    .where(telegram_user.got_horoscope == 1).execute())
    

async def send_monthly_horoscope(bot: AsyncTeleBot):

    get_user_for_sending_horoscope = (telegram_user
                .select()
                .where((telegram_user.subscribe_status == True) & 
                       (telegram_user.monthly_horoscope == False)).execute())
    
    horoscope_text_ru = ""
    horoscope_text_en = ""
    horoscope_text_es = ""

    horoscope_text_ru = await generate_monthly_horoscope(date = datetime.date.today(),lang="ru")    
    
    horoscope_text_en = await generate_monthly_horoscope(date = datetime.date.today(),lang="en")
    
    horoscope_text_es = await generate_monthly_horoscope(date = datetime.date.today(),lang="es")


    for user in get_user_for_sending_horoscope:
        try:
            if (user.lang == 'ru'):
                await bot.send_message(user.chat_id, horoscope_text_ru)
            elif (user.lang == 'en'):
                await bot.send_message(user.chat_id, horoscope_text_en)
            else:
                await bot.send_message(user.chat_id, horoscope_text_es)
            
            user.monthly_horoscope = True
            user.save()

        except Exception as e:
            print(f"[ERROR] sending mounthly horoscope: {e}")