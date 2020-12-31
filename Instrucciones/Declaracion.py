from Tipo import Tipo
from Instrucciones.Instruccion import Instruccion
from Instrucciones.Asignacion import Asignacion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.Logica import *
from Expresion.Relacional import *
from Expresion.Expresion import *

from Expresion.FuncionesNativas import *

class Declaracion(Instruccion):
    def __init__(self, id=None,constant=False,tipo=None,valor=None,nullable=True):

        self.id=id
        self.constant=constant
        self.tipo=tipo
        self.valor=valor
        self.nullable=nullable

    def ejecutar(self, ent:Entorno):
        'ejecutar declaracion'
        simbolo=Simbolo(self.tipo,self.id,self.valor,-1)
        simbolo.atributos = {'constant': self.constant, 'nullable': self.nullable}
        s=ent.nuevoSimbolo(simbolo)





class default():
    'despues la defino'
