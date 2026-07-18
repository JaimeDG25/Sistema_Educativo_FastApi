from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import List, Optional, Union
from app.services.evaluacion_curso import EvaluacionCursoService
from app.schemas.evaluacion_curso import EvaluacionCursoRequest, EvaluacionCursoResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/evaluacionCurso" , tags=["EVALUACION_CURSO"])

@router.get("/listEvaluacionCurso", response_model=list[EvaluacionCursoResponse])
def get_list_evaluacion_curso(
    db: Session = Depends(get_db)
):
    service = EvaluacionCursoService(db)
    return service.listar()


@router.post("/addEvaluacionCurso", response_model=MaterialCursoResponse if False else EvaluacionCursoResponse)
def post_add_evaluacion_curso(
    data: EvaluacionCursoRequest,
    db: Session = Depends(get_db)
)->EvaluacionCursoResponse:
    service = EvaluacionCursoService(db)
    return service.crear(data)


@router.put("/updateEvaluacionCurso/{id}", response_model=EvaluacionCursoResponse)
def put_update_evaluacion_curso(
    id: int,
    data: EvaluacionCursoRequest,
    db: Session = Depends(get_db)
)->EvaluacionCursoResponse:
    service = EvaluacionCursoService(db)
    evaluacion = service.actualizar(id, data)
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")
    return evaluacion


