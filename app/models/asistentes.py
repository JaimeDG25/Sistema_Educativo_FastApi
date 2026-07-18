# app/models/asistente.py
from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
from app.database.base import Base
from enum import Enum

class RolEmpleado(str, Enum):
    ADMIN = "ADMIN"
    ASISTENTE = "ASISTENTE"

class Asistente(Base):
    __tablename__ = "asistentes_table"

    id = Column(Integer, primary_key=True)
    nombreEmpleado = Column(String(100), nullable=False)
    apellidoEmpleado = Column(String(100), nullable=False)
    dniEmpleado = Column(String(8), unique=True)
    correoEmpleado = Column(String(100), unique=True)
    habilitadoEmpleado = Column(Boolean, default=True)
    passwordEmpleado = Column(String(100), nullable=False)
    rolesEmpleado = Column(SqlEnum(RolEmpleado),nullable=False)

    @property
    def habilitado(self) -> bool:
        return self.habilitadoEmpleado if self.habilitadoEmpleado is not None else True

