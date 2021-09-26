from finanzas import app
from flask import render_template, request, redirect, url_for
from finanzas.models import ListaMovimientos, Movimiento, ValidationError

# Aquí comenzamos a establecer las rutas:
@app.route("/")
def inicio():
    lm = ListaMovimientos()
    lm.leer()
    print(lm.movimientos)
    return render_template("index.html", items=lm.movimientos)
    # de la misma forma que hemos indicado título, y Jinja lo interpretará
    # a través del render_template, podríamos también
    # modificar el Lenguaje.
    # Especificamos la variable que será reconocible por Jinja.

@app.route("/nuevo", methods=['GET', 'POST'])
def nuevo():

    if request.method == 'GET':
        return render_template("nuevo_mov.html", errores=[], form = {"fecha":"", "concepto":"", "cantidad":""})
    else:
        datos = request.form
        movimiento = Movimiento(datos)
        # try:
        #     movimiento = Movimiento(datos)
        if len(movimiento.errores) > 0:
        #except ValidationError as msg:
            return render_template("nuevo_mov.html", errores= movimiento.errores, form=datos)

        #TODO validar datos

        lm = ListaMovimientos()
        lm.leer()
        
        lm.anyadir(datos)
        lm.escribir()

        return redirect(url_for("inicio"))
