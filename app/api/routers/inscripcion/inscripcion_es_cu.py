from fastapi import APIRouter,Depends
from datetime import datetime
from typing import List, Optional, Union
from app.services.inscripcion_es_cu import InscripcionEsCuService
from app.schemas.inscripcion_es_cu import InscripcionEsCuResponse, InscripcionEsCuRequest
import pandas as pd
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/inscripcionEsCu" , tags=["INSCRIPCION_ES_CU"])

@router.get("/listInscripcionEsCu", response_model=list[InscripcionEsCuResponse])
def get_list_inscripcion_es_cu(
    db: Session = Depends(get_db)
):
    service = InscripcionEsCuService(db)
    return service.listar()


@router.post("/addInscripcionEsCu", response_model=InscripcionEsCuResponse)
def post_add_inscripcion_es_cu(
    data: InscripcionEsCuRequest,
    db: Session = Depends(get_db)
)->InscripcionEsCuResponse:
    service = InscripcionEsCuService(db)
    return service.crear(data)


