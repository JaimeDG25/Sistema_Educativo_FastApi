from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine
from app.database.base import Base

from app.api.routers.asistentes import asistentes
from app.api.routers.cursos import cursos
from app.api.routers.estudiantes import estudiantes
from app.api.routers.asignacion import asignacion
from app.api.routers.material import material_curso
from app.api.routers.inscripcion import inscripcion_es_cu
from app.api.routers.evaluacion import evaluacion_curso
from app.api.routers.nota import nota_evaluacion

from app.api.routers.login import login

from app.api.seed.asistente import seed_asistente
from app.api.seed.estudiante import seed_estudiante
from app.api.seed.curso import seed_curso
from app.database.connection import SessionLocal

from fastapi.staticfiles import StaticFiles
import os

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Gestiones")

# Asegurar directorios de carga de archivos y montar StaticFiles
os.makedirs("public/uploads/materials", exist_ok=True)
app.mount("/public", StaticFiles(directory="public"), name="public")
origins = [
    "http://localhost:3000",
    "https://async-courses.vercel.app",
    "https://async-courses-835fgf5d3-kalcios-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://async-courses-.*-kalcios-projects\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RUTAS DE SWAGER XD

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        seed_asistente(db)
        seed_estudiante(db)
        seed_curso(db)
    finally:
        db.close()


app.include_router(login.router)
app.include_router(asistentes.router)
app.include_router(cursos.router)
app.include_router(estudiantes.router)
app.include_router(asignacion.router)
app.include_router(material_curso.router)
app.include_router(inscripcion_es_cu.router)
app.include_router(evaluacion_curso.router)
app.include_router(nota_evaluacion.router)
