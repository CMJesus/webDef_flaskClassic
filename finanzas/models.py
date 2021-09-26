import csv
from datetime import date, datetime
from . import FICHERO

class ValidationError(Exception):
    pass

class Movimiento():
    def __init__(self, diccionario):
        try:
            self.fecha = date.fromisoformat(diccionario["fecha"])
            ahora = datetime.now()
            if self.fecha.strftime("%Y%m%d") > ahora.strftime("%Y%m%d"):
                self.errores.append("La fecha no puede ser superior a la actual")
                #raise ValidationError("La fecha no puede ser superior a la actual")
        except ValueError:
            self.errores.append("Formato de fecha")
            #raise ValidationError("Formato de fecha incorrecto")

        self.concepto = diccionario["concepto"]
        if self.concepto == "":
            raise ValidationError("Informe del concepto")
        
        try:
            self.es_ingreso = diccionario["ingreso_gasto"]
        except KeyError:
            self.errores("Informe tipo de movimiento(ingreso/gasto/)")
            #raise ValidationError("Informe tipo de movimiento(ingreso/gasto/)")
        
        try:
            self.cantidad = float(diccionario["cantidad"])
            if self.cantidad <= 0:
                self.errores("Introduzca una cantidad mayor que cero")
                #raise ValidationError("Introduzca una cantidad mayor que cero")
        except ValueError:
            self.errores("Cantidad debe de ser un número")
            #raise ValidationError("Cantidad debe de ser un número")

        
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
        dwriter.writeheader()        
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        fichero.close()

    def anyadir(self, valor):
        movimiento = {}
        movimiento['fecha'] = valor['fecha']
        movimiento['concepto'] = valor['concepto']
        movimiento['ingreso_gasto'] = valor['ingreso_gasto']
        movimiento['cantidad'] = valor['cantidad']
        self.movimientos.append(movimiento)