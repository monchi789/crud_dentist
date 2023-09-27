from config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float


class Treatments(Base):
    """
        Modelo de datos para representar tratamientos médicos.

        Esta clase define la estructura de la tabla 'treatments' en la base de datos,
        que contiene información sobre los tratamientos médicos realizados.

        Atributos:
            - id (int): Identificador único del tratamiento.
            - treatment_name (str): Nombre del tratamiento médico.
            - description (str): Descripción detallada del tratamiento.
            - inicial_amount (float): Monto inicial del tratamiento.
            - total_amount (float): Monto total del tratamiento.

        Tablas relacionadas:
            - La columna 'patientId' está relacionada con la tabla 'patients' mediante
              una clave foránea, lo que permite vincular el tratamiento con un paciente.

    """

    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True, index=True)
    treatment_name = Column(String)
    description = Column(String)
    inicial_amount = Column(Float)
    total_amount = Column(Float)

    patientId = Column(Integer, ForeignKey('patients.id'))
