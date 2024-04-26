from utility.constants.db_constant import *
from DB.init_db_models import ledger
import datetime

def addLedger(
    tranzaction_id : int,
    invoice_id: int, 
    invoice_status: InvoiceStatus,
    comment: PaymentType,
    status: LedgerStatus,
    tranzactions_status = TranzactionType.NO_TRANZACTION):
    
    created_at = datetime.datetime.today()
    updated_at = datetime.datetime.today()

    ledger.insert(tranzaction_id=tranzaction_id, invoice_id=invoice_id, 
                     invoice_status=invoice_status, tranzactions_status=tranzactions_status, 
                     created_at=created_at, updated_at=updated_at, 
                     comment=comment, status = status).on_conflict_ignore().execute()