from fastapi import FastAPI
from models.user import Base
from models.patient import Base
from models.appointment import Base
from models.amount import Base
from models.treatment import Base
from models.invoice import Base
from config.database import engine
from routes import user, patient, amount, appointment, invoice, treatment

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(patient.router)
app.include_router(amount.router)
app.include_router(appointment.router)
app.include_router(invoice.router)
app.include_router(treatment.router)
