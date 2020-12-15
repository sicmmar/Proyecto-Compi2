from Expresion.Binaria import Binaria


class Logica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)


    def getval(self):
        valizq = self.exp1.getval()
        valder = self.exp2.getval()
        if self.operador == 'and':
            self.val = valizq and valder
        elif self.operador == 'or':
            self.val = valizq or valder
        return self.val
