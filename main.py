from fastapi import FastAPI
from models.user import Base
from models.patient import Base
from models.appointment import Base
from models.amount import Base
from models.treatment import Base
from models.invoice import Base
from config.database import engine
from routes import user, patient, amount, appointment, invoice, treatment, token

# Crear una instancia de FastAPI
app = FastAPI()

# Crear las tablas en la base de datos usando SQLAlchemy y los modelos Base correspondientes
# Esto asegura que las tablas se creen según la definición de modelos en SQLAlchemy
Base.metadata.create_all(bind=engine)

# Incluir todas las rutas definidas en tus módulos de rutas en tu aplicación FastAPI
app.include_router(user.router)
app.include_router(patient.router)
app.include_router(amount.router)
app.include_router(appointment.router)
app.include_router(invoice.router)
app.include_router(treatment.router)
app.include_router(token.router)
