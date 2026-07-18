from pydantic import BaseModel,SecretStr

class LoginRequest(BaseModel):
    dni: str
    password: str