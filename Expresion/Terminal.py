from Expresion.Expresion import Expresion
from datetime import date
from datetime import datetime
from Entorno import Entorno
import random as rn
import math

class Terminal(Expresion) :
    '''
        Esta clase representa un terminal.
    '''
    def __init__(self,tipo,valor) :
       Expresion.__init__(self)
       self.tipo=tipo
       self.valor=valor

    def getval(self,entorno):

        if self.tipo.tipo=='identificador':
            'buscar columna'

        if str(self.valor) == 'CURRENT_DATE':
            return date.today()
        elif str(self.valor)== 'CURRENT_TIME' or (self.valor=='now' and self.tipo.tipo=='timestamp without time zone'):
            return datetime.now()
        elif(str(self.valor).lower()=='random'):
                value = rn.randint(0,1)
                return value
        elif (str(self.valor).lower()=="pi"):
                return math.pi
        return str(self.valor)