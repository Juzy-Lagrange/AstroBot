from Bot.bot import *
from Handlers.MessageHandlers.ReplyMarkups.choose_language import choose_language

def change_language(message, bot: AsyncTeleBot):
    choose_language(message, bot)