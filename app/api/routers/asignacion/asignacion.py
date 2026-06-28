from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import List, Optional, Union
from app.services.asignacion_cu_as import AsignacionCuAsService
from app.schemas.asignacion_cu_as import AsignacionCuAsRequest,AsignacionCuAsResponse
import pandas as pd
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/asignacionCuAs" , tags=["ASIGNACION_CU_AS"])

@router.get("/listAsignacionCuAs", response_model=list[AsignacionCuAsResponse])
def get_list_asignacionCuAss(
    db: Session = Depends(get_db)
):
    service = AsignacionCuAsService(db)
    asignaciones = service.listar()
    return [a for a in asignaciones if a.curso is not None]


@router.get("/findAsignacionCuAsById/{id}", response_model=AsignacionCuAsResponse)
def get_find_asignacionCuAss_by_id(
    id: int,
    db: Session = Depends(get_db)
)->AsignacionCuAsResponse:
    service = AsignacionCuAsService(db)
    asignacion = service.buscarPorId(id)
    if not asignacion or asignacion.curso is None:
        raise HTTPException(status_code=404, detail="Asignacion no encontrada o curso inexistente")
    return asignacion


@router.post("/addAsignacionCuAs", response_model=AsignacionCuAsResponse)
def post_add_asignacion_cu_as(
    data: AsignacionCuAsRequest,
    db: Session = Depends(get_db)
)->AsignacionCuAsResponse:
    service = AsignacionCuAsService(db)
    return service.crear(data)


@router.delete("/deleteAsignacionCuAs", response_model=AsignacionCuAsResponse)
def delete_eliminate_asignacion_cu_as(
    id: int,
    db: Session = Depends(get_db)
):
    service = AsignacionCuAsService(db)
    return service.eliminar(id)
