from pydantic import BaseModel

class EstudianteRequest(BaseModel):
    nombreEstudiante : str
    apellidoEstudiante : str 
    dniEstudiante : str
    correoEstudiante : str
    habilitadoEstudiante : bool
    rolEstudiante : str

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