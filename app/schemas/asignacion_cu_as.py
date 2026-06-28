from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class AsistenteResponse(BaseModel):
    id: int
    nombreEmpleado: str
    apellidoEmpleado: str
    dniEmpleado: str
    correoEmpleado: str
    class Config:
        from_attributes = True

class CursoResponse(BaseModel):
    id: int
    nombreCurso: str
    descripcionCurso: str
    creditosCurso: int
    class Config:
        from_attributes = True


class AsignacionCuAsRequest(BaseModel):
    asistenteIdAsignacionCuAs : int 
    cursoIdAsignacionCuAs : int

class AsignacionCuAsResponse(BaseModel):
    id : int
    asistenteIdAsignacionCuAs: int
    asistente: Optional[AsistenteResponse] = None
    cursoIdAsignacionCuAs: int
    curso: Optional[CursoResponse] = None
    fechaAsignacionCuAs :datetime
    class Config:
        from_attributes = True
