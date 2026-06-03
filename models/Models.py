from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conductor(db.Model):
    __tablename__ = 'Conductores'

    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)


class Camion(db.Model):
    __tablename__ = 'Camiones'

    id_camion = db.Column(db.Integer, primary_key=True)
    placa_camion = db.Column(db.String(20), unique=True, nullable=False)
    capacidad_peso = db.Column(db.Float, nullable=False)


class Movimiento(db.Model):
    __tablename__ = 'Movimientos'

    id_movimiento = db.Column(db.Integer, primary_key=True)
    hora_entrada = db.Column(db.DateTime)
    hora_salida = db.Column(db.DateTime)

    id_empleado = db.Column(
        db.Integer,
        db.ForeignKey('Conductores.id_empleado'),
        nullable=False
    )

    id_camion = db.Column(
        db.Integer,
        db.ForeignKey('Camiones.id_camion'),
        nullable=False
    )

    peso_carga = db.Column(db.Float)

    peso_llegada = db.Column(db.Float)

    discrepancia = db.Column(db.Float)

    conductor = db.relationship("Conductor")
    camion = db.relationship("Camion")