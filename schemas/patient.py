from pydantic import BaseModel


class PatientRequest(BaseModel):
    """
        Modelo de datos para una solicitud de paciente.

        Attributes:
            first_name (str): El nombre del paciente.
            last_name (str): El apellido del paciente.
            phone_number (str): El número de teléfono del paciente.
            address (str): La dirección del paciente.
            userId (int): El ID del usuario asociado al paciente.

        Config:
            json_schema_extra (dict): Un ejemplo de datos en formato JSON que ilustra la estructura esperada
            en una solicitud.
    """

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
