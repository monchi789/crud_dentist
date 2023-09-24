from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette.exceptions import HTTPException
from models.patient import Patients
from starlette import status
from schemas.patient import PatientRequest


router = APIRouter(
    tags=['Patient']
)


@router.get('/patients/', status_code=status.HTTP_200_OK)
async def get_all_patients(db: db_dependency):
    return db.query(Patients).all()


@router.get('/patients/{patient_id}', status_code=status.HTTP_200_OK)
async def get_patient_by_id(db: db_dependency, patient_id: int = Path(gt=0)):
    patient_model = db.query(Patients).filter(Patients.id == patient_id).first()
    if patient_model is not None:
        return patient_model
    raise HTTPException(status_code=404, detail='Patient not found.')


@router.get('/patients/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_patient_by_user(db: db_dependency, user_id: int = Path(gt=0)):
    patient_model = db.query(Patients).filter(Patients.userId == user_id).all()
    if patient_model is not None:
        return patient_model
    raise HTTPException(status_code=404, detail='User and Patient not found')


@router.post('/patients/', status_code=status.HTTP_201_CREATED)
async def create_patient(db: db_dependency, patient_request: PatientRequest):
    patient_model = Patients(**patient_request.model_dump())
    db.add(patient_model)
    db.commit()


@router.put('/patients/{patient_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_patient(db: db_dependency, patient_request: PatientRequest, patient_id: int = Path(gt=0)):
    patient_model = db.query(Patients).filter(Patients.id == patient_id).first()

    if patient_model is None:
        raise HTTPException(status_code=404, detail='Patient not found')

    patient_model.first_name = patient_request.first_name
    patient_model.last_name = patient_request.last_name
    patient_model.phone_number = patient_request.phone_number
    patient_model.address = patient_request.address
    patient_model.userId = patient_request.userId

    db.add(patient_model)
    db.commit()


@router.delete('/patients/{patient_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(db: db_dependency, patient_id: int = Path(gt=0)):
    patient_model = db.query(Patients).filter(Patients.id == patient_id).first()

    if patient_model is None:
        raise HTTPException(status_code=404, detail='Patient not found')
    db.query(Patients).filter(Patients.id == patient_id).delete()
    db.commit()
