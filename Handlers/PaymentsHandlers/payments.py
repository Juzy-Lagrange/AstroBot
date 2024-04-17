from Bot.bot import *
import datetime
from utility import GetLocalizationIfUserSession, tryGenURLProfile
from utility import GeoModule as GM


async def successful_payment(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    payment_info = message.successful_payment

    

    #natal_chart product id
    purchase = {
         'chat_id': user_id,
         'product_type': 2,  
         'date': datetime.date.today().__str__(),
         'sum': payment_info.total_amount,
    }

    print(purchase)

    Models['purchases'].insert(purchase).execute()


    if payment_info.invoice_payload == "NatalChartGeneration":
        profile = session.getProfile(user_id)
        username = profile["name"]
        year, month, day = profile["birth_date"].split("-")
        min,hour = list(map(int,profile["birth_time"].split(":"))) if (profile["birth_time"] != None) else [0,0]

        day = int(day[0:2])
        month = int(month)
        year = int(year)
        print(profile["birth_city"])

        geomod = GM(profile["birth_city"]).GetGeoInfo()
        res = astro_clinet.GetPDFRequest(
            username,
            day, month, year,
            min, hour,
            geomod,
            session.getLang(user_id))

        if (res["status"] == True):
            user_pdf_link = res["pdf_url"]
            await bot.send_message(user_id,f"[{lc['SuccesfulyGenerated']}]({user_pdf_link})", parse_mode='MarkdownV2')
        else:
            print("Wrong: ", res)