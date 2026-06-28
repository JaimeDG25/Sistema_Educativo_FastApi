from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

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
    class Config:
        from_attributes = True

class EvaluacionCursoRequest(BaseModel):
    materialCuEvaluacion : int
    inscripcionEsCuEvaluacion : Optional[int] = None
    tituloEvaluacion : str
    porcentajeEvaluacion : float
    puntosEvaluacion : float
    fechaSubidaEvaluacion : datetime
    preguntasEvaluacion : Optional[str] = None
    semana : Optional[int] = 1

class EvaluacionCursoResponse(BaseModel):
    id : int
    materialCuEvaluacion : int
    inscripcionEsCuEvaluacion : Optional[int] = None
    tituloEvaluacion : str
    porcentajeEvaluacion : float
    puntosEvaluacion : float
    fechaSubidaEvaluacion : datetime
    preguntasEvaluacion : Optional[str] = None
    semana : Optional[int] = 1
    class Config:
        from_attributes = True