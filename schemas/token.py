from pydantic import BaseModel


class Token(BaseModel):
    """
       Modelo de datos para representar un token de acceso.

       Attributes:
           access_token (str): El token de acceso generado.
           token_type (str): El tipo de token (generalmente 'bearer').

       Note:
           Un token de acceso es utilizado para autenticar y autorizar las solicitudes al sistema.

    """

    access_token: str
    token_type: str
