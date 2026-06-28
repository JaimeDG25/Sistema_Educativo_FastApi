# schemas/asistente_schema.py
from pydantic import BaseModel
from enum import Enum

from typing import Optional

class RolEmpleado(str, Enum):
    ADMIN = "ADMIN"
    ASISTENTE = "ASISTENTE"

class AsistenteRequest(BaseModel):
    nombreEmpleado: str
    apellidoEmpleado: str
    dniEmpleado: str
    correoEmpleado: str
    passwordEmpleado: str
    rolesEmpleado: RolEmpleado
    habilitadoEmpleado: Optional[bool] = True

class AsistenteResponse(BaseModel):
    id: int
    nombreEmpleado: str
    apellidoEmpleado: str
    dniEmpleado: str
    correoEmpleado: str
    passwordEmpleado: str
    rolesEmpleado: RolEmpleado
    habilitadoEmpleado: bool
    habilitado: bool
    class Config:
        from_attributes = True