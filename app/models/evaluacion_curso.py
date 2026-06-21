from sqlalchemy import Column, Integer, String,Date, ForeignKey, Boolean,Numeric
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.database.base import Base

class EvaluacionCurso(Base):
    __tablename__ = "evaluacion-curso-table"

    id = Column(Integer,primary_key=True)
    materialCuEvaluacion = Column(Integer, ForeignKey("material-curso-table.id"), nullable=False)
    inscripcionEsCuEvaluacion = Column(Integer, ForeignKey("inscripcion-es-cu-table.id"), nullable=False)
    tituloEvaluacion= Column(String, nullable=False)
    porcentajeEvaluacion= Column(Numeric, nullable=False)
    puntosEvaluacion= Column(Numeric, nullable=False)
    fechaSubidaEvaluacion = Column(Date, nullable=False)

    inscripcion = relationship("InscripcionEsCu")
    material = relationship("MaterialCurso")