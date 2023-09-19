from pydantic import BaseModel


class TreatmentRequest(BaseModel):
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
