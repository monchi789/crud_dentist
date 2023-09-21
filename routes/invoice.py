from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette.exceptions import HTTPException
from starlette import status
from schemas.invoice import InvoiceRequest
# from models.models import Invoices
from models.invoice import Invoices
from datetime import datetime

router = APIRouter(
    tags=['Invoice']
)


@router.get('/invoices/', status_code=status.HTTP_200_OK)
async def get_all_invoices(db: db_dependency):
    return db.query(Invoices).all()


@router.get('/invoices/{invoice_id}', status_code=status.HTTP_200_OK)
async def get_invoice_by_id(db: db_dependency, invoice_id: int = Path(gt=0)):
    invoice_model = db.query(Invoices).filter(Invoices.id == invoice_id).first()

    if invoice_model is not None:
        return invoice_model
    raise HTTPException(status_code=404, detail='Invoice not found')


@router.get('/invoices/treatment/{treatment_id}', status_code=status.HTTP_200_OK)
async def get_invoice_by_treatment(db: db_dependency, treatment_id: int = Path(gt=0)):
    invoice_model = db.query(Invoices).filter(Invoices.treatmentId == treatment_id).all()
    if invoice_model is not None:
        return invoice_model
    raise HTTPException(status_code=404, detail='Treatment not found')


@router.post('/invoices/', status_code=status.HTTP_201_CREATED)
async def create_invoice(db: db_dependency, invoice_request: InvoiceRequest):
    date_offisue = datetime.strptime(invoice_request.date_offisue, '%Y-%m-%d')
    invoice_model = Invoices(date_offisue=date_offisue, invoice_amount=invoice_request.invoice_amount,
                             treatmentId=invoice_request.treatmentId)
    db.add(invoice_model)
    db.commit()


@router.put('/invoices/{invoice_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_invoice(db: db_dependency, invoice_request: InvoiceRequest, invoice_id: int = Path(gt=0)):

    invoice_model = db.query(Invoices).filter(Invoices.id == invoice_id).first()

    if invoice_model is None:
        raise HTTPException(status_code=404, detail='Invoice not found')
    try:
        date_offisue = datetime.strptime(invoice_request.date_offisue, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail='Invalid payment_date format. Use YYYY-MM-DD.')
    invoice_model.date_offisue = date_offisue
    invoice_model.invoice_amount = invoice_request.invoice_amount
    invoice_model.treatmentId = invoice_request.treatmentId

    db.add(invoice_model)
    db.commit()

    print(invoice_model.date_offisue, invoice_model.invoice_amount, invoice_model.treatmentId)


@router.delete('/invoices/{invoice_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice(db: db_dependency, invoice_id: int = Path(gt=0)):
    invoice_model = db.query(Invoices).filter(Invoices.id == invoice_id)

    if invoice_model is None:
        raise HTTPException(status_code=404, detail='Invoice not found')

    db.query(Invoices).filter(Invoices.id == invoice_id).delete()
    db.commit()
