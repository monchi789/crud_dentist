from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
