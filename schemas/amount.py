from pydantic import BaseModel


class AmountRequest(BaseModel):
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
