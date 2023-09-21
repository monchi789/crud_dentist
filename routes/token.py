from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends
from models.user import Users
from config.database import db_dependency
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Token']
)


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filters(Users.username == username)


@router.post('/token')
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    return form_data.username
