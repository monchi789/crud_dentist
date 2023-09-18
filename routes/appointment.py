from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette import status
from starlette.exceptions import HTTPException
from models.appointment import Appointments
from schemas.appointment import AppointmentRequest

router = APIRouter()


@router.get('/appointments/', status_code=status.HTTP_200_OK)
async def get_all_appointments(db: db_dependency):
    return db.query(Appointments).all()


@router.get('/appointments/{appointment_id}', status_code=status.HTTP_200_OK)
async def get_appointment_by_id(db: db_dependency, appointment_id: int = Path(gt=0)):
    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()
    if appointment_model is not None:
        return appointment_model
    raise HTTPException(status_code=404, detail='Appointment not found')


@router.get('/appointments/patient/{patient_id}', status_code=status.HTTP_200_OK)
async def get_appointment_by_patient(db: db_dependency, patient_id: int = Path(gt=0)):
    appointmnet_model = db.query(Appointments).filter(Appointments.patientId == patient_id)
    if appointmnet_model is not None:
        return appointmnet_model
    raise HTTPException(status_code=404, detail='Patient not found')


@router.post('/appointments/', status_code=status.HTTP_201_CREATED)
async def create_appointment(db: db_dependency, appointment_request: AppointmentRequest):
    appointment_model = Appointments(**appointment_request.model_dump())
    db.add(appointment_model)
    db.commit()


@router.put('/appointments/{appointment_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_appointment(db: db_dependency, appointment_request: AppointmentRequest, appointment_id: int = Path(gt=0)):
    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()

    if appointment_model is None:
        raise HTTPException(status_code=404, detail='Appointment not found')

    appointment_model.date = appointment_request.date
    appointment_model.time = appointment_request.time
    appointment_model.description = appointment_request.description
    appointment_model.patientId = appointment_request.patientId

    db.add(appointment_model)
    db.commit()


@router.delete('/appointments/{appointment_id}')
async def delete_appointment(db: db_dependency, appointment_id: int = Path(gt=0)):
    appointment_model = db.query(Appointments).filter(Appointments.id == appointment_id).first()

    if appointment_model is None:
        raise HTTPException(status_code=404, detail='Appointment not found')

    db.query(Appointments).filter(Appointments.id == appointment_id).delete()
    db.commit()