# app/api/routers/login/login.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.login import LoginRequest
from app.services.login import LoginService

router = APIRouter(
    prefix="/login",
    tags=["LOGIN"]
)

@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    print("INCOMING LOGIN REQUEST:", data.dict())
    service = LoginService(db)
    return service.login(data)