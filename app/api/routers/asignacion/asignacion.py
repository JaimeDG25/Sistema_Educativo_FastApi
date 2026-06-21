from fastapi import APIRouter,Depends
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
    return service.listar()


@router.get("/findAsignacionCuAsById/{id}", response_model=AsignacionCuAsResponse)
def get_find_asignacionCuAss_by_id(
    id: int,
    db: Session = Depends(get_db)
)->AsignacionCuAsResponse:
    service = AsignacionCuAsService(db)
    return service.buscarPorId(id)


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
