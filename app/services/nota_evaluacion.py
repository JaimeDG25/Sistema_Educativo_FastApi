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
            
        # Regla de negocio para gamificacion:
        # Semana 1 inicio: Lunes 23 de Marzo del 2026
        from datetime import date
        start_date = date(2026, 3, 23)
        today = date.today()
        diff_days = (today - start_date).days
        current_week = (diff_days // 7) + 1
        current_week = min(max(1, current_week), 18)
        
        eval_semana = evaluacion.semana if evaluacion.semana is not None else 1
        
        if eval_semana < current_week:
            # Semana pasada / Vencida -> x0 puntos
            multiplicador = 0.0
        else:
            # Semana actual o futura. Lunes (0) a Jueves (3) -> x1.5, Viernes (4) a Domingo (6) -> x1.0
            if today.weekday() <= 3:
                multiplicador = 1.5
            else:
                multiplicador = 1.0
                
        puntos_otorgados = int(round(data.calificacionNota * multiplicador))
        
        if estudiante.puntos is None:
            estudiante.puntos = 0
        estudiante.puntos += puntos_otorgados
        
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