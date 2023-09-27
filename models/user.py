from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Users(Base):
    """
        Modelo de datos para representar usuarios.

        Esta clase define la estructura de la tabla 'users' en la base de datos,
        que contiene información sobre los usuarios del sistema.

        Atributos:
            - id (int): Identificador único del usuario.
            - username (str): Nombre de usuario único.
            - email (str): Dirección de correo electrónico única.
            - phone_number (str): Número de teléfono único.
            - first_name (str): Nombre del usuario.
            - last_name (str): Apellido del usuario.
            - password (str): Contraseña del usuario (se recomienda el almacenamiento seguro).

    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
