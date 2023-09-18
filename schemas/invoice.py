from pydantic import BaseModel


class InvoiceRequest(BaseModel):
    date_offisue: str
    invoice_amount: float

    class Config:
        json_scheme_extra = {
            'example': {
                'date_offisue': '2023-09-18',
                'invoice_amount': 500.00,
                'treatmentId': 1
            }
        }
