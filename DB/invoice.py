from utility.constants.db_constant import *
from DB.init_db_models import invoices
from DB.ledger import addLedger

def addInvoice(
    chat_id : str,
    product_id: int, 
    creation_date,
    expired_date,
    gateway: PaymentType,
    currency: CurrencyType,
    amount: float,
    status: InvoiceStatus,
    crypto_invoice_id=None):

    invoice_id = invoices.insert(chat_id=chat_id, product_id=product_id, 
                     creation_date=creation_date, expired_date=expired_date, 
                     gateway=gateway, currency=currency, 
                     amount=amount, status=status,
                     crypto_invoice_id=crypto_invoice_id).on_conflict_ignore().execute()
    
    addLedger(tranzaction_id=None, invoice_id=invoice_id, 
              invoice_status=InvoiceStatus.ACTIVE,
              comment=None, status=LedgerStatus.INVOICE_NEW)
    
    return invoice_id


def updInvoiceStatus(invoice_id, status: InvoiceStatus):
    invoice = invoices.get(invoices.id == invoice_id)
    invoice.status = status

    if status == InvoiceStatus.PAID:
        ledger_status = LedgerStatus.INVOICE_PAID
    elif status == InvoiceStatus.EXPIRED:
        ledger_status = LedgerStatus.INVOICE_EXPIRED
        
    addLedger(tranzaction_id=None, invoice_id=invoice_id, 
              invoice_status=status,
              comment=None, status=ledger_status)
    invoice.save()
    return invoice