# services/asistente_service.py
from sqlalchemy.orm import Session
from app.core.password_security import hash_password
from app.models.asistentes import Asistente
from app.schemas.asistentes import (AsistenteRequest, AsistenteResponse)

class AsistenteService:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        asistentes = self.db.query(Asistente).all()
        return asistentes

    def buscarPorId(self, id:int):
        asistente_encontrado = self.db.query(Asistente).filter(Asistente.id==id).first()
        return asistente_encontrado

    def crear(self, data: AsistenteRequest):
        asistente = Asistente(
            nombreEmpleado= data.nombreEmpleado,
            apellidoEmpleado= data.apellidoEmpleado,
            dniEmpleado=data.dniEmpleado,
            correoEmpleado=data.correoEmpleado,
            passwordEmpleado = hash_password(data.passwordEmpleado),
            rolesEmpleado=data.rolesEmpleado
        )
        self.db.add(asistente)
        self.db.commit()
        self.db.refresh(asistente)
        return asistente

    def eliminar(self, id: int):
        asistente = self.db.query(Asistente).filter(Asistente.id == id).first()
        if not asistente:
            return None
        self.db.delete(asistente)
        self.db.commit()
        return asistente