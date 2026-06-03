from flask import render_template, request
from flask import Flask
from flask import jsonify
from datetime import datetime
from models import db

from models.Models import db, Movimiento, Conductor, Camion
from Utils.MovimientoHelper import MovimientoHelper


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transporte.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/RegistroEntradas', methods=['GET', 'POST'])
def entrada():

    mensaje = ""
    estado = ""

    movimientos = Movimiento.query.filter(
        Movimiento.hora_entrada == None
    ).all()

    if request.method == 'POST':

        id_salida = request.form['id_salida']
        peso_llegada = float(request.form['peso_llegada'])

        movimiento = Movimiento.query.get(id_salida)

        if movimiento is None:
            mensaje = "No existe una salida con ese ID"

        else:

            discrepancia = MovimientoHelper.calcular_discrepancia(
                movimiento.peso_carga,
                peso_llegada
            )

            movimiento.hora_entrada = datetime.now()
            movimiento.peso_llegada = peso_llegada
            movimiento.discrepancia = discrepancia

            db.session.commit()

            estado = MovimientoHelper.obtener_estado_discrepancia(
                movimiento.peso_carga,
                peso_llegada
            )

    mensaje = (
        f"Entrada registrada correctamente. "
        f"{estado}"
    )

    return render_template(
        'RegistroEntradas.html',
        mensaje=mensaje,
        movimientos=movimientos
    )


@app.route('/BuscarSalida/<int:id_movimiento>')
def buscar_salida(id_movimiento):

    movimiento = Movimiento.query.get(id_movimiento)

    if movimiento is None:
        return jsonify({
            "error": "No encontrado"
        }), 404

    return jsonify({
        "nombre_empleado": movimiento.conductor.nombre,
        "placa_camion": movimiento.camion.placa_camion,
        "peso_carga": movimiento.peso_carga
    })


@app.route('/RegistroSalidas', methods=['GET', 'POST'])
def salida():

    mensaje = ""

    conductores = Conductor.query.all()
    camiones = Camion.query.all()

    if request.method == 'POST':

        id_empleado = int(request.form.get('id_empleado'))
        id_camion = int(request.form.get('id_camion'))

        peso = float(request.form.get('peso'))

        conductor = Conductor.query.get(id_empleado)
        camion = Camion.query.get(id_camion)

        if conductor is None:
            mensaje = "El conductor no existe"

        elif camion is None:
            mensaje = "El camión no existe"

        else:

            movimiento = Movimiento(
                hora_entrada=None,
                hora_salida=datetime.now(),
                id_empleado=id_empleado,
                id_camion=id_camion,
                peso_carga=peso
            )

            db.session.add(movimiento)
            db.session.commit()

            mensaje = (
                f"Salida registrada correctamente. "
                f"ID Movimiento: {movimiento.id_movimiento}"
            )

    return render_template(
        'RegistroSalidas.html',
        mensaje=mensaje,
        conductores=conductores,
        camiones=camiones
    )


if __name__ == '__main__':
    app.run(debug=True)
