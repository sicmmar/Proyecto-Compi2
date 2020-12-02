class Simbolo:
    def __init__(self, tipo = None, nombre = "", valor = None, linea = 0):
        self.tipo = tipo
        self.nombre = nombre
        self.valor = valor
        self.linea = linea
    
    def toString(self):
        if self.nombre != None:
            print(self.tipo, ";", self.nombre, ";", self.valor, ";", self.linea)
        