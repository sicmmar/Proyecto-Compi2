from Expresion.Funcion import Funcion
from Entorno import Entorno
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



