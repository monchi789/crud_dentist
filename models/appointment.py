from config.database import Base
from sqlalchemy import Column, String, Time, Date, Integer, ForeignKey


class Appointments(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    time = Column(Time)
    description = Column(String)

    patientId = Column(Integer, ForeignKey('patients.id'))
