from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Float


class Invoices(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    date_offisue = Column(Date)
    invoice_amount = Column(Float)

    treatmentId = Column(Integer, ForeignKey('treatments.id'))
