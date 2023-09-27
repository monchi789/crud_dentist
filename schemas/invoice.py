from pydantic import BaseModel


class InvoiceRequest(BaseModel):
    """
        Modelo de datos para una solicitud de factura médica.

        Attributes:
            date_offisue (str): La fecha de emisión de la factura en formato 'YYYY-MM-DD'.
            invoice_amount (float): La cantidad de la factura.
            treatmentId (int): El ID del tratamiento médico asociado a la factura.

        Config:
            json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
            en una solicitud.
    """

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
