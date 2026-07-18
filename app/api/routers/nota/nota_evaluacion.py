from fastapi import APIRouter,Depends
from datetime import datetime
from typing import List, Optional, Union
from app.services.nota_evaluacion import NotaEvaluacionService
from app.schemas.nota_evaluacion import NotaEvaluacionRequest, NotaEvaluacionResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/notaEvaluacion" , tags=["NOTA_EVALUACION"])

@router.get("/listNotaEvaluacion", response_model=list[NotaEvaluacionResponse])
def get_list_nota_evaluacion(
    db: Session = Depends(get_db)
):
    service = NotaEvaluacionService(db)
    return service.listar()


@router.post("/addNotaEvaluacion", response_model=NotaEvaluacionResponse)
def post_add_nota_evaluacion(
    data: NotaEvaluacionRequest,
    db: Session = Depends(get_db)
)->NotaEvaluacionResponse:
    service = NotaEvaluacionService(db)
    return service.crear(data)


