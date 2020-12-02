from Expresion import Expresion, Entorno
#import sys
#sys.path.append("/home/sicmmar/Documents/Compi2/Ejemplo2/arbol/")
#from Nodo import Nodo

class Operacion(Expresion):
    def __init__(self, tipo = "", valor = None, valorIzq = None, valorDer = None):
        self.valor = valor
        self.tipo = tipo
        self.valorIzq = valorIzq
        self.valorDer = valorDer

    def ejecutar(self, ent = Entorno()):
        if self.tipo == "int":
            return Operacion("int", int(self.valor))
        elif self.tipo == "double":
            return Operacion("double", self.valor)
        elif self.tipo == "caracter":
            return Operacion("caracter", self.valor)
        elif self.tipo == "booleano":
            if str(self.valor).lower() == "true":
                return Operacion("boolean", True)
            elif str(self.valor).lower == "false":
                return Operacion("boolean", False)
        
        elif self.tipo == "suma":
            return self.suma(ent, self.valorIzq, self.valorDer)


    
    def obtenerValor(self, ent = Entorno()):
        return Operacion(self.tipo, self.valor)

    def suma(self, ent = Entorno(), izq = None, der = None):
        x = izq.ejecutar(ent)
        y = der.ejecutar(ent)

        return Operacion("int", (int(x.valor) + int(y.valor)))



#globalito = Entorno()
#num1 = Operacion("int", 58)
#num2 = Operacion("int", 10)

#x = Operacion("suma",None,num1,num2)
#res = x.ejecutar(globalito)
#print(num1.valor)
#print(num2.valor)
#print(res.valor)