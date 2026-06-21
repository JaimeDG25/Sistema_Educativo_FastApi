# schemas/asistente_schema.py
from pydantic import BaseModel
from enum import Enum

class RolEmpleado(str, Enum):
    ADMIN = "ADMIN"
    ASISTENTE = "ASISTENTE"

class AsistenteRequest(BaseModel):
    nombreEmpleado: str
    apellidoEmpleado: str
    dniEmpleado: str
    correoEmpleado: str
    passwordEmpleado:str
    rolesEmpleado: RolEmpleado

class AsistenteResponse(BaseModel):
    id: int
    nombreEmpleado: str
    apellidoEmpleado: str
    dniEmpleado: str
    correoEmpleado: str
    passwordEmpleado:str
    rolesEmpleado: RolEmpleado
    class Config:
        from_attributes = True