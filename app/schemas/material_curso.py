from pydantic import BaseModel
from datetime import date, datetime

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

class AsignacionCuAsResponse(BaseModel):
    id : int
    asistenteIdAsignacionCuAs: int
    asistente: AsistenteResponse
    cursoIdAsignacionCuAs: int
    curso: CursoResponse
    fechaAsignacionCuAs :datetime
    class Config:
        from_attributes = True

class MaterialCursoRequest(BaseModel):
    asignacionCuAsIdMaterial : int
    tituloMaterial : str
    descripcionMaterial : str
    tipoMaterial : str
    estadoMaterial : bool
    urlMaterial : str
    fechaSubidaMaterial : datetime

class MaterialCursoResponse(BaseModel):
    id : int
    asignacionCuAsIdMaterial : int
    asignacion: AsignacionCuAsResponse
    tituloMaterial : str
    descripcionMaterial : str
    tipoMaterial : str
    estadoMaterial : bool
    urlMaterial : str
    fechaSubidaMaterial : datetime