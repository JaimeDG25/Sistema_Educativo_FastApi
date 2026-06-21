from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.asistentes import Asistente
from app.schemas.login import LoginRequest
from app.core.password_security import verify_password
from app.core.jwt_security import create_access_token


class LoginService:
    def __init__(self, db: Session):
        self.db = db
    def login(self, data: LoginRequest):
        usuario = self.db.query(
            Asistente
        ).filter(
            Asistente.dniEmpleado == data.dni
        ).first()
        if not usuario:
            raise HTTPException(
                status_code=401,
                detail="Usuario no encontrado"
            )
        if not verify_password(
            data.password,
            usuario.passwordEmpleado
        ):
            raise HTTPException(
                status_code=401,
                detail="Contraseña incorrecta"
            )
        token = create_access_token(
            {
                "id": usuario.id,
                "dni": usuario.dniEmpleado,
                "rol": usuario.rolesEmpleado.value
            }
        )
        return {
            "access_token": token,
            "token_type": "bearer"
        }