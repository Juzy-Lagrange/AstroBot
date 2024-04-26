from utility.constants.db_constant import *
from DB.init_db_models import tranzactions
from DB.invoice import updInvoiceStatus
from DB.ledger import addLedger

def addTranzactions(
    invoice_id: int,
    paid_amount: float,
    currency: CurrencyType,
    usd_rate: float,
    currency_fee: CurrencyType,
    fee_amount: float,
    ):

    status = TranzactionType.PAID
    
    transaction = tranzactions.insert(
        invoice_id=invoice_id, paid_amount=paid_amount,
        currency=currency, usd_rate=usd_rate,
        currency_fee=currency_fee, fee_amount=fee_amount,
        status=status
    ).on_conflict_ignore().execute()

    new_invoice = updInvoiceStatus(invoice_id, InvoiceStatus.PAID)

    addLedger(tranzaction_id=transaction, 
              invoice_id=invoice_id,
              invoice_status=InvoiceStatus.PAID, 
              tranzactions_status=TranzactionType.PAID,
              comment=None, status=LedgerStatus.TRANSACTION_NEW)
    
    return [new_invoice, tranzactions.get(tranzactions.id == transaction)]
    
    

