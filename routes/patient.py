from fastapi import APIRouter, Path
from config.database import db_dependency
from starlette.exceptions import HTTPException
from models.patient import Patients
from starlette import status
from schemas.patient import PatientRequest
from routes.token import user_dependency

router = APIRouter(
    tags=['Patient']
)


@router.get('/patients/', status_code=status.HTTP_200_OK)
async def get_all_patients(user: user_dependency, db: db_dependency):
    """
        Obtiene todos los pacientes asociados al usuario autenticado.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.

        Returns:
            list[Patients]: Lista de todos los pacientes registrados para el usuario autenticado.
    """

    return db.query(Patients).filter(Patients.userId == user.get('id')).all()


@router.get('/patients/{patient_id}', status_code=status.HTTP_200_OK)
async def get_patient_by_id(user: user_dependency, db: db_dependency, patient_id: int = Path(gt=0)):
    """
        Obtiene un paciente por su identificador, asociado al usuario autenticado.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            patient_id (int): Identificador del paciente a recuperar.

        Returns:
            Patients: El paciente correspondiente al ID proporcionado y asociado al usuario autenticado.
    """

    patient_model = (db.query(Patients).filter(Patients.id == patient_id).filter(Patients.userId == user.get('id'))
                     .first())
    if patient_model is not None:
        return patient_model
    raise HTTPException(status_code=404, detail='Patient not found.')


@router.get('/patients/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_patient_by_user(user: user_dependency, db: db_dependency, user_id: int = Path(gt=0)):
    """
        Obtiene todos los pacientes asociados a un usuario específico.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            user_id (int): Identificador del usuario.

        Returns:
            list[Patients]: Lista de pacientes asociados al usuario especificado.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    patient_model = db.query(Patients).filter(Patients.userId == user_id).all()
    if patient_model is not None:
        return patient_model
    raise HTTPException(status_code=404, detail='User and Patient not found')


@router.post('/patients/', status_code=status.HTTP_201_CREATED)
async def create_patient(user: user_dependency, db: db_dependency, patient_request: PatientRequest):
    """
        Crea un nuevo paciente asociado al usuario autenticado.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            patient_request (PatientRequest): Datos del paciente a crear en formato JSON.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Athentication Failed')
    patient_model = Patients(
        first_name=patient_request.first_name, last_name=patient_request.last_name,
        phone_number=patient_request.phone_number, address=patient_request.address,
        userId=user.get('id')
    )
    db.add(patient_model)
    db.commit()


@router.put('/patients/{patient_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_patient(user: user_dependency, db: db_dependency, patient_request: PatientRequest,
                         patient_id: int = Path(gt=0)):
    """
        Actualiza un paciente existente asociado al usuario autenticado.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            patient_request (PatientRequest): Datos del paciente a actualizar en formato JSON.
            patient_id (int): Identificador del paciente a actualizar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    patient_model = (db.query(Patients).filter(Patients.id == patient_id).
                     filter(Patients.userId == user.get('id')).first())

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
async def delete_patient(user: user_dependency, db: db_dependency, patient_id: int = Path(gt=0)):
    """
        Elimina un paciente existente asociado al usuario autenticado.

        Args:
            user: Dependencia de usuario autenticado.
            db: Dependencia de la base de datos.
            patient_id (int): Identificador del paciente a eliminar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    patient_model = (db.query(Patients).filter(Patients.id == patient_id).
                     filter(Patients.userId == user.get('id')).first())
    if patient_model is None:
        raise HTTPException(status_code=404, detail='Patient not found')
    db.query(Patients).filter(Patients.id == patient_id).delete()
    db.commit()
