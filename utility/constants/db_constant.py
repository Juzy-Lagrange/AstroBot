#<==============================================>
#               currency
#<==============================================>
class InvoiceStatus:
    EXPIRED = "expired"
    ACTIVE = "active"
    PAID = "paid"    

class PaymentType:
    CRYPTO = "crypto"
    FIAT = "fiat"

class CurrencyType:
    RUB = "RUB"
    USDT = "USDT"
    BTC = "BTC"
    TON = "TON"


class TranzactionType:
    PAID="paid"
    NEW = "new"
    NO_TRANZACTION="no_tranzaction"

class LedgerStatus:
    INVOICE_NEW = "new_invoice"
    INVOICE_EXPIRED =  "invoice_expired"
    INVOICE_PAID = "invoice_paid"
    INVOICE_PAID = "upd_invoice_status"

    TRANSACTION_NEW = "new_transaction"
    