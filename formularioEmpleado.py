import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado

qtCreatorFile = "EC3_FALCON_FALCON/PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class FormularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioEmpleado, self).__init__()
        uic.loadUi("EC3_FALCON_FALCON/PaqueteEmpleado/frmEmpleado.ui", self)

        self.btnAceptar.clicked.connect(self.procesar)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.show()

    def procesar(self):
        # 
        codigo = 1
        nombre = "KEVIN"
        dni = "70243852"  
        numeroHoras = 20
        tarifaHora =  20

        empleado1 = Empleado(codigo, nombre, dni, numeroHoras, tarifaHora)
        self.mostrarDatos(empleado1)

    def imprimir(self, cad):
        self.txtS.append(cad)

    def mostrarDatos(self, empleado):
        self.imprimir("CODIGO\t: " + str(empleado.getCodigo()))
        self.imprimir("NOMBRE\t: " + str(empleado.getNombre()))
        self.imprimir("DNI\t: " + str(empleado.getDni()))
        self.imprimir("HORAS\t: " + str(empleado.getNumeroHoras()))
        self.imprimir("TARIFA\t: " + str(empleado.getTarifaHora()))
        self.imprimir("SUELDO BRUTO\t: " + str(empleado.sueldoBruto()))
        self.imprimir("DESCUENTO ESSALUD (12%)\t: " + str(empleado.descuentoEssalud()))
        self.imprimir("DESCUENTO AFP (11%)\t: " + str(empleado.descuentoAfp()))
        self.imprimir("DESCUENTO TOTAL\t: " + str(empleado.descuentoTotal()))
        self.imprimir("SUELDO NETO\t: " + str(empleado.sueldoNeto()))
        self.imprimir("")

    def cerrar(self):
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioEmpleado()
    app.exec()        