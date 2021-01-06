from Expresion.Expresion import Expresion
from Instrucciones.Declaracion import Declaracion
from tkinter import *
from reportes import *
from Expresion.variablesestaticas import variables
from Tipo import Tipo
from Entorno.Entorno import Entorno
import Instrucciones

class LLamadaFuncion(Expresion):
    def __init__(self,nombre,parametros):
        self.nombre=nombre
        self.parametros=parametros

    def getval(self, ent:Entorno):
        'ejecucion llamada funcinon'
        sim=ent.buscarSimbolo('_f'+self.nombre)
        if sim != None:
            tipo=sim.tipo
            defparams=sim.valor[0]
            instrucciones=sim.valor[1]
            newent=Entorno(ent)
            if self.parametros!=None:
                if len(defparams)==len(self.parametros):
                    for i in range(0,len(defparams)):
                        param=defparams[i]
                        dec=Declaracion(param.nombre,False,param.tipo,self.parametros[i])
                        dec.ejecutar(newent)
                    for inst in instrucciones:
                        v=  inst.ejecutar(newent)
                        if v!=None:
                            util=Tipo('',None,-1,-1)
                            if util.comparetipo(v.tipo,tipo):
                                return v
                            else:
                                reporteerrores.append(Lerrores("Error Semantico", "Error el tipo devuelto no coincide con el de la funcion",  0, 0))
                                variables.consola.insert(INSERT, "Error el tipo devuelto no coincide con el de la funcion")

                else:
                    reporteerrores.append(Lerrores("Error Semantico","Error Los parametros no coinciden con la definicion de la funcion",0, 0))
                    variables.consola.insert(INSERT,"Error Los parametros no coinciden con la definicion de la funcion")
                    return
            else:
                for inst in instrucciones:
                    v = inst.ejecutar(newent)
                    if v != None:
                        util = Tipo('', None, -1, -1)
                        if util.comparetipo(v.tipo, tipo):
                            return v
                        else:
                            reporteerrores.append(
                                Lerrores("Error Semantico", "Error el tipo devuelto no coincide con el de la funcion",
                                         0, 0))
                            variables.consola.insert(INSERT, "Error el tipo devuelto no coincide con el de la funcion")


    def traducir(self,ent):
        'traduzco funcion'
        lenp = 0
        cad = ''
        if self.params != None:
            lenp = len(self.params)

        for i in range(0, lenp):
            cad += 'stack.append(' + str(self.params[i].traducir(ent).temp) + ')\n'

        nl = ent.newlabel()
        cad += 'stack.append(\'' + nl + '\')\n'
        variables.stack.append(nl)
        cad += 'goto .L_' + self.nombre + '\n'
        cad += 'label ' + nl + '\n'
        nt=ent.newtemp()
        cad+=nt+' = stack[0]\n'
        self.temp=nt
        self.codigo3d = cad
        return self

