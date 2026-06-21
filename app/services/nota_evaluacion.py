# app/services/nota_evaluacion.py
from sqlalchemy.orm import Session
from datetime import date, datetime
from app.models.evaluacion_curso import EvaluacionCurso
from app.models.estudiantes import Estudiantes
from app.models.nota_evaluacion import NotaEvaluacion
from app.schemas.nota_evaluacion import NotaEvaluacionRequest, NotaEvaluacionResponse


class NotaEvaluacionService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        nota = self.db.query(NotaEvaluacion).all()
        return nota
    
    def crear(self, data: NotaEvaluacionRequest):
        estudiante = self.db.query(Estudiantes).filter(Estudiantes.id == data.estudianteNota).first()
        if not estudiante:
            raise Exception("El estudiante no existe")
        evaluacion = self.db.query(EvaluacionCurso).filter(EvaluacionCurso.id == data.evaluacionCuNota).first()
        if not evaluacion:
            raise Exception("El evaluacion no existe")
        nueva_nota = NotaEvaluacion(
            evaluacionCuNota = data.evaluacionCuNota,
            estudianteNota = data.estudianteNota,
            calificacionNota = data.calificacionNota,
            observacionNota = data.observacionNota
        )
        self.db.add(nueva_nota)
        self.db.commit()
        self.db.refresh(nueva_nota)
        return nueva_nota