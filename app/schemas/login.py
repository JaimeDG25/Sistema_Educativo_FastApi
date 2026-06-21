from pydantic import BaseModel

class LoginRequest(BaseModel):
    dni: str
    password: str