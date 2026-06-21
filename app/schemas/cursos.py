# app/schemas/cursos.py

from pydantic import BaseModel

class CursoRequest(BaseModel):
    nombreCurso:str
    descripcionCurso: str
    creditosCurso: int

class CursoResponse(BaseModel):
    id:int
    nombreCurso:str
    descripcionCurso: str
    creditosCurso: int
    class Config:
        from_attributes = True
