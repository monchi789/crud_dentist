from pydantic import BaseModel


class InvoiceRequest(BaseModel):
    date_offisue: str
    invoice_amount: float
    treatmentId: int

    class Config:
        json_schema_extra = {
            'example': {
                'date_offisue': '2023-09-18',
                'invoice_amount': 110.00,
                'treatmentId': 1
            }
        }
