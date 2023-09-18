from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    username: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str = Field(min_length=3)

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'monchi789',
                'email': 'monchi@example.com',
                'phone_number': '987675645',
                'first_name': 'Cristian',
                'last_name': 'Monzon Guzman',
                'password': '7686824'
            }
        }
