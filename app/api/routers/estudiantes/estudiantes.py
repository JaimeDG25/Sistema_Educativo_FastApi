# app/api/routers/estudiantes/estudiantes.py

from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import List, Optional, Union
from app.services.estudiantes import EstudiantesService
from app.schemas.estudiantes import EstudianteRequest, EstudianteResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db

router= APIRouter(prefix="/Estudiantes" , tags=["ESTUDIANTES"])

@router.get("/listEstudiantes", response_model=list[EstudianteResponse])
def get_list_estudiantes(
    db: Session = Depends(get_db)
):
    service = EstudiantesService(db)
    return service.listar()


@router.get("/findEstudianteById/{id}", response_model=EstudianteResponse)
def get_find_estudiante_by_id(
    id: int,
    db: Session = Depends(get_db)
)->EstudianteResponse:
    service = EstudiantesService(db)
    estudiante = service.buscarPorId(id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


@router.post("/addEstudiante", response_model=EstudianteResponse)
def post_add_estudiante(
    data: EstudianteRequest,
    db: Session = Depends(get_db)
)-> EstudianteResponse:
    service = EstudiantesService(db)
    return service.crear(data)


@router.delete("/deleteEstudiante", response_model=EstudianteResponse)
def delete_eliminate_estudiante(
    id: int,
    db: Session = Depends(get_db)
):
    service = EstudiantesService(db)
    return service.eliminar(id)


@router.put("/updateEstudiante/{id}", response_model=EstudianteResponse)
def put_update_estudiante(
    id: int,
    data: EstudianteRequest,
    db: Session = Depends(get_db)
)-> EstudianteResponse:
    service = EstudiantesService(db)
    estudiante = service.actualizar(id, data)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

