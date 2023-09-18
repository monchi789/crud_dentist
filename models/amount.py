from config.database import Base
from sqlalchemy import Column, Integer, Date, Float, ForeignKey


class Amounts(Base):
    __tablename__ = 'amounts'

    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(Date)
    amount_payment = Column(Float)

    treatmentId = Column(Integer, ForeignKey('treatments.id'))
