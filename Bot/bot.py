import json

from os import getenv
from dotenv import load_dotenv

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, LabeledPrice
from telebot.async_telebot import AsyncTeleBot
from asyncio import sleep as async_sleep

from AstrologyAPISDK.sdk import AstrologyAPIClient
from DB.init_db_models import Models
from session.session import *

from Bot.products import ProductProcessor

with open('./localization/local.json', encoding="utf-8") as localization:
    content = localization.read()
    localization = json.loads(content)

load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_TOKEN")
ASTROLOGY_API_TOKEN = getenv("ASTROLOGY_API")
ASTROLOGY_USER_TOKEN = getenv("ASTROLOGY_ID")

astro_clinet = AstrologyAPIClient(
    ASTROLOGY_USER_TOKEN,
    ASTROLOGY_API_TOKEN
)

ProductFabricMethod = ProductProcessor()


session = Session()