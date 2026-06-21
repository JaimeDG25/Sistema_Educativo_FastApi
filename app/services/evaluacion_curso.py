# app/services/inscripcion_es_cu.py
from sqlalchemy.orm import Session
from datetime import date, datetime
from app.models.evaluacion_curso import EvaluacionCurso
from app.models.material_curso import MaterialCurso
from app.models.inscripcion_es_cu import InscripcionEsCu
from app.schemas.evaluacion_curso import EvaluacionCursoRequest,EvaluacionCursoResponse


class EvaluacionCursoService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        evaluacion = self.db.query(EvaluacionCurso).all()
        return evaluacion
    
    def crear(self, data: EvaluacionCursoRequest):
        inscripcion = self.db.query(InscripcionEsCu).filter(InscripcionEsCu.id == data.inscripcionEsCuEvaluacion).first()
        if not inscripcion:
            raise Exception("La inscripcion no existe")
        material = self.db.query(MaterialCurso).filter(MaterialCurso.id == data.materialCuEvaluacion).first()
        if not material:
            raise Exception("El material no existe")
        nueva_evaluacion = EvaluacionCurso(
            materialCuEvaluacion = data.materialCuEvaluacion,
            inscripcionEsCuEvaluacion = data.inscripcionEsCuEvaluacion,
            tituloEvaluacion = data.tituloEvaluacion,
            porcentajeEvaluacion = data.porcentajeEvaluacion,
            puntosEvaluacion = data.puntosEvaluacion,
            fechaSubidaEvaluacion = date.today()
        )
        self.db.add(nueva_evaluacion)
        self.db.commit()
        self.db.refresh(nueva_evaluacion)
        return nueva_evaluacion