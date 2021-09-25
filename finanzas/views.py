from finanzas import app
from flask import render_template
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
    return render_template("index.html", titulo="[TÍTULO]", items=lm.movimientos)
    # de la misma forma que hemos indicado título, y Jinja lo interpretará
    # a través del render_template, podríamos también
    # modificar el Lenguaje.
    # Especificamos la variable que será reconocible por Jinja.