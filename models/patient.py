from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Patients(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    address = Column(String)

    userId = Column(Integer, ForeignKey('users.id'))
