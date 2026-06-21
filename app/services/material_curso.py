# app/services/material_curso.py
from sqlalchemy.orm import Session
from datetime import date, datetime
from app.models.asignacion_cu_as import AsignacionCuAs
from app.models.cursos import Cursos
from app.models.material_curso import MaterialCurso
from app.schemas.material_curso import MaterialCursoRequest, MaterialCursoResponse

class MaterialCursoService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        materiales = self.db.query(MaterialCurso).all()
        return materiales
    
    def crear(self, data: MaterialCursoRequest):
        asignacion = self.db.query(AsignacionCuAs).filter(AsignacionCuAs.id == data.asignacionCuAsIdMaterial).first()
        if not asignacion:
            raise Exception("La asignacion no existe")

        nuevo_material = MaterialCurso(
            asignacionCuAsIdMaterial=data.asignacionCuAsIdMaterial,
            tituloMaterial=data.tituloMaterial,
            descripcionMaterial=data.descripcionMaterial,
            tipoMaterial=data.tipoMaterial,
            estadoMaterial=data.estadoMaterial,
            urlMaterial=data.urlMaterial,
            fechaSubidaMaterial=date.today()
        )

        self.db.add(nuevo_material)
        self.db.commit()
        self.db.refresh(nuevo_material)

        return nuevo_material