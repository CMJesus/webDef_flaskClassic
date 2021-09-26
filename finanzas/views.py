from finanzas import app
from flask import render_template, request, redirect, url_for
from finanzas.models import ListaMovimientos

# Aquí comenzamos a establecer las rutas:

# La Lista de Movimientos ya no nos sirve, hemos creado el Models.
# lista_movimientos = [
#     {
#         "fecha": "01/01/2021",
#         "concepto": "aguinaldos",
#         "es_ingreso": True,
#         "cantidad": 500.0,
#     },
#     {
#         "fecha": "01/02/2021",
#         "concepto": "regalo",
#         "es_ingreso": False,
#         "cantidad": 600.0,
#     },
#     {
#         "fecha": "01/03/2021",
#         "concepto": "gasto",
#         "es_ingreso": False,
#         "cantidad": 50.0,
#     }    
# ]


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
            return render_template("nuevo.html")
        else:
            datos = request.form
            lm = ListaMovimientos()
            lm.leer()
            lm.anyadir(datos)
            lm.escribir()
            return redirect(url_for("inicio"))
