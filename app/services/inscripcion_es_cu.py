# app/services/inscripcion_es_cu.py
from sqlalchemy.orm import Session
from datetime import date, datetime
from typing import Optional
from app.models.estudiantes import Estudiantes
from app.models.asignacion_cu_as import AsignacionCuAs
from app.models.inscripcion_es_cu import InscripcionEsCu
from app.schemas.inscripcion_es_cu import InscripcionEsCuRequest,InscripcionEsCuResponse


class InscripcionEsCuService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self, estudiante_id: Optional[int] = None):
        from sqlalchemy.orm import joinedload
        query = self.db.query(InscripcionEsCu).options(
            joinedload(InscripcionEsCu.estudiante),
            joinedload(InscripcionEsCu.asignacion).joinedload(AsignacionCuAs.curso)
        )
        if estudiante_id is not None:
            query = query.filter(InscripcionEsCu.estudianteIdInscripcion == estudiante_id)
        return query.all()
    
    def crear(self, data: InscripcionEsCuRequest):
        estudiante = self.db.query(Estudiantes).filter(Estudiantes.id == data.estudianteIdInscripcion).first()
        if not estudiante:
            raise Exception("El estudiante no existe")
        asignacion = self.db.query(AsignacionCuAs).filter(AsignacionCuAs.id == data.asignacionIdInscripcion).first()
        if not asignacion:
            raise Exception("La asignacion no existe")
        nueva_inscripcion = InscripcionEsCu(
            estudianteIdInscripcion= data.estudianteIdInscripcion,
            asignacionIdInscripcion= data.asignacionIdInscripcion,
            totalPuntosInscripcion= data.totalPuntosInscripcion,
            fechaInscripcion= date.today()
        )
        self.db.add(nueva_inscripcion)
        self.db.commit()
        self.db.refresh(nueva_inscripcion)
        return nueva_inscripcion