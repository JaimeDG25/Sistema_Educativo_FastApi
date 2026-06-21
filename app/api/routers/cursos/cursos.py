# app/api/routers/cursos/cursos.py

from fastapi import APIRouter,Depends
from datetime import datetime
from typing import List, Optional, Union
from app.services.cursos import CursosService
from app.schemas.cursos import CursoRequest, CursoResponse
import pandas as pd
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/cursos" , tags=["CURSOS"])

@router.get("/listCursos", response_model=list[CursoResponse])
def get_list_cursos(
    db: Session = Depends(get_db)
):
    service = CursosService(db)
    return service.listar()


@router.get("/findCursoById/{id}", response_model=CursoResponse)
def get_find_curso_by_id(
    id: int,
    db: Session = Depends(get_db)
)->CursoResponse:
    service = CursosService(db)
    return service.buscarPorId(id)


@router.post("/addCurso", response_model=CursoResponse)
def post_add_curso(
    data: CursoRequest,
    db: Session = Depends(get_db)
)->CursoResponse:
    service = CursosService(db)
    return service.crear(data)


@router.delete("/deleteCurso", response_model=CursoResponse)
def delete_eliminate_curso(
    id: int,
    db: Session = Depends(get_db)
):
    service = CursosService(db)
    return service.eliminar(id)

