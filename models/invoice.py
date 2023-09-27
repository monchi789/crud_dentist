from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Float


class Invoices(Base):
    """
        Modelo de datos para representar facturas asociadas a tratamientos médicos.

        Esta clase define la estructura de la tabla 'invoices' en la base de datos,
        que contiene información sobre las facturas generadas por tratamientos médicos.

        Atributos:
            - id (int): Identificador único de la factura.
            - date_issue (Date): Fecha de emisión de la factura.
            - invoice_amount (float): Monto total de la factura.

        Tablas relacionadas:
            - La columna 'treatmentId' está relacionada con la tabla 'treatments' mediante
              una clave foránea.

    """

    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    date_offisue = Column(Date)
    invoice_amount = Column(Float)

    treatmentId = Column(Integer, ForeignKey('treatments.id'))
