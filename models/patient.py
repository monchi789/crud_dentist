from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Patients(Base):
    """
        Modelo de datos para representar información de pacientes.

        Esta clase define la estructura de la tabla 'patients' en la base de datos,
        que contiene información detallada sobre los pacientes atendidos.

        Atributos:
            - id (int): Identificador único del paciente.
            - first_name (str): Nombre del paciente.
            - last_name (str): Apellido del paciente.
            - phone_number (str): Número de teléfono del paciente.
            - address (str): Dirección del paciente.

        Tablas relacionadas:
            - La columna 'userId' está relacionada con la tabla 'users' mediante
              una clave foránea, lo que permite vincular al paciente con un usuario.

    """

    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    address = Column(String)

    userId = Column(Integer, ForeignKey('users.id'))
