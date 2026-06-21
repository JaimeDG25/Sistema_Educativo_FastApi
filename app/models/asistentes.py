# app/models/asistente.py
from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
from app.database.base import Base
from enum import Enum

class RolEmpleado(str, Enum):
    ADMIN = "ADMIN"
    ASISTENTE = "ASISTENTE"

class Asistente(Base):
    __tablename__ = "asistentes-table"

    id = Column(Integer, primary_key=True)
    nombreEmpleado = Column(String)
    apellidoEmpleado = Column(String)
    dniEmpleado = Column(String(8), unique=True)
    correoEmpleado = Column(String(50), unique=True)
    habilitadoEmpleado = Column(Boolean, default=True)
    passwordEmpleado = Column(String, nullable=False)
    rolesEmpleado = Column(SqlEnum(RolEmpleado),nullable=False)

