from os import getenv
from dotenv import load_dotenv

load_dotenv()
PROVIDER_TOKEN_TEST = getenv("PROVIDER_TOKEN_TEST")

products = {
#<================================================>
#                   RUSSIAN LANG
#<================================================>    
    "ru": {
        "plan_starstart": {
            "title": "Звездный старт",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_starstart",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_astralbloom": {
            "title":"Астральный Что-то там",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_astralbloom",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_waytostars": {
            "title":"Путь к звездам",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "natal_chart": {
            "title":"натальная карта",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        }
    },

#<================================================>
#                   ENGLISH LANG
#<================================================>

    "en": {
        "plan_starstart": {
            "title":"Way to stars",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_astralbloom": {
            "title":"astral bloom",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_astralbloom",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_waytostars": {
            "title":"way to stars",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "natal_chart": {
            "title":"натальная карта",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        }
    },
    
#<================================================>
#                   TURKISH LANG
#<================================================>
    "trk": {
        "plan_starstart": {
            "title":"Way to stars",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_astralbloom": {
            "title":"astral bloom",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_astralbloom",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "plan_waytostars": {
            "title":"way to stars",
            "description":"U get tuc tuc tuc bac bac bac",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        },
        "natal_chart": {
            "title":"натальная карта",
            "description":"Данный продукт включает в себя:\n то, то и то...",
            "invoice_payload":"plan_waytostars",
            "provider_token": PROVIDER_TOKEN_TEST,
            "currency":"rub"
        }
    }
}

costs = {
    "plan_starstart": 990,
    "plan_astralbloom": 1300,
    "plan_waytostars": 1500,
    "natal_chart": 300
}