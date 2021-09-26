import csv
from . import FICHERO

class Movimiento():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = ingreso_gasto
        self.cantidad = cantidad

# Aquí arriba debe de haber validaciones. RaiseValueError

class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, "r")
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()

    def escribir(self):
        if len(self.movmientos) == 0:
            return

        fichero = open(FICHERO, "w")
        #nombres_campo = ["fecha", "concepto", "ingreso_gasto", "cantidad"]
        nombres_campo = list(self.movimientos[0].keys())
        # Aquí, con esta opción, tengo que asegurarme de que haya movimientos.
        # Para lo anterior podemos leer antes de entrar con un if len.
        dwriter = csv.DictWriter(fichero, fieldnames = nombres_campo)
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        fichero.close()

    # def anyadir(self, valor):
    #     movimiento = {}
    #     movimiento = ["fecha"] = valor ['fecha']
    #     movimiento = ['concepto'] = valor ['concepto']
    #     movimiento = ['ingreso_gasto'] = valor ['ingreso_gasto']
    #     movimiento = ['cantidad'] = valor ['cantidad']
    #     self.movimientos.append(movimiento)