class Empleado:
#CONSTRUCTOR    
    def __init__(self, codigo, nombre, dni, numeroHoras, tarifaHora):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__dni = dni
        self.__numeroHoras = numeroHoras
        self.__tarifaHora = tarifaHora

    # Métodos get y set
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getNumeroHoras(self):
        return self.__numeroHoras

    def getTarifaHora(self):
        return self.__tarifaHora
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDni(self, dni):
        self.__dni = dni

    def setNumeroHoras(self, numeroHoras):
        self.__numeroHoras = numeroHoras

    def setTarifaHora(self, tarifaHora):
        self.__tarifaHora = tarifaHora

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    def sueldoBruto(self):
        return self.__numeroHoras * self.__tarifaHora

    def descuentoEssalud(self):
        return self.sueldoBruto() * 0.12

    def descuentoAfp(self):
        return self.sueldoBruto() * 0.11

    def descuentoTotal(self):
        return self.descuentoEssalud() + self.descuentoAfp()

    def sueldoNeto(self):
        return self.sueldoBruto() - self.descuentoTotal()
