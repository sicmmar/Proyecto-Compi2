from Expresion.Expresion import Expresion
from Entorno import Entorno
class Funcion(Expresion):
    '''
        Esta clase representa una expresión
    '''

    'Todas las Instrrucciones tienen un valor y un tipo'
    def __init__(self,namefunc,parametros=[]):
        'Obtener el valor de la Instrruccion'
        self.namefund=namefunc
        self.parametros=parametros

    def getval(self,entorno):
            'Metodo Abstracto para obtener el valor de la Instrruccion'
            if self.namefunc=='DATE_PART':
                datepart=Date_Part(self.parametros[0], self.parametros[1])
                return datepart.getval(entorno)

class Date_Part(Funcion):
    'This is an abstract class'

    def __init__(self,field=None,interval=None):
        self.field=field
        self.interval=interval


    def getval(self,entorno):
        'spliteo el timestamp'
        splited=self.interval.split(' ')
        cont=0
        for contenido in splited:
            if contenido == self.field:
                print(splited[cont-1])
                return splited[cont-1]
            cont=cont+1
        return None

