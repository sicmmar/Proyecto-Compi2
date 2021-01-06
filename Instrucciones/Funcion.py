from Entorno.Simbolo import Simbolo
from Instrucciones.Instruccion import Instruccion

class Funcion(Instruccion):
    def __init__(self,nombre,params,instrucciones,tipo=None):
        self.nombre=nombre
        self.params=params
        self.instrucciones=instrucciones
        self.tipo=tipo

    def ejecutar(self, ent):
        'ejecucion de la definicion de la funcion'
        simbolo = Simbolo(self.tipo, '_f'+self.nombre, [self.params,self.instrucciones], -1)
        s = ent.nuevoSimbolo(simbolo)

    def traducir(self, ent):
        self.codigo3d = 'ci.ejecutarsql("create function ' + self.nombre + '('
        if self.params != None:
            for param in self.params:
                if param.modo != None:
                    self.codigo3d += 'inout '
                self.codigo3d += param.nombre + ' ' + param.tipo.tipo
        self.codigo3d += ') return ' + self.tipo.tipo
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(self.codigo3d)
        print(self.tipo.valor)
        print(self.instrucciones)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


class Parametro():
    def __init__(self,nombre,modo,tipo):
        self.nombre=nombre
        self.modo=modo
        self.tipo=tipo