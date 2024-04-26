
from aiocryptopay import AioCryptoPay
from aiocryptopay.const import (
    HTTPMethods,
    Networks,
    Assets,
    PaidButtons,
    InvoiceStatus,
    CurrencyType,
    CheckStatus,
)
from aiocryptopay.models.update import Update

from os import getenv
from dotenv import load_dotenv

load_dotenv()
CRYPRO_PAY_TEST_TOKEN = getenv("CRYPRO_PAY_TEST_TOKEN")
cryptoPay = AioCryptoPay(token=CRYPRO_PAY_TEST_TOKEN, network=Networks.TEST_NET)
