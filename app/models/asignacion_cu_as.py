# app/models/estudiantes.py
from sqlalchemy import Column, Integer, String,Date, ForeignKey
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.database.base import Base

class AsignacionCuAs(Base):
    __tablename__ = "asignacion-cu-as-table"

    id = Column(Integer,primary_key=True)
    asistenteIdAsignacionCuAs = Column(Integer, ForeignKey("asistentes-table.id"), nullable=False)
    cursoIdAsignacionCuAs = Column(Integer, ForeignKey("cursos-table.id"), nullable=False)
    fechaAsignacionCuAs = Column(Date, nullable=False)

    asistente = relationship("Asistente")
    curso = relationship("Cursos")