import json

from os import getenv
from dotenv import load_dotenv

from crypto_payments.crypro_payments import *

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, LabeledPrice, InputFile
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters
from asyncio import sleep as async_sleep

from AstrologyAPISDK.sdk import AstrologyAPIClient
from DB.init_db_models import Models
from session.session import *

from Bot.products import ProductProcessor

from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.asyncio_storage import StateMemoryStorage

with open('./localization/local.json', encoding="utf-8") as localization:
    content = localization.read()
    localization = json.loads(content)

class MyStates(StatesGroup):
    # Just name variables differently
    default = State()
    
    prepare = State()
    wait_for_message = State()
    post = State()

    wait_for_user_name = State()
    send_gift = State()

    choose_currency = State()
    currency_rub = State()
    currency_crypto = State()

    change_lang = State()

class ForwardFilter(asyncio_filters.SimpleCustomFilter):
    key = 'is_forwarded'
    async def check(self, message):
        return message.forward_date is not None


class active_invoice_status:
    status = True

globals().update(Models)

load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")
ASTROLOGY_API_TOKEN = getenv("ASTROLOGY_API")
ASTROLOGY_USER_TOKEN = getenv("ASTROLOGY_ID")


astro_clinet = AstrologyAPIClient(
    ASTROLOGY_USER_TOKEN,
    ASTROLOGY_API_TOKEN
)

ProductFabricMethod = ProductProcessor()
active_invoices = active_invoice_status()

admin_ids = [718202048,1199045651,5424241246]

session = Session()