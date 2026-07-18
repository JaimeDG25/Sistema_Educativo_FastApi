
from app.models.cursos import Cursos

def seed_curso(db):
    existe = db.query(Cursos).filter(Cursos.id == 1).first()
    if existe:
        return
    curso = [
        Cursos(
            nombreCurso="Matematica I",
            descripcionCurso="Geometria y razonamiento matematico",
            creditosCurso=5,
        ),
        Cursos(
            nombreCurso="Principios Algoritmos",
            descripcionCurso="Fundamentos de programación y resolución de problemas mediante algoritmos",
            creditosCurso=5,
        ),
        Cursos(
            nombreCurso="Base de Datos",
            descripcionCurso="Diseño, modelado y gestión de bases de datos relacionales",
            creditosCurso=4,
        ),
        Cursos(
            nombreCurso="Programación Orientada a Objetos",
            descripcionCurso="Desarrollo de aplicaciones utilizando el paradigma orientado a objetos",
            creditosCurso=5,
        ),
        Cursos(
            nombreCurso="Ingeniería de Software",
            descripcionCurso="Análisis, diseño y desarrollo de sistemas de software",
            creditosCurso=4,
        ),
        Cursos(
            nombreCurso="Redes y Comunicaciones",
            descripcionCurso="Fundamentos de redes de computadoras y protocolos de comunicación",
            creditosCurso=4,
        ),
    ]
    db.add_all(curso)
    db.commit()
    print("Curso inicial creado")