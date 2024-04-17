from Bot.products_dict import products
from telebot.types import LabeledPrice

class Product:
    def __init__ (self, title, description, invoice_payload, provider_token, currency):
        self.__CONST_CONVERT_TO_RUB = 100
        self.title = title
        self.description = description
        self.invoice_payload = invoice_payload
        self.provider_token = provider_token
        self.currency = currency
    
    def getProductParameters(self):
        parameters =  self.__dict__
        parameters.pop("_Product__CONST_CONVERT_TO_RUB")
        return parameters

    def setPrice(self, count):
        count = count * self.__CONST_CONVERT_TO_RUB
        self.prices = [LabeledPrice(f'{self.title}',count)]
 

class ProductProcessor:
    def __init__ (self):
        self.__productGetter = {
            "plan_starstart": self.__getStarsStart,
            "plan_astralbloom": self.__getAstralBloom,
            "plan_waytostars": self.__getWayToStars,
            "natal_chart": self.__getNatalChart,
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