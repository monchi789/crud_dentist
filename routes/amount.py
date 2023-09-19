from fastapi import APIRouter, Path
# from models.models import Amounts
from models.amount import Amounts
from starlette import status
from starlette.exceptions import HTTPException
from schemas.amount import AmountRequest
from config.database import db_dependency
from datetime import datetime

router = APIRouter()


@router.get('/amounts/', status_code=status.HTTP_200_OK)
async def get_all_amounts(db: db_dependency):
    return db.query(Amounts).all()


@router.get('/amounts/{amount_id}', status_code=status.HTTP_200_OK)
async def get_amount_by_id(db: db_dependency, amount_id: int = Path(gt=0)):
    amount_model = db.query(Amounts).filter(Amounts.id == amount_id).first()
    if amount_model is not None:
        return amount_model
    raise HTTPException(status_code=404, detail='Amount not found')


@router.get('/amounts/treatment/{treatment_id}', status_code=status.HTTP_200_OK)
async def get_amount_by_treatment(db: db_dependency, treatment_id: int = Path(gt=0)):
    amount_model = db.query(Amounts).filter(Amounts.treatmentId == treatment_id)
    if amount_model is not None:
        return amount_model
    raise HTTPException(status_code=404, detail='Treatment not found')


@router.post('/amounts/', status_code=status.HTTP_201_CREATED)
async def create_amount(db: db_dependency, amount_request: AmountRequest):
    payment_date = datetime.strptime(amount_request.payment_date, '%Y-%m-%d')

    amount_model = Amounts(payment_date=payment_date, amount_payment=amount_request.amount_payment,
                           treatmentId=amount_request.treatmentId)
    db.add(amount_model)
    db.commit()


@router.put('/amounts/{amount_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_amount(db: db_dependency, amount_request: AmountRequest, amount_id: int = Path(gt=0)):
    amount_model = db.query(Amounts).filter(Amounts.id == amount_id).first()

    if amount_model is None:
        raise HTTPException(status_code=404, detail='Amount not found')

    try:
        payment_date = datetime.strptime(amount_request.payment_date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail='Invalid payment_date format. Use YYYY-MM-DD.')

    amount_model.payment_date = payment_date
    amount_model.amount_payment = amount_request.amount_payment
    amount_model.treatment_id = amount_request.treatmentId

    db.add(amount_model)
    db.commit()


@router.delete('/amounts/{amount_id}')
async def delete_amount(db: db_dependency, amount_id: int = Path(gt=0)):
    amount_model = db.query(Amounts).filter(Amounts.id == amount_id).first()

    if amount_model is None:
        raise HTTPException(status_code=404, detail='Amount not found')
    db.query(Amounts).filter(Amounts.id == amount_id).delete()
    db.commit()

