from sqlalchemy import Column, Integer, String,Date, ForeignKey, Boolean
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.database.base import Base

class InscripcionEsCu(Base):
    __tablename__ = "inscripcion-es-cu-table"

    id = Column(Integer,primary_key=True)
    estudianteIdInscripcion = Column(Integer, ForeignKey("estudiante-table.id"), nullable=False)
    asignacionIdInscripcion = Column(Integer, ForeignKey("asignacion-cu-as-table.id"), nullable=False)
    totalPuntosInscripcion = Column(Integer, nullable=False)
    fechaInscripcion = Column(Date, nullable=False)

    estudiante = relationship("Estudiantes")
    asignacion = relationship("AsignacionCuAs")