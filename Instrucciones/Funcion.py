from Entorno.Simbolo import Simbolo
from Instrucciones.Instruccion import Instruccion
from Expresion.variablesestaticas import variables
from tkinter import  *
from Expresion.Terminal import  Terminal
from Instrucciones.Declaracion import Declaracion
from Tipo import  Tipo
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
        if s!='ok':
            variables.consola.insert(INSERT,'La funcion '+self.nombre+' no se pudo crear porque ya existe\n')

    def traducir(self,ent):
        'traduccion proc'
        nl = ent.newlabel()
        cad = 'goto ' + nl + '\n'
        cad += 'label ' + ent.newlabel('f_' + self.nombre) + '\n'
        cont = 0
        lenparams = 0
        if self.params != None:
            lenparams = len(self.params)

        for i in range(0, lenparams):
            val = 'stack[' + str(i) + ']'
            term = Terminal(Tipo('stack', None, -1, -1), val)
            d = Declaracion(self.params[i].nombre, False, self.params[i].tipo, term)
            c3d = d.traducir(ent).codigo3d
            cad += c3d
            cont = i

        if self.instrucciones != None:
            for inst in self.instrucciones:
                if inst != None:
                    c3d = inst.traducir(ent).codigo3d
                    cad += c3d
        cad += 'temp=stack[' + str(lenparams) + ']\n'
        cad += 'stack=[]\n'
        cad += 'goto temp\n'
        cad += 'label ' + nl + '\n'
        self.codigo3d = cad

        # string quemado 
        self.stringsql = 'ci.ejecutarsql("create function ' + self.nombre + '('
        if self.params != None:
            for param in self.params:
                if param.modo != None:
                    self.stringsql += 'inout '
                self.stringsql += param.nombre + ' ' + param.tipo.tipo
        self.stringsql += ') returns ' + self.tipo.tipo
        
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(self.codigo3d)
        print(self.tipo.valor)
        print(self.instrucciones)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

        return self




class DropFunction(Instruccion):
    def __init__(self,nombre):
        self.nombre=nombre

    def ejecutar(self,ent):
        res= ent.eliminarSimbolo('_f'+self.nombre)
        if res=='ok':
            variables.consola.insert(INSERT,'Se elimino la funcion '+self.nombre +'\n')

class Parametro():
    def __init__(self,nombre,modo,tipo):
        self.nombre=nombre
        self.modo=modo
        self.tipo=tipo

