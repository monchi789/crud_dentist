from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    date: str
    time: str
    description: str
    patientId: int

    class Config:
        json_schema_extra = {
            'example': {
                'date': '2018-08-18',
                'time': '14:30:00',
                'description': 'Cita 1',
                'patientId': 1
            }
        }
