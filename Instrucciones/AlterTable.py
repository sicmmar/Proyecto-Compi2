from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *
from enum import Enum
from Instrucciones.CreateTable import *

class AlterTable(Instruccion):
    def __init__(self,id,opcion):
        self.tabla = id
        self.opcion = opcion
    
    def ejecutar(self,ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tablaAlterada:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tablaAlterada != None:
                if self.opcion.tipoAlter == TipoAlter.ADDCOLUMNA:
                    addColumna:AddColumn = self.opcion
                    res = DBMS.alterAddColumn(dbActual,self.tabla,None)
                    if res == 0:
                        nuevaCol:Simbolo = Simbolo(addColumna.tipo,addColumna.id)
                        nuevaCol.tabla = self.tabla
                        nuevaCol.baseDatos = dbActual
                        tablaAlterada.valor.append(nuevaCol)
                        e = ent.editarSimbolo(self.tabla + "_" + dbActual,tablaAlterada)
                        if e == "ok": print("a la tabla se le agrego nueva col")
                    else: return "No se ha podido agregar la columna '" + addColumna.id + "' a la tabla " + self.tabla
                
                elif self.opcion.tipoAlter == TipoAlter.ADDCHECK:
                    #formato: C_database_tabla_nombreColumna
                    addCheck:AddCheck = self.opcion
                    nombreColCheck:str = str(addCheck.condicion.exp1.valor)
                    tablaCheck:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
                    if tablaCheck != None: 
                        for col in tablaCheck.valor:
                            if col.nombre == nombreColCheck:
                                col.atributos.update({'check':str("C_" + dbActual + "_" + self.tabla + "_" + col.nombre)})
                                nuevoSym:Simbolo = Simbolo(TipoSimbolo.CONSTRAINT_CHECK,str("C_" + dbActual + "_" + self.tabla + "_" + col.nombre),addCheck.condicion)
                                nuevoSym.baseDatos = dbActual
                                nuevoSym.tabla = self.tabla
                                ent.nuevoSimbolo(nuevoSym)
                                break

class TipoAlter(Enum):
    ADDCOLUMNA = 1,
    ADDCHECK = 2

class AddColumn():
    def __init__(self,id:str,tipo):
        self.id = id
        self.tipo = tipo
        self.tipoAlter = TipoAlter.ADDCOLUMNA

class AddCheck():
    def __init__(self,id,condicion:CondicionCheck):
        self.constraint = id
        self.condicion = condicion
        self.tipoAlter = TipoAlter.ADDCHECK