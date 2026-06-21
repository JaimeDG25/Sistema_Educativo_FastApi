
from app.models.cursos import Cursos

def seed_curso(db):
    existe = db.query(Cursos).filter(Cursos.id == 1).first()
    if existe:
        return
    curso = Cursos(
        nombreCurso="Matematica I",
        descripcionCurso="Geometria y razonamiento matematico",
        creditosCurso=5,
    )
    db.add(curso)
    db.commit()
    print("✅ Curso inicial creado")