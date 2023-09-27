from fastapi import APIRouter, Path
from models.amount import Amounts
from starlette import status
from starlette.exceptions import HTTPException
from schemas.amount import AmountRequest
from config.database import db_dependency
from datetime import datetime
from routes.token import user_dependency

router = APIRouter(
    tags=['Amount']
)


@router.get('/amounts/', status_code=status.HTTP_200_OK)
async def get_all_amounts(user: user_dependency, db: db_dependency):
    """
       Obtiene todos los pagos asociados a tratamientos médicos.

       Args:
           user: Dependencia de usuario autenticado.
           db: Dependencia de la base de datos.

       Returns:
           list[Amounts]: Lista de todos los pagos registrados.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    return db.query(Amounts).all()


@router.get('/amounts/{amount_id}', status_code=status.HTTP_200_OK)
async def get_amount_by_id(user: user_dependency, db: db_dependency, amount_id: int = Path(gt=0)):
    """
        Obtiene un pago por su identificador.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            amount_id (int): Identificador del pago a recuperar.

        Returns:
            Amounts: El pago correspondiente al ID proporcionado.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    amount_model = db.query(Amounts).filter(Amounts.id == amount_id).first()
    if amount_model is not None:
        return amount_model
    raise HTTPException(status_code=404, detail='Amount not found')


@router.get('/amounts/treatment/{treatment_id}', status_code=status.HTTP_200_OK)
async def get_amount_by_treatment(user: user_dependency, db: db_dependency, treatment_id: int = Path(gt=0)):
    """
        Obtiene los pagos asociados a un tratamiento médico específico.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            treatment_id (int): Identificador del tratamiento médico.

        Returns:
            list[Amounts]: Lista de pagos asociados al tratamiento médico.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    amount_model = db.query(Amounts).filter(Amounts.treatmentId == treatment_id)
    if amount_model is not None:
        return amount_model
    raise HTTPException(status_code=404, detail='Treatment not found')


@router.post('/amounts/', status_code=status.HTTP_201_CREATED)
async def create_amount(user: user_dependency, db: db_dependency, amount_request: AmountRequest):
    """
        Crea un nuevo registro de pago.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            amount_request (AmountRequest): Datos del pago a crear en formato JSON.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    payment_date = datetime.strptime(amount_request.payment_date, '%Y-%m-%d')
    amount_model = Amounts(payment_date=payment_date, amount_payment=amount_request.amount_payment,
                           treatmentId=amount_request.treatmentId)
    db.add(amount_model)
    db.commit()


@router.put('/amounts/{amount_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_amount(user: user_dependency, db: db_dependency, amount_request: AmountRequest, amount_id: int = Path(gt=0)):
    """
        Actualiza un registro de pago existente.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            amount_request (AmountRequest): Datos del pago a actualizar en formato JSON.
            amount_id (int): Identificador del pago a actualizar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

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
async def delete_amount(user: user_dependency, db: db_dependency, amount_id: int = Path(gt=0)):
    """
       Elimina un registro de pago existente.

       Args:
           user: Dependencia de usuario autenticado.
           db: Dependencia de la base de datos.
           amount_id (int): Identificador del pago a eliminar.

       Returns:
           None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    amount_model = db.query(Amounts).filter(Amounts.id == amount_id).first()

    if amount_model is None:
        raise HTTPException(status_code=404, detail='Amount not found')
    
    db.query(Amounts).filter(Amounts.id == amount_id).delete()
    db.commit()

