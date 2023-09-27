from pydantic import BaseModel


class AmountRequest(BaseModel):
    """
        Modelo de datos para una solicitud de pago asociado a tratamientos médicos.

        Attributes:
            payment_date (str): La fecha del pago en formato 'YYYY-MM-DD'.
            amount_payment (float): La cantidad del pago.
            treatmentId (int): El ID del tratamiento médico asociado al pago.

        Config:
            json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
            en una solicitud.
    """

    payment_date: str
    amount_payment: float
    treatmentId: int

    class Config:
        json_schema_extra = {
            'example': {
                'payment_date': '2023-09-18',
                'amount_payment': 100.00,
                'treatmentId': 1
            }
        }
