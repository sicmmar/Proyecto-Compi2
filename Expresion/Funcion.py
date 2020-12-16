from Expresion.Importes import *
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
            if self.namefund=='DATE_PART':
                return Date_Part(self.parametros[0],self.parametros[1])

