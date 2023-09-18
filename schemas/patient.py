from pydantic import BaseModel


class PatientRequest(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    userId: int

    class Config:
        json_schema_extra = {
            'example': {
                'first_name': 'Juan',
                'last_name': 'Mendoza',
                'phone_number': '947676465',
                'address': 'AV. Principal b-8',
                'userId': 1
            }
        }
