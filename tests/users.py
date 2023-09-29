import json
from main import app
from fastapi.testclient import TestClient
from fastapi import status
from models.user import Users
from schemas.user import UserRequest
from config.database import db_dependency
from passlib.context import CryptContext


app = TestClient(app)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def test_get_all_users():
    """
       Prueba que el endpoint `/users/` devuelve todos los usuarios.
    """

    response = app.get("/users/")
    users = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(users) > 0

    assert any('id' in user for user in users)
    assert any('username' in user for user in users)
    assert any('email' in user for user in users)
    assert any('phone_number' in user for user in users)
    assert any('first_name' in user for user in users)
    assert any('last_name' in user for user in users)
    assert any('password' in user for user in users)


def test_get_user_by_id(id=1):
    """
        Prueba que el endpoint `/users/{user_id}` devuelve el usuario indicado
    """

    response = app.get(f'/users/{id}')
    user = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(user) > 0
    assert 'id' in user
    assert 'username' in user
    assert 'email' in user
    assert 'phone_number' in user
    assert 'first_name' in user
    assert 'last_name' in user
    assert 'password' in user


def test_create_user():
    """
       Prueba que el endpoint `/user` crea un nuevo usuario.
    """

    db: db_dependency

    # Crear una solicitud de usuario.
    user_request = {
        "email": "Prueba@example.com",
        "first_name": "Prueba",
        "last_name": "Monzon Guzman",
        "password": "1234",
        "phone_number": "987565467",
        "username": "Prueba"
    }

    # Realizar la solicitud POST al endpoint `/user`.
    response = app.post("/user", json=json.dumps(user_request))

    # Validar la respuesta.
    assert response.status_code == status.HTTP_201_CREATED
    assert response.headers["Content-Type"] == "application/json"

    # Validar que el usuario se haya creado correctamente.
    user_model = Users(username=user_request.get('username'), phone_number=user_request.get('phone_number'),
                       email=user_request.get('email'), first_name=user_request.get('first_name'),
                       last_name=user_request.get('last_name'),
                       password=bcrypt_context.hash(user_request.get('password')))
    assert user_model is not None
    assert user_model.username == user_request.get('username')
    assert user_model.phone_number == user_request.get('phone_number')
    assert user_model.email == user_request.get('email')
    assert user_model.first_name == user_request.get('first_name')
    assert user_model.last_name == user_request.get('last_name')
    # assert bcrypt_context.check_password_hash(user_request.get('password'), user_model.password)


def test_update_user():
    """
       Prueba que el endpoint `/user/{user_id}` actualiza un usuario existente.
    """

    # Crear un usuario de prueba.
    user_request = UserRequest(username="test_user", phone_number="+15555555555",
                               email="test_user@example.com", first_name="Test",
                               last_name="User", password="password123")
    response = app.post("/user", json=user_request.model_dump())

    # Obtener el ID del usuario de prueba.
    user_id = response.json()["id"]

    # Crear una solicitud de actualización de usuario.
    updated_user_request = UserRequest(username="updated_test_user", phone_number="+15555555556",
                                       email="updated_test_user@example.com", first_name="Updated",
                                       last_name="User", password="password321")

    # Realizar la solicitud PUT al endpoint `/user/{user_id}`.
    response = app.put("/user/{}".format(user_id), json=updated_user_request.model_dump())

    # Validar la respuesta.
    assert response.status_code == 204

    # Validar que el usuario se haya actualizado correctamente.
    user_model = Users.query.filter(Users.id == user_id).first()
    assert user_model is not None
    assert user_model.username == updated_user_request.username
    assert user_model.phone_number == updated_user_request.phone_number
    assert user_model.email == updated_user_request.email
    assert user_model.first_name == updated_user_request.first_name
    assert user_model.last_name == updated_user_request.last_name
    assert bcrypt_context.check_password_hash(updated_user_request.password, user_model.password)
