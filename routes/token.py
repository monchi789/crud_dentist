from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends
from models.user import Users
from config.database import db_dependency
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from schemas.token import Token
from starlette.exceptions import HTTPException
from starlette import status
from jose import jwt, JWTError


router = APIRouter(
    tags=['Token']
)

SECRET_KEY = 'f073e065227f7e169fe0182b9beaabf81588d8b204e47ed64aa6dfef31e5daa8'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_toke(username: str, user_id: int, expires_delta: timedelta):
    enconde = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    enconde.update({'exp': expires})
    return jwt.encode(enconde, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')

        return {'username': username, 'id': user_id}

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')


@router.post('/token', response_model=Token, status_code=status.HTTP_201_CREATED)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
    token = create_access_toke(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}
