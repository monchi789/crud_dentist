from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette import status
from starlette.exceptions import HTTPException
from datetime import datetime
from models.appointment import Appointments
from schemas.appointment import AppointmentRequest
from routes.token import user_dependency

router = APIRouter(
    tags=['Appointment']
)


@router.get('/appointments/', status_code=status.HTTP_200_OK)
async def get_all_appointments(user: user_dependency, db: db_dependency):
    """
       Obtiene todas las citas médicas.

       Args:
           user: Dependencia de usuario autenticado.
           db: Dependencia de la base de datos.

       Returns:
           list[Appointments]: Lista de todas las citas médicas registradas.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')
    return db.query(Appointments).all()


@router.get('/appointments/{appointment_id}', status_code=status.HTTP_200_OK)
async def get_appointment_by_id(user: user_dependency, db: db_dependency, appointment_id: int = Path(gt=0)):
    """
        Obtiene una cita médica por su identificador.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            appointment_id (int): Identificador de la cita médica a recuperar.

        Returns:
            Appointments: La cita médica correspondiente al ID proporcionado.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()
    if appointment_model is not None:
        return appointment_model
    raise HTTPException(status_code=404, detail='Appointment not found')


@router.get('/appointments/patient/{patient_id}', status_code=status.HTTP_200_OK)
async def get_appointment_by_patient(user: user_dependency, db: db_dependency, patient_id: int = Path(gt=0)):
    """
        Obtiene las citas médicas asociadas a un paciente específico.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            patient_id (int): Identificador del paciente.

        Returns:
            list[Appointments]: Lista de citas médicas asociadas al paciente.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    appointmnet_model = db.query(Appointments).filter(Appointments.patientId == patient_id)
    if appointmnet_model is not None:
        return appointmnet_model
    raise HTTPException(status_code=404, detail='Patient not found')


@router.post('/appointments/', status_code=status.HTTP_201_CREATED)
async def create_appointment(user: user_dependency, db: db_dependency, appointment_request: AppointmentRequest):
    """
        Crea una nueva cita médica.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            appointment_request (AppointmentRequest): Datos de la cita médica a crear en formato JSON.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    date = datetime.strptime(appointment_request.date, '%Y-%m-%d')
    format_time = datetime.strptime(appointment_request.time, '%H:%M:%S').time()
    appointment_model = Appointments(
        date=date, time=format_time, description=appointment_request.description,
        patientId=appointment_request.patientId
    )
    db.add(appointment_model)
    db.commit()


@router.put('/appointments/{appointment_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_appointment(user: user_dependency, db: db_dependency, appointment_request: AppointmentRequest, appointment_id: int = Path(gt=0)):
    """
        Actualiza una cita médica existente.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            appointment_request (AppointmentRequest): Datos de la cita médica a actualizar en formato JSON.
            appointment_id (int): Identificador de la cita médica a actualizar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()

    if appointment_model is None:
        raise HTTPException(status_code=404, detail='Appointment not found')

    try:
        date = datetime.strptime(appointment_request.date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=404, detail='Invalid date format. Use YYYY-MM-DD.')

    appointment_model.date = date
    appointment_model.time = appointment_request.time
    appointment_model.description = appointment_request.description
    appointment_model.patientId = appointment_request.patientId

    db.add(appointment_model)
    db.commit()


@router.delete('/appointments/{appointment_id}')
async def delete_appointment(user: user_dependency, db: db_dependency, appointment_id: int = Path(gt=0)):
    """
        Elimina una cita médica existente.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            appointment_id (int): Identificador de la cita médica a eliminar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authetication Failed.')

    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()

    if appointment_model is None:
        raise HTTPException(status_code=404, detail='Appointment not found')

    db.query(Appointments).filter(Appointments.id == appointment_id).delete()
    db.commit()
