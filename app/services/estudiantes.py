# services/asistente_service.py
from sqlalchemy.orm import Session
from app.models.estudiantes import Estudiantes
from app.schemas.estudiantes import (EstudianteRequest, EstudianteResponse)

class EstudiantesService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        asistentes = self.db.query(Estudiantes).all()
        return asistentes

    def buscarPorId(self, id:int):
        asistente_encontrado = self.db.query(Estudiantes).filter(Estudiantes.id==id).first()
        return asistente_encontrado

    def crear(self, data: EstudianteRequest):
        asistente = Estudiantes(
            nombreEstudiante = data.nombreEstudiante,
            apellidoEstudiante = data.apellidoEstudiante,
            dniEstudiante = data.dniEstudiante,
            correoEstudiante = data.correoEstudiante,
            habilitadoEstudiante = data.habilitadoEstudiante,
            rolEstudiante = data.rolEstudiante
        )
        self.db.add(asistente)
        self.db.commit()
        self.db.refresh(asistente)
        return asistente

    def eliminar(self, id: int):
        asistente = self.db.query(Estudiantes).filter(Estudiantes.id == id).first()
        if not asistente:
            return None
        self.db.delete(asistente)
        self.db.commit()
        return asistente