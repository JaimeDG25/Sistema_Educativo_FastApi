from app.models.asistentes import Asistente, RolEmpleado
from app.core.password_security import hash_password

def seed_asistente(db):
    existe = db.query(Asistente)\
        .filter(Asistente.correoEmpleado == "asistente@gmail.com")\
        .first()
    if existe:
        return
    asistente = [
        Asistente(
            nombreEmpleado="Zaiko",
            apellidoEmpleado="Tsakio",
            habilitadoEmpleado=True,
            dniEmpleado="87654321",
            correoEmpleado="asistente@gmail.com",
            passwordEmpleado=hash_password("12345"),
            rolesEmpleado=RolEmpleado.ADMIN
        ),
        Asistente(
            nombreEmpleado="Ñiero",
            apellidoEmpleado="Vazques",
            habilitadoEmpleado=False,
            dniEmpleado="88765432",
            correoEmpleado="tacza@gmail.com",
            passwordEmpleado=hash_password("12345"),
            rolesEmpleado=RolEmpleado.ADMIN
        )
    ]
    db.add_all(asistente)
    db.commit()
    print("✅ Asistente inicial creado")

