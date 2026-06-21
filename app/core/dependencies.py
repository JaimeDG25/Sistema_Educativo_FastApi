# app/core/dependencies.py

from jose import jwt
from jose import JWTError
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security

from app.core.jwt_security import (
    SECRET_KEY,
    ALGORITHM
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login/login"
)

http_bearer = HTTPBearer()
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(http_bearer)
):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )
def require_admin(
    current_user=Depends(get_current_user)
):

    if current_user["rol"] != "ADMIN":

        raise HTTPException(
            status_code=403,
            detail="No tienes permisos"
        )

    return current_user