import sqlite3
import os
import sys

# Add current path to sys.path to import app modules
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.core.password_security import hash_password

def reset_db():
    db_path = "sistema.db"
    if not os.path.exists(db_path):
        print(f"Error: No se encontró la base de datos en {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Disable foreign keys temporarily for truncation
        cursor.execute("PRAGMA foreign_keys = OFF;")

        # 1. Truncate/Clear all transaction and relations tables
        tables_to_clear = [
            "nota-evaluacion-table",
            "evaluacion-curso-table",
            "material-curso-table",
            "inscripcion-es-cu-table",
            "asignacion-cu-as-table",
            "asistentes-table",
            "estudiante-table"
        ]

        for table in tables_to_clear:
            print(f"Limpiando tabla: {table}")
            cursor.execute(f"DELETE FROM `{table}`;")

        print("Tablas limpiadas con éxito.")

        # 2. Re-enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Hashear contraseñas
        pass_admin = hash_password("12345")
        pass_docente = hash_password("12345")
        pass_estudiante = hash_password("student123")

        # 3. Insertar Seeds
        # Administrador (en asistentes-table)
        cursor.execute("""
            INSERT INTO `asistentes-table` (id, nombreEmpleado, apellidoEmpleado, dniEmpleado, correoEmpleado, habilitadoEmpleado, passwordEmpleado, rolesEmpleado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (1, "Zaiko", "Tsakio", "87654321", "asistente@gmail.com", 1, pass_admin, "ADMIN"))
        print("Seed de Administrador (Zaiko Tsakio) creado.")

        # Docente (en asistentes-table)
        cursor.execute("""
            INSERT INTO `asistentes-table` (id, nombreEmpleado, apellidoEmpleado, dniEmpleado, correoEmpleado, habilitadoEmpleado, passwordEmpleado, rolesEmpleado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (2, "Juan", "Pérez", "11223344", "juan.perez@example.com", 1, pass_docente, "ASISTENTE"))
        print("Seed de Docente (Juan Pérez) creado.")

        # Estudiante (en estudiante-table)
        cursor.execute("""
            INSERT INTO `estudiante-table` (id, nombreEstudiante, apellidoEstudiante, dniEstudiante, correoEstudiante, habilitadoEstudiante, rolEstudiante, passwordEstudiante)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (1, "Estudiante", "Mock", "55555555", "estudiante@gmail.com", 1, "ESTUDIANTE", pass_estudiante))
        print("Seed de Estudiante (Estudiante Mock) creado.")

        conn.commit()
        print("Todos los cambios guardados exitosamente en la base de datos.")

    except Exception as e:
        conn.rollback()
        print(f"Error durante el reseteo de la base de datos: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    reset_db()
