from pydantic import BaseModel
from datetime import date, datetime

class EstudianteResponse(BaseModel):
    id : int
    nombreEstudiante : str
    apellidoEstudiante : str 
    dniEstudiante : str
    correoEstudiante : str
    habilitadoEstudiante : bool
    rolEstudiante : str
    class Config:
        from_attributes = True

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

class InscripcionEsCuRequest(BaseModel):
    estudianteIdInscripcion : int
    asignacionIdInscripcion : int
    totalPuntosInscripcion : int
    fechaInscripcion : datetime

class InscripcionEsCuResponse(BaseModel):
    id : int
    estudianteIdInscripcion : int
    estudiante : EstudianteResponse
    asignacionIdInscripcion : int
    asignacion : AsignacionCuAsResponse
    totalPuntosInscripcion : int
    fechaInscripcion : datetime
    class Config:
        from_attributes = True
