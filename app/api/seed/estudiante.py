
from app.models.estudiantes import Estudiantes

def seed_estudiante(db):
    existe = db.query(Estudiantes).filter(Estudiantes.correoEstudiante == "estudiante@gmail.com").first()
    if existe:
        return
    estudiante = Estudiantes(
        nombreEstudiante="Zaiko",
        apellidoEstudiante="Tsakio",
        dniEstudiante="12345678",
        correoEstudiante="estudiante@gmail.com",
        habilitadoEstudiante=True,
        rolEstudiante="ESTUDIANTE"
    )
    db.add(estudiante)
    db.commit()
    print("✅ Estudiante inicial creado")