from Bot.products_dict import products
from telebot.types import LabeledPrice


from os import getenv
from dotenv import load_dotenv

load_dotenv()
PROVIDER_TOKEN_TEST = getenv("PROVIDER_TOKEN_TEST")


class Product:
    def __init__ (self, title, description, invoice_payload):
        self.__CONST_CONVERT_TO_RUB = 100
        self.title = title
        self.description = description
        self.invoice_payload = invoice_payload
        self.provider_token = PROVIDER_TOKEN_TEST
        self.currency = "rub"
    
    def getProductParameters(self):
        parameters =  self.__dict__
        #print(parameters)
        parameters.pop("_Product__CONST_CONVERT_TO_RUB")
        return parameters

    def setPrice(self, count):
        count = count * self.__CONST_CONVERT_TO_RUB
        self.prices = [LabeledPrice(self.title, int(count))]
 

class ProductProcessor:
    def __init__ (self):
        self.__productGetter = {
            "plan_starstart": self.__getStarsStart,
            "plan_astralbloom": self.__getAstralBloom,
            "plan_waytostars": self.__getWayToStars,
            "natal_chart": self.__getNatalChart,
            "one_taro_gen": self.__getOneTaro,
            "three_taro_gen": self.__getThreeTaro,
            "one_month_horoscope": self.__getOneMonthHoroscope,
            "three_month_horoscope": self.__getThreeMonthHoroscope,
            "one_year_horoscope": self.__getOneYearHoroscope
        }

    def getProduct(self, name, lang, cost):
        currentProduct = self.__productGetter[name](lang)
        currentProduct.setPrice(cost)
        return currentProduct
    
    def __getStarsStart(self,lang):
        return Product(**products[lang]["plan_starstart"])

    def __getWayToStars(self, lang):
        return Product(**products[lang]["plan_waytostars"])
    
    def __getAstralBloom(self,lang):
        return Product(**products[lang]["plan_astralbloom"])

    def __getNatalChart(self, lang):
        return Product(**products[lang]["natal_chart"])
    
    def __getOneTaro(self, lang):
        return Product(**products[lang]["one_taro_gen"])
    
    def __getThreeTaro(self, lang):
        return Product(**products[lang]["three_taro_gen"])
    
    def __getOneMonthHoroscope(self, lang):
        return Product(**products[lang]["one_month_horoscope"])
    
    def __getThreeMonthHoroscope(self, lang):
        return Product(**products[lang]["three_month_horoscope"])
    
    def __getOneYearHoroscope(self, lang):
        return Product(**products[lang]["one_year_horoscope"])