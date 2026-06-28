# services/asistente_service.py
from sqlalchemy.orm import Session
from app.models.estudiantes import Estudiantes
from app.schemas.estudiantes import (EstudianteRequest, EstudianteResponse)
from app.core.password_security import hash_password

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
        raw_password = data.passwordEstudiante or "student123"
        asistente = Estudiantes(
            nombreEstudiante = data.nombreEstudiante,
            apellidoEstudiante = data.apellidoEstudiante,
            dniEstudiante = data.dniEstudiante,
            correoEstudiante = data.correoEstudiante,
            habilitadoEstudiante = data.habilitadoEstudiante,
            rolEstudiante = data.rolEstudiante,
            passwordEstudiante = hash_password(raw_password)
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

    def actualizar(self, id: int, data: EstudianteRequest):
        estudiante = self.db.query(Estudiantes).filter(Estudiantes.id == id).first()
        if not estudiante:
            return None
        estudiante.nombreEstudiante = data.nombreEstudiante
        estudiante.apellidoEstudiante = data.apellidoEstudiante
        estudiante.dniEstudiante = data.dniEstudiante
        estudiante.correoEstudiante = data.correoEstudiante
        estudiante.habilitadoEstudiante = data.habilitadoEstudiante
        estudiante.rolEstudiante = data.rolEstudiante
        if data.passwordEstudiante:
            estudiante.passwordEstudiante = hash_password(data.passwordEstudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante