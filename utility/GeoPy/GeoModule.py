import json
from geopy.geocoders import Nominatim

class GeoModule:
    def __init__(self,city):
        self.city = city
        self.engine = Nominatim(user_agent="astro-bot")

    def GetGeoInfo(self):
        return self.engine.geocode(self.city)