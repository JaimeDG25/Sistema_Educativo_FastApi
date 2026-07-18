# app/api/routers/asistentes/asistentes.py
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import List, Optional, Union
from app.services.asistentes import AsistenteService
from app.schemas.asistentes import AsistenteRequest,AsistenteResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.core.dependencies import require_admin, get_current_user
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
    current_user=Depends(get_current_user)
)->AsistenteResponse:
    if current_user.get("rol") != "ADMIN" and current_user.get("id") != id:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver este perfil")
        
    service = AsistenteService(db)
    asistente = service.buscarPorId(id)
    if not asistente:
        raise HTTPException(status_code=404, detail="Asistente no encontrado")
    return asistente


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


@router.put("/updateAsistentes/{id}", response_model=AsistenteResponse)
def put_update_asistente(
    id: int,
    data: AsistenteRequest,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
)-> AsistenteResponse:
    service = AsistenteService(db)
    asistente = service.actualizar(id, data)
    if not asistente:
        raise HTTPException(status_code=404, detail="Asistente no encontrado")
    return asistente
