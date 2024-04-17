import requests

class AstrologyAPIClient:
    baseURL = "https://pdf.astrologyapi.com/v1/"

    def __init__(self, uid, key):
        self.userID = uid
        self.apiKey = key

    def getUrl(cls):
        return cls.baseURL

    def getResponse(self, resource, data):
        # print(self.userID)
        url = self.getUrl() + resource
        # print(url)
        resp = requests.post(url, data=data, auth=(self.userID, self.apiKey))
        return resp

    def packageHoroData(self, date, month, year, hour, minute, latitude, longitude, timezone):
        return {
            'day': date,
            'month': month,
            'year': year,
            'hour': hour,
            'min': minute,
            'lat': latitude,
            'lon': longitude,
            'tzone': timezone
        }
    
    def packageDailyHoroData(self,zodiacName,timezone):
        return {
            'zodiacName': zodiacName,
            'timezone': timezone,
        }

    def packageNumeroData(self, date, month, year, name):
        return {
            'day': date,
            'month': month,
            'year': year,
            'name': name
        }

    def packageMatchMakingData(self, maleBirthData, femaleBirthData):
        mData = {
            'm_day': maleBirthData['date'],
            'm_month': maleBirthData['month'],
            'm_year': maleBirthData['year'],
            'm_hour': maleBirthData['hour'],
            'm_min': maleBirthData['minute'],
            'm_lat': maleBirthData['latitude'],
            'm_lon': maleBirthData['longitude'],
            'm_tzone': maleBirthData['timezone']
        }

        fData = {
            'f_day': femaleBirthData['date'],
            'f_month': femaleBirthData['month'],
            'f_year': femaleBirthData['year'],
            'f_hour': femaleBirthData['hour'],
            'f_min': femaleBirthData['minute'],
            'f_lat': femaleBirthData['latitude'],
            'f_lon': femaleBirthData['longitude'],
            'f_tzone': femaleBirthData['timezone']
        }
        tempData = dict(mData.items() + fData.items())
        return tempData

    def call(self, resource, date, month, year, hour, minute, latitude, longitude, timezone):
        data = self.packageHoroData(date, month, year, hour, minute, latitude, longitude, timezone)
        return self.getResponse(resource, data)

    def matchMakingCall(self, resource, maleBirthData, femaleBirthData):
        data = self.packageMatchMakingData(maleBirthData, femaleBirthData)
        return self.getResponse(resource, data)

    def numeroCall(self, resource, date, month, year, name):
        data = self.packageNumeroData(date, month, year, name)
        return self.getResponse(resource, data)

    def dailyHoroCall(self,resource,zodiacName, timezone):
        data = self.packageDailyHoroData(zodiacName,timezone)
        return self.getResponse(resource,data)

    def GetPDFRequest(self, username, day, month, year, hour, minute, GEOMODULE, lang, tzone = 3):
        resource = "natal_horoscope_report/tropical"
        data = {
            "name": username,
            "day": day,
            "month": month,
            "year": year,
            "hour": hour,
            "minute": minute,
            "latitude": round(GEOMODULE.latitude,2),
            "longitude": round(GEOMODULE.longitude,2),
            "place": GEOMODULE.address,
            "language": lang,
            "timezone": tzone,
            "footer_link": "Astro-bot.com",
            "logo_url": "https://images-ext-1.discordapp.net/external/agId5Rh2EQO53UKsnvqH3h-QvcFGwvJChCkKe2TMnTE/%3Fq%3Dtbn%3AANd9GcSMNE0EDjcoDcLAjVSbfENntI7NkqoKNxcXDc45oc4GWg% 26s/https/encrypted-tbn0.gstatic.com/images?format=webp" ,
            "company_name": "Astrolog",
            "company_info": "DATABASE",
            "domain_url": "https://Astro-bot.com",
            "company_email": "example@gmail.com",
            "company_landline": "+77777777777",
            "company_mobile": "+77777777777"
        }
        return {"status": True, "pdf_url": "https://s3.ap-south-1.amazonaws.com/pdfapilambda/f8c7bf80-f762-11ee-ab2f-d33c7f557692.pdf"}
        #return self.getResponse(resource, data).json()

