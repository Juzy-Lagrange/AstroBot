import json
import sdk
import requests

client = sdk.AstrologyAPIClient("628901", "bc5870530c8a93a476a4824db9dbb145")

# Daily Horoscope APIs need to be called
resource = "natal_horoscope_report/tropical"

data = {
    "name": "Никита",
    "day": 8,
    "month": 9,
    "year": 2005,
    "hour": 12,
    "min": 21,
    "lat": 63.12,
    "lon": 75.27,
    "place": "Noyabrsk, Russia",
    "language": "ru",
    "tzone": 3,
    "footer_link": "Astro-bot.com",
    "logo_url": "https://images-ext-1.discordapp.net/external/agId5Rh2EQO53UKsnvqH3h-QvcFGwvJChCkKe2TMnTE/%3Fq%3Dtbn%3AANd9GcSMNE0EDjcoDcLAjVSbfENntI7NkqoKNxcXDc45oc4GWg%26s/https/encrypted-tbn0.gstatic.com/images?format=webp",
    "company_name": "Astrolog",
    "company_info": "DATABASE",
    "domain_url": "https://Astro-bot.com",
    "company_email": "example@gmail.com",
    "company_landline": "+77777777777",
    "company_mobile": "+77777777777"
}



result = client.getResponse(resource, data)

print(result.json())
