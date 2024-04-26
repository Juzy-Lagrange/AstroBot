from Bot.bot import session, AsyncTeleBot
from telebot.types import InputMediaPhoto
from taro_bot import cards


async def generate_one_card(user_id, lc, bot: AsyncTeleBot):
    deck = cards.get_deck(session.getLang(user_id))
    cards.shuffle_deck(deck)
    card = cards.get_card(deck)

    if card[1] == -1:
        one_card_msg = lc["RFormatedTaroString"].format(card[0]["name"], card[0]["rdesc"])
    else:
        one_card_msg = lc["FormatedTaroString"].format(card[0]["name"], card[0]["desc"])

    img = open("taro_bot/"+card[0]["image"], 'rb')
    await bot.send_photo(user_id,img,caption = one_card_msg)
    

async def generate_three_cards(user_id, lc, bot: AsyncTeleBot):

    deck = cards.get_deck(session.getLang(user_id))
    cards.shuffle_deck(deck)
    tcards = [cards.get_card(deck) for _ in range(3)]

    genMsg = lambda card: lc["RFormatedTaroString"].format(card[0]["name"], card[0]["rdesc"]) if card[1] == -1 else lc["FormatedTaroString"].format(card[0]["name"], card[0]["desc"])
    imgs = []
    for card in tcards:
        img = open(f"./taro_bot/{card[0]['image']}","+rb")
        imgs.append(img)
    texts = [genMsg(card) for card in tcards]  

    for i in range(3):
        await bot.send_photo(user_id, imgs[i], caption = texts[i])