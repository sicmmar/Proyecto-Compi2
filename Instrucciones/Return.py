
from Instrucciones.Instruccion import Instruccion

class Return(Instruccion):
    def __init__(self,exp):
        self.exp=exp

    def ejecutar(self, ent):
        'ejecutar return'
        return self.exp.getval(ent)
