# app/models/estudiantes.py
from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
from app.database.base import Base
from enum import Enum

class Estudiantes(Base):
    __tablename__ = "estudiante-table"

    id = Column(Integer,primary_key=True)
    nombreEstudiante = Column(String, nullable=False)
    apellidoEstudiante = Column(String, nullable=False)
    dniEstudiante = Column(String(8), nullable=False)
    correoEstudiante = Column(String(50), nullable=False)
    habilitadoEstudiante = Column(Boolean, default=True)
    rolEstudiante = Column(String,nullable=False)
    passwordEstudiante = Column(String, nullable=True)
    puntos = Column(Integer, default=0, nullable=False)

    @property
    def points(self) -> int:
        return self.puntos if self.puntos is not None else 0