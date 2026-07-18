# app/models/cursos.py
from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
from app.database.base import Base
from enum import Enum

class Cursos(Base):
    __tablename__ = "cursos_table"

    id = Column(Integer,primary_key=True)
    nombreCurso = Column(String(100), nullable=False)
    descripcionCurso = Column(String(100), nullable=False)
    creditosCurso = Column(Integer, nullable=False)