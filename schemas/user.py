from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    """
        Modelo de datos para una solicitud de creación de usuario.

        Attributes:
            username (str): El nombre de usuario del usuario.
            email (str): El correo electrónico del usuario.
            phone_number (str): El número de teléfono del usuario.
            first_name (str): El primer nombre del usuario.
            last_name (str): El apellido del usuario.
            password (str): La contraseña del usuario (debe tener al menos 3 caracteres).

        Config:
            json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
            en una solicitud.

    """

    username: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str = Field(min_length=3)

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'monchi789',
                'email': 'monchi@example.com',
                'phone_number': '987675645',
                'first_name': 'Cristian',
                'last_name': 'Monzon Guzman',
                'password': '7686824'
            }
        }
