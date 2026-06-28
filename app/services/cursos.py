# services/asistente_service.py
from sqlalchemy.orm import Session
from app.models.cursos import Cursos
from app.schemas.cursos import (CursoRequest, CursoResponse)

class CursosService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        asistentes = self.db.query(Cursos).all()
        return asistentes

    def buscarPorId(self, id:int):
        asistente_encontrado = self.db.query(Cursos).filter(Cursos.id==id).first()
        return asistente_encontrado

    def crear(self, data: CursoRequest):
        asistente = Cursos(
            nombreCurso= data.nombreCurso,
            descripcionCurso= data.descripcionCurso,
            creditosCurso=data.creditosCurso
        )
        self.db.add(asistente)
        self.db.commit()
        self.db.refresh(asistente)
        return asistente

    def eliminar(self, id: int):
        asistente = self.db.query(Cursos).filter(Cursos.id == id).first()
        if not asistente:
            return None
        self.db.delete(asistente)
        self.db.commit()
        return asistente

    def actualizar(self, id: int, data: CursoRequest):
        curso = self.db.query(Cursos).filter(Cursos.id == id).first()
        if not curso:
            return None
        curso.nombreCurso = data.nombreCurso
        curso.descripcionCurso = data.descripcionCurso
        curso.creditosCurso = data.creditosCurso
        self.db.commit()
        self.db.refresh(curso)
        return curso