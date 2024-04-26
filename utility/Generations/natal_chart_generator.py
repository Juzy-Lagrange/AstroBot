from Bot.bot import session, astro_clinet, AsyncTeleBot
from utility.GeoPy.GeoModule import GeoModule as GM

def GenerateNatalChart(user_id, lc, bot: AsyncTeleBot):
    profile = session.getProfile(user_id)

    username = profile["name"]
    year, month, day = profile["birth_date"].split("-")
    min,hour = list(map(int,profile["birth_time"].split(":"))) if (profile["birth_time"] != None) else [0,0]

    day = int(day[0:2])
    month = int(month)
    year = int(year)
    print(profile["birth_city"])

    geomod = GM(profile["birth_city"]).GetGeoInfo()
    lang = session.getLang(user_id)
    if lang == 'es':
        lang = 'en'
    res = astro_clinet.GetPDFRequest(
        username=username,
        day=day, 
        month=month, 
        year=year,
        minute=min, 
        hour=hour,
        GEOMODULE=geomod,
        lang=lang
       ) 
    print(res)
    if (res["status"] == True):
        user_pdf_link = res["pdf_url"]
        return user_pdf_link
    else:
        res["pdf_url"]="error"
        print("Wrong Generations: ", res)
        return res