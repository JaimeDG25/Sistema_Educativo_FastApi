from fastapi import APIRouter, Depends, HTTPException
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
    materiales = service.listar()
    return [m for m in materiales if m.asignacion is not None and m.asignacion.curso is not None]


from fastapi import Form, File, UploadFile
import os
import uuid

@router.post("/addMaterialCurso", response_model=MaterialCursoResponse)
def post_add_material_curso(
    asignacionCuAsIdMaterial: int = Form(...),
    tituloMaterial: str = Form(...),
    descripcionMaterial: str = Form(...),
    tipoMaterial: str = Form(...),
    estadoMaterial: bool = Form(...),
    urlMaterial: Optional[str] = Form(None),
    semana: int = Form(1),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
)->MaterialCursoResponse:
    final_url = urlMaterial
    if file is not None and file.filename != "":
        # Generar nombre único
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{file_ext}"
        
        # Carpeta local
        upload_dir = os.path.join("public", "uploads", "materials")
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, unique_filename)
        
        # Guardar archivo
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
            
        # Ruta de acceso (URL)
        final_url = f"/public/uploads/materials/{unique_filename}"

    data = MaterialCursoRequest(
        asignacionCuAsIdMaterial=asignacionCuAsIdMaterial,
        tituloMaterial=tituloMaterial,
        descripcionMaterial=descripcionMaterial,
        tipoMaterial=tipoMaterial,
        estadoMaterial=estadoMaterial,
        urlMaterial=final_url or "",
        fechaSubidaMaterial=datetime.utcnow(),
        semana=semana
    )
    service = MaterialCursoService(db)
    return service.crear(data)


@router.put("/updateMaterialCurso/{id}", response_model=MaterialCursoResponse)
def put_update_material_curso(
    id: int,
    data: MaterialCursoRequest,
    db: Session = Depends(get_db)
)->MaterialCursoResponse:
    service = MaterialCursoService(db)
    material = service.actualizar(id, data)
    if not material:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return material


@router.delete("/deleteMaterialCurso")
def delete_eliminate_material_curso(
    id: int,
    db: Session = Depends(get_db)
):
    service = MaterialCursoService(db)
    material = service.eliminar(id)
    if not material:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return {"message": "Material eliminado exitosamente", "id": id}


