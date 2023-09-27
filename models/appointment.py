from config.database import Base
from sqlalchemy import Column, String, Time, Date, Integer, ForeignKey


class Appointments(Base):
    """
        Modelo de datos para representar citas médicas.

        Esta clase define la estructura de la tabla 'appointments' en la base de datos,
        que contiene información sobre las citas médicas programadas.

        Atributos:
            - id (int): Identificador único de la cita médica.
            - date (Date): Fecha de la cita médica.
            - time (Time): Hora de la cita médica.
            - description (str): Descripción o motivo de la cita médica.

        Tablas relacionadas:
            - La columna 'patientId' está relacionada con la tabla 'patients' mediante
              una clave foránea.

    """

    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    time = Column(Time)
    description = Column(String)

    patientId = Column(Integer, ForeignKey('patients.id'))
