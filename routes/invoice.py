from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette.exceptions import HTTPException
from starlette import status
from schemas.invoice import InvoiceRequest
from models.invoice import Invoices
from datetime import datetime
from routes.token import user_dependency

router = APIRouter(
    tags=['Invoice']
)


@router.get('/invoices/', status_code=status.HTTP_200_OK)
async def get_all_invoices(user: user_dependency, db: db_dependency):
    """
       Obtiene todas las facturas.

       Args:
           user: Dependencia de usuario autenticado.
           db: Dependencia de la base de datos.

       Returns:
           list[Invoices]: Lista de todas las facturas registradas.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    return db.query(Invoices).all()


@router.get('/invoices/{invoice_id}', status_code=status.HTTP_200_OK)
async def get_invoice_by_id(user: user_dependency, db: db_dependency, invoice_id: int = Path(gt=0)):
    """
        Obtiene una factura por su identificador.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            invoice_id (int): Identificador de la factura a recuperar.

        Returns:
            Invoices: La factura correspondiente al ID proporcionado.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    invoice_model = db.query(Invoices).filter(Invoices.id == invoice_id).first()

    if invoice_model is not None:
        return invoice_model
    raise HTTPException(status_code=404, detail='Invoice not found')


@router.get('/invoices/treatment/{treatment_id}', status_code=status.HTTP_200_OK)
async def get_invoice_by_treatment(user: user_dependency, db: db_dependency, treatment_id: int = Path(gt=0)):
    """
        Obtiene las facturas asociadas a un tratamiento médico específico.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            treatment_id (int): Identificador del tratamiento médico.

        Returns:
            list[Invoices]: Lista de facturas asociadas al tratamiento médico.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    invoice_model = db.query(Invoices).filter(Invoices.treatmentId == treatment_id).all()
    if invoice_model is not None:
        return invoice_model
    raise HTTPException(status_code=404, detail='Treatment not found')


@router.post('/invoices/', status_code=status.HTTP_201_CREATED)
async def create_invoice(user: user_dependency, db: db_dependency, invoice_request: InvoiceRequest):
    """
        Crea una nueva factura.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            invoice_request (InvoiceRequest): Datos de la factura a crear en formato JSON.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    date_offisue = datetime.strptime(invoice_request.date_offisue, '%Y-%m-%d')
    invoice_model = Invoices(date_offisue=date_offisue, invoice_amount=invoice_request.invoice_amount,
                             treatmentId=invoice_request.treatmentId)
    db.add(invoice_model)
    db.commit()


@router.put('/invoices/{invoice_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_invoice(user: user_dependency, db: db_dependency, invoice_request: InvoiceRequest,
                         invoice_id: int = Path(gt=0)):
    """
        Actualiza una factura existente.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            invoice_request (InvoiceRequest): Datos de la factura a actualizar en formato JSON.
            invoice_id (int): Identificador de la factura a actualizar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

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
async def delete_invoice(user: user_dependency, db: db_dependency, invoice_id: int = Path(gt=0)):
    """
        Elimina una factura existente.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            invoice_id (int): Identificador de la factura a eliminar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    invoice_model = db.query(Invoices).filter(Invoices.id == invoice_id)

    if invoice_model is None:
        raise HTTPException(status_code=404, detail='Invoice not found')

    db.query(Invoices).filter(Invoices.id == invoice_id).delete()
    db.commit()
