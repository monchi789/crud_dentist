from fastapi import APIRouter, Path
from starlette import status
from starlette.exceptions import HTTPException
from config.database import db_dependency
from models.user import Users
from schemas.user import UserRequest
from jose import jwt
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


router = APIRouter(
    tags=['User']
)


@router.get('/users/')
async def get_all_users(db: db_dependency):
    return db.query(Users).all()


@router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(db: db_dependency, user_id: int = Path(gt=0)):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail='User not found.')


@router.post('/user', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    user_model = Users(username=user_request.username, phone_number=user_request.phone_number,
                       email=user_request.email, first_name=user_request.first_name,
                       last_name=user_request.last_name,
                       password=bcrypt_context.hash(user_request.password))
    db.add(user_model)
    db.commit()


@router.put('/user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user_request: UserRequest, user_id: int = Path(gt=0)):
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail='User not found.')

    user_model.username = user_request.username
    user_model.email = user_request.email
    user_model.phone_number = user_request.phone_number
    user_model.first_name = user_request.first_name
    user_model.last_name = user_request.last_name
    user_model.password = bcrypt_context.hash(user_request.password)

    db.add(user_model)
    db.commit()


@router.delete('/user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user_id: int = Path(gt=0)):
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail='User not found.')

    db.query(Users).filter(Users.id == user_id).delete()
    db.commit()
