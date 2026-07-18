
from app.models.estudiantes import Estudiantes
from app.core.password_security import hash_password
def seed_estudiante(db):
    existe = db.query(Estudiantes).filter(Estudiantes.correoEstudiante == "estudiante@gmail.com").first()
    if existe:
        return
    estudiantes = [
        Estudiantes(
            nombreEstudiante="Zaiko",
            apellidoEstudiante="Tsakio",
            dniEstudiante="12345678",
            correoEstudiante="estudiante@gmail.com",
            habilitadoEstudiante=True,
            rolEstudiante="ESTUDIANTE",
            passwordEstudiante=hash_password("student123")
        ),
        Estudiantes(
            nombreEstudiante="María",
            apellidoEstudiante="Gonzales",
            dniEstudiante="87654321",
            correoEstudiante="maria.gonzales@gmail.com",
            habilitadoEstudiante=True,
            rolEstudiante="ESTUDIANTE",
            passwordEstudiante=hash_password("maria123")
        ),
        Estudiantes(
            nombreEstudiante="Carlos",
            apellidoEstudiante="Ramírez",
            dniEstudiante="74185296",
            correoEstudiante="carlos.ramirez@gmail.com",
            habilitadoEstudiante=True,
            rolEstudiante="ESTUDIANTE",
            passwordEstudiante=hash_password("carlos123")
        ),
        Estudiantes(
            nombreEstudiante="Ana",
            apellidoEstudiante="Pérez",
            dniEstudiante="36925814",
            correoEstudiante="ana.perez@gmail.com",
            habilitadoEstudiante=True,
            rolEstudiante="ESTUDIANTE",
            passwordEstudiante=hash_password("ana123")
        ),
        Estudiantes(
            nombreEstudiante="Luis",
            apellidoEstudiante="Torres",
            dniEstudiante="25874136",
            correoEstudiante="luis.torres@gmail.com",
            habilitadoEstudiante=True,
            rolEstudiante="ESTUDIANTE",
            passwordEstudiante=hash_password("luis123")
        ),
    ]
    db.add_all(estudiantes)
    db.commit()
    print("Estudiante inicial creado")