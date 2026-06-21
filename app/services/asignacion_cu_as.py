# app/services/asignacion_cu_as.py
from sqlalchemy.orm import Session
from datetime import date, datetime
from app.models.asistentes import Asistente
from app.models.cursos import Cursos
from app.models.asignacion_cu_as import AsignacionCuAs
from app.schemas.asignacion_cu_as import AsignacionCuAsRequest,AsignacionCuAsResponse

class AsignacionCuAsService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        asignaciones = self.db.query(AsignacionCuAs).all()
        return asignaciones
    
    def crear(self, data: AsignacionCuAsRequest):
        asistente = self.db.query(Asistente).filter(Asistente.id == data.asistenteIdAsignacionCuAs).first()
        if not asistente:
            raise Exception("El asistente no existe")
        curso = self.db.query(Cursos).filter(Cursos.id == data.cursoIdAsignacionCuAs).first()
        if not curso:
            raise Exception("El curso no existe")

        nueva_asignacion = AsignacionCuAs(
            asistenteIdAsignacionCuAs=data.asistenteIdAsignacionCuAs,
            cursoIdAsignacionCuAs=data.cursoIdAsignacionCuAs,
            fechaAsignacionCuAs=date.today()
        )

        self.db.add(nueva_asignacion)
        self.db.commit()
        self.db.refresh(nueva_asignacion)

        return nueva_asignacion