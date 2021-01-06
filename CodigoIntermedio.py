import gramatica2 as g


class CodigoIntermedio():
    def __init__(self,entorno):
        self.entorno=entorno


    def ejecutarsql(self,stringinstr):
        'ejecucion del bloque'
        g.parse(stringinstr)
