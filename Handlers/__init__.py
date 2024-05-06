from Handlers.MessageHandlers.Commands.commands import send_greetings as greetings, send_help, send_info, send_price
from Handlers.MessageHandlers.ReplyMarkups.choose_language import choose_language
from Handlers.MessageHandlers.ReplyMarkups.main_menu import send_start_page
from Handlers.MessageHandlers.ReplyMarkups.main_menu import send_main_menu


from Handlers.MessageHandlers.ReplyMarkups.general import *
from Handlers.MessageHandlers.ReplyMarkups.change_lang import change_language
from Handlers.MessageHandlers.ReplyMarkups.change_subscirbe_status import change_subscribe_status

from Handlers.MessageHandlers.AdminPanel.admin_panel import *

from Handlers.MessageHandlers.ReplyMarkups.natal_chart import natal_chart_gen
from Handlers.MessageHandlers.ReplyMarkups.natal_chart import get_webapp_data
from Handlers.MessageHandlers.ReplyMarkups.natal_chart import send_example_chart
from Handlers.MessageHandlers.ReplyMarkups.natal_chart import generate_natal_chart

from Handlers.MessageHandlers.ReplyMarkups.taro import send_one_card_taro_spread
from Handlers.MessageHandlers.ReplyMarkups.taro import send_three_card_taro_spread
from Handlers.MessageHandlers.ReplyMarkups.taro import taro_predictions

from Handlers.MessageHandlers.ReplyMarkups.daily_functions import day_arcane
from Handlers.MessageHandlers.ReplyMarkups.daily_functions import day_color
from Handlers.MessageHandlers.ReplyMarkups.daily_functions import day_number

from Handlers.MessageHandlers.ReplyMarkups.horoscope import *

from Handlers.PreCheckoutQueryHandler.checkout_handler import checkout

from Handlers.PaymentsHandlers.SendProductsresult.plans import *
from Handlers.PaymentsHandlers.payments import successful_payment

from Handlers.CallbackHandlers.callbacks import *

from Handlers.Choose_currency.choose_currency import *

from Handlers.SEND_INVOICE.crypto_invoice import *
from Handlers.SEND_INVOICE.rub_invoice import *
