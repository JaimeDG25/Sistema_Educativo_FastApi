from fastapi import APIRouter,Depends
from datetime import datetime
from typing import List, Optional, Union
from app.services.material_curso import MaterialCursoService
from app.schemas.material_curso import MaterialCursoRequest,MaterialCursoResponse
import pandas as pd
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/materialCurso" , tags=["MATERIAL_CURSO"])

@router.get("/listMaterialCurso", response_model=list[MaterialCursoResponse])
def get_list_material_curso(
    db: Session = Depends(get_db)
):
    service = MaterialCursoService(db)
    return service.listar()


@router.post("/addMaterialCurso", response_model=MaterialCursoResponse)
def post_add_material_curso(
    data: MaterialCursoRequest,
    db: Session = Depends(get_db)
)->MaterialCursoResponse:
    service = MaterialCursoService(db)
    return service.crear(data)


