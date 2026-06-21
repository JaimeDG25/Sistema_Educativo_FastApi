from sqlalchemy import Column, Integer, String,Date, ForeignKey, Boolean, Numeric
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.database.base import Base

class NotaEvaluacion(Base):
    __tablename__ = "nota-evaluacion-table"

    id = Column(Integer,primary_key=True)
    evaluacionCuNota = Column(Integer, ForeignKey("estudiante-table.id"), nullable=False)
    estudianteNota = Column(Integer, ForeignKey("evaluacion-curso-table.id"), nullable=False)
    calificacionNota= Column(Numeric, nullable=False)
    observacionNota= Column(Integer, nullable=False)

    estudiante = relationship("Estudiantes")
    nota = relationship("EvaluacionCurso")