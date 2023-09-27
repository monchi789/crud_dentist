from config.database import Base
from sqlalchemy import Column, Integer, Date, Float, ForeignKey


class Amounts(Base):
    """
        Modelo de datos para representar pagos asociados a tratamientos médicos.

        Esta clase define la estructura de la tabla 'amounts' en la base de datos,
        que contiene información sobre los pagos realizados por tratamientos médicos.

        Atributos:
            - id (int): Identificador único del pago.
            - payment_date (Date): Fecha en la que se realizó el pago.
            - amount_payment (float): Monto del pago realizado.
            - treatmentId (int): Clave foránea que hace referencia al tratamiento médico asociado.

        Tablas relacionadas:
            - La columna 'treatmentId' está relacionada con la tabla 'treatments' mediante
              una clave foránea.

    """

    __tablename__ = 'amounts'

    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(Date)
    amount_payment = Column(Float)

    treatmentId = Column(Integer, ForeignKey('treatments.id'))
