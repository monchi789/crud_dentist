from config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float


class Treatments(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True, index=True)
    treatment_name = Column(String)
    description = Column(String)
    inicial_amount = Column(Float)
    total_amount = Column(Float)

    patientId = Column(Integer, ForeignKey('patients.id'))
