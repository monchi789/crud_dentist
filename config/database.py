from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from typing import Annotated

# URL de la base de datos
SQL_ALCHEMY_DATABSE_URL = 'postgresql+psycopg2://monchi789:1234@127.0.0.1:5432/crud_dentist'

# Crear el motor de la base de datos
engine = create_engine(SQL_ALCHEMY_DATABSE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base de datos para definir modelos
Base = declarative_base()


def get_db():
    """
        Función para obtener una instancia de la base de datos.

        Returns:
            Session: Una sesión de base de datos.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Anotación para definir una dependencia de base de datos
db_dependency = Annotated[Session, Depends(get_db)]
