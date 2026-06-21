# app/api/routers/asistentes/asistentes.py
from fastapi import APIRouter,Depends
from datetime import datetime
from typing import List, Optional, Union
from app.services.asistentes import AsistenteService
from app.schemas.asistentes import AsistenteRequest,AsistenteResponse
import pandas as pd
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.core.dependencies import require_admin
router= APIRouter(prefix="/asistentes" , tags=["ASISTENTES"])

@router.get("/listAsistentes", response_model=list[AsistenteResponse])
def get_list_asistentes(
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):
    service = AsistenteService(db)
    return service.listar()


@router.get("/findAsistentesById/{id}", response_model=AsistenteResponse)
def get_find_asistentes_by_id(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
)->AsistenteResponse:
    service = AsistenteService(db)
    return service.buscarPorId(id)


@router.post("/addAsistentes", response_model=AsistenteResponse)
def post_add_asistente(
    data: AsistenteRequest,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
)->AsistenteResponse:
    service = AsistenteService(db)
    return service.crear(data)


@router.delete("/deleteAsistentes", response_model=AsistenteResponse)
def delete_eliminate_asistente(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):
    service = AsistenteService(db)
    return service.eliminar(id)
