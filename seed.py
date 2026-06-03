from datetime import datetime, timedelta
from app import app
from models.Models import db, Conductor, Camion, Movimiento


def cargar_datos_prueba():

    # Conductores
    conductor1 = Conductor(
        id_empleado=1,
        nombre="Juan Perez"
    )

    conductor2 = Conductor(
        id_empleado=2,
        nombre="Carlos Lopez"
    )

    conductor3 = Conductor(
        id_empleado=3,
        nombre="Pedro Martinez"
    )

    # Camiones
    camion1 = Camion(
        placa_camion="ABC123",
        capacidad_peso=20
    )

    camion2 = Camion(
        placa_camion="XYZ456",
        capacidad_peso=30
    )

    camion3 = Camion(
        placa_camion="DEF789",
        capacidad_peso=25
    )

    db.session.add_all([
        conductor1,
        conductor2,
        conductor3,
        camion1,
        camion2,
        camion3
    ])

    db.session.commit()



    print("Datos de prueba insertados correctamente")


with app.app_context():
    cargar_datos_prueba()