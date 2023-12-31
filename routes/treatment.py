from fastapi import APIRouter, Path
from models.treatment import Treatments
from schemas.treatment import TreatmentRequest
from starlette import status
from starlette.exceptions import HTTPException
from config.database import db_dependency
from routes.token import user_dependency

router = APIRouter(
    tags=['Treatment']
)


@router.get('/treatments/', status_code=status.HTTP_200_OK)
async def get_all_treatments(user: user_dependency, db: db_dependency):
    """
        Obtiene todos los tratamientos médicos.

        Args:
            user (dict): Usuario autenticado.
            db: Dependencia de la base de datos.

        Returns:
            list[Treatments]: Lista de objetos de tratamiento médico.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    return db.query(Treatments).all()


@router.get('/treatments/{id_treatment}')
async def get_treatment_by_id(user: user_dependency, db: db_dependency, treatment_id: int = Path(gt=0)):
    """
        Obtiene un tratamiento médico por ID.

        Args:
            user (dict): Usuario autenticado.
            db: Dependencia de la base de datos.
            treatment_id (int): ID del tratamiento médico.

        Returns:
            Treatments: Objeto de tratamiento médico.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    treatment_model = db.query(Treatments).filter(Treatments.id == treatment_id).first()
    if treatment_model is not None:
        return treatment_model
    raise HTTPException(status_code=404, detail='Treatment not found')


@router.get('/treatments/patient/{patient_id}')
async def get_treatment_by_patient(user: user_dependency, db: db_dependency, patient_id: int = Path(gt=0)):
    """
        Obtiene un tratamiento médico por ID de paciente.

        Args:
            user (dict): Usuario autenticado.
            db: Dependencia de la base de datos.
            patient_id (int): ID del paciente.

        Returns:
            Treatments: Objeto de tratamiento médico asociado al paciente.
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    treatment_model = db.query(Treatments).filter(Treatments.patientId == patient_id).first()
    if treatment_model is not None:
        return treatment_model
    raise HTTPException(status_code=404, detail='Patient not found')


@router.post('/treatments/', status_code=status.HTTP_201_CREATED)
async def create_treatment(user: user_dependency, db: db_dependency, treatment_request: TreatmentRequest):
    """
        Crea un nuevo tratamiento médico.

        Args:
            user (dict): Usuario autenticado.
            db: Dependencia de la base de datos.
            treatment_request (TreatmentRequest): Datos del tratamiento médico a crear.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed')

    treatment_model = Treatments(**treatment_request.model_dump())
    db.add(treatment_model)
    db.commit()


@router.put('/treatments/', status_code=status.HTTP_204_NO_CONTENT)
async def update_treatment(user: user_dependency, db: db_dependency, treatment_request: TreatmentRequest):
    """
        Actualiza un tratamiento médico existente.

        Args:
            user (dict): Usuario autenticado.
            db: Dependencia de la base de datos.
            treatment_request (TreatmentRequest): Datos del tratamiento médico a actualizar.

        Returns:
            None
    """

    if user is None:
        raise HTTPException(status_code=404, detail='Authentication Failed.')

    treatment_model = db.query(Treatments).filter(Treatments.id == treatment_request).first()

    if treatment_model is None:
        raise HTTPException(status_code=404, detail='Treatment not found')

    treatment_model.treatment_name = treatment_request.treatment_name
    treatment_model.description = treatment_request.description
    treatment_model.inicial_amount = treatment_request.inicial_amount
    treatment_model.total_amount = treatment_request.total_amount

    db.add(treatment_model)
    db.commit()

