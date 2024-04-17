from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards import getPredictionsTaroButtons
from telebot.types import InputMediaPhoto
from taro_bot import cards

async def taro_predictions(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    taro_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    taro_markup.add(*getPredictionsTaroButtons(lc))
    await bot.send_message(message.chat.id,lc["TaroChooseFunc"],reply_markup = taro_markup)


async def send_one_card_taro_spread(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    deck = cards.get_deck()
    cards.shuffle_deck(deck)
    card = cards.get_card(deck)

    if card[1] == -1:
        one_card_msg = lc["RFormatedTaroString"].format(card[0]["name"], card[0]["rdesc"])
    else:
        one_card_msg = lc["FormatedTaroString"].format(card[0]["name"], card[0]["desc"])

    img = open("taro_bot/"+card[0]["image"], 'rb')
    await bot.send_photo(user_id,img,caption = one_card_msg)


async def send_three_card_taro_spread(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    deck = cards.get_deck()
    cards.shuffle_deck(deck)
    tcards = [cards.get_card(deck) for _ in range(3)]

    genMsg = lambda card: lc["RFormatedTaroString"].format(card[0]["name"], card[0]["rdesc"]) if card[1] == -1 else lc["FormatedTaroString"].format(card[0]["name"], card[0]["desc"])
    imgs = [open("taro_bot/"+card[0]["image"],'rb') for card in tcards]
    texts = [genMsg(card) for card in tcards]  

    for i in range(3):
        await bot.send_photo(user_id,imgs[i], caption = texts[i])
