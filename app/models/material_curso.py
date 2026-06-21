# app/models/estudiantes.py
from sqlalchemy import Column, Integer, String,Date, ForeignKey, Boolean
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.database.base import Base

class MaterialCurso(Base):
    __tablename__ = "material-curso-table"

    id = Column(Integer,primary_key=True)
    asignacionCuAsIdMaterial = Column(Integer, ForeignKey("asignacion-cu-as-table.id"), nullable=False)
    tituloMaterial = Column(String, nullable=False)
    descripcionMaterial = Column(String, nullable=False)
    tipoMaterial = Column(String, nullable=False)
    estadoMaterial = Column(Boolean, nullable=False)
    urlMaterial = Column(String, nullable=False)
    fechaSubidaMaterial = Column(Date, nullable=False)

    asignacion = relationship("AsignacionCuAs")
