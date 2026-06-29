from pydantic import BaseModel
from typing import Optional

class EstudianteRequest(BaseModel):
    nombreEstudiante : str
    apellidoEstudiante : str 
    dniEstudiante : str
    correoEstudiante : str
    habilitadoEstudiante : bool
    rolEstudiante : str
    passwordEstudiante : Optional[str] = None
    puntos : Optional[int] = 0

class EstudianteResponse(BaseModel):
    id : int
    nombreEstudiante : str
    apellidoEstudiante : str 
    dniEstudiante : str
    correoEstudiante : str
    habilitadoEstudiante : bool
    rolEstudiante : str
    passwordEstudiante : Optional[str] = None
    puntos : int = 0
    points : int = 0
    class Config:
        from_attributes = True