from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException
from app.models.asistentes import Asistente
from app.models.estudiantes import Estudiantes
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
            or_(Asistente.dniEmpleado == data.dni, Asistente.correoEmpleado == data.dni)
        ).first()
        
        if usuario:
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

        # Fallback: buscar en estudiantes
        estudiante = self.db.query(
            Estudiantes
        ).filter(
            or_(Estudiantes.dniEstudiante == data.dni, Estudiantes.correoEstudiante == data.dni)
        ).first()

        if not estudiante:
            raise HTTPException(
                status_code=401,
                detail="Usuario no encontrado"
            )
        print("Password ingresada:", data.password)
        print("Password almacenada:", estudiante.passwordEstudiante)
        print("Tipo:", type(estudiante.passwordEstudiante))
        if not estudiante.passwordEstudiante or not verify_password(
            data.password,
            estudiante.passwordEstudiante
        ):
            raise HTTPException(
                status_code=401,
                detail="Contraseña incorrecta"
            )

        token = create_access_token(
            {
                "id": estudiante.id,
                "dni": estudiante.dniEstudiante,
                "rol": estudiante.rolEstudiante
            }
        )
        return {
            "access_token": token,
            "token_type": "bearer"
        }