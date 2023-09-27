from pydantic import BaseModel


class TreatmentRequest(BaseModel):
    """
        Modelo de datos para una solicitud de tratamiento médico.

        Attributes:
            treatment_name (str): El nombre del tratamiento médico.
            description (str): La descripción del tratamiento médico.
            inicial_amount (float): El monto inicial del tratamiento médico.
            total_amount (float): El monto total del tratamiento médico.
            patientId (int): El ID del paciente asociado al tratamiento médico.

        Config:
            json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
            en una solicitud.
    """

    treatment_name: str
    description: str
    inicial_amount: float
    total_amount: float
    patientId: int

    class Config:
        json_schema_extra = {
            'example': {
                'treatment_name': 'Ortodoncia',
                'description': 'Lorem Ipsum is simply dummy text',
                'inicial_amount': 453.12,
                'total_amount': 800.00,
                'patientId': 1
            }
        }
