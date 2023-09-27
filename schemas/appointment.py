from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    """
       Modelo de datos para una solicitud de cita médica.

       Attributes:
           date (str): La fecha de la cita en formato 'YYYY-MM-DD'.
           time (str): La hora de la cita en formato 'HH:MM:SS'.
           description (str): Descripción de la cita.
           patientId (int): El ID del paciente asociado a la cita.

       Config:
           json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
           en una solicitud.
    """

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
