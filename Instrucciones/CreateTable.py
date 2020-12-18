from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *

class CreateTable(Instruccion):
    def __init__(self, id:str, listaDef):
        self.id = id
        self.listaDef = listaDef
        self.numColumnas = 0

    def ejecutar(self, ent:Entorno):
        dbActual = ent.getDataBase()
        tam = len(self.listaDef)
        nuevaTabla = Simbolo(TipoSimbolo.TABLA,(self.id + "_" + dbActual))
        listaColumnas = []
        listaAtrCol = []
        hayPrimaria = False
        hayForanea = False
        primariaAdd:Primaria = None
        foraneaAdd:Foranea = None
        for x in range(0,tam,1):
            tt = self.listaDef[x]
            if tt.tipo == AtributosColumna.COLUMNA_SIMPLE:
                self.numColumnas += 1
                nuevaColumna = Simbolo(tt.tipoDato,tt.identificador)
                if tt.lista != None: #aca se mete si viene por ejemplo: columna1 integer references tabla2
                    tamano = len(tt.lista)
                    for y in range(tamano):
                        hayAtr = False
                        nuevoSym = Simbolo("tipo","nombre")
                        nuevoSym.baseDatos = dbActual
                        nuevoSym.tabla = self.id
                        atrColumna:Atributo = tt.lista[y]
                        if atrColumna.tipo == AtributosColumna.UNICO:
                            hayAtr = True
                            nuevoSym.tipo = TipoSimbolo.CONSTRAINT_UNIQUE
                            if atrColumna.valor != None:
                                nuevoSym.nombre = str("UNIQUE_" + atrColumna.valor)
                                nuevaColumna.atributos.update({'unique':atrColumna.valor})
                            else:
                                nuevoSym.nombre = str("UNIQUE_" + tt.identificador)
                                nuevaColumna.atributos.update({'unique':str("UNIQUE_" + tt.identificador)})
                        elif atrColumna.tipo == AtributosColumna.CHECK:
                            hayAtr = True
                            nuevoSym.tipo = TipoSimbolo.CONSTRAINT_CHECK
                            nuevoSym.valor = atrColumna.exp
                            if atrColumna.valor != None:
                                nuevoSym.nombre = str("CHECK_" + atrColumna.valor)
                                nuevaColumna.atributos.update({'check':atrColumna.valor})
                            else:
                                nuevoSym.nombre = str("CHECK_" + self.id + "_" + tt.identificador)
                                nuevaColumna.atributos.update({'check':str("CHECK_" + self.id + "_" + tt.identificador)})
                        elif atrColumna.tipo == AtributosColumna.DEFAULT:
                            nuevaColumna.atributos.update({'default':atrColumna.valor})
                        elif atrColumna.tipo == AtributosColumna.NO_NULO:
                            nuevaColumna.atributos.update({'not null':True})
                        elif atrColumna.tipo == AtributosColumna.NULO:
                            nuevaColumna.atributos.update({'null':True})
                        elif atrColumna.tipo == AtributosColumna.PRIMARY:
                            hayPrimaria = True
                            nuevaColumna.atributos.update({'primary':str("PK_" + dbActual + "_" + self.id)}) # PK_database_tabla
                        elif atrColumna.tipo == AtributosColumna.REFERENCES:
                            rr = DBMS.extractTable(dbActual,atrColumna.valor)
                            if rr == None:
                                return str("La tabla \'" + atrColumna.valor + "\' a la que está referenciando, no existe")
                            else:
                                tablaReferencia:Simbolo = ent.buscarSimbolo(atrColumna.valor + "_" + dbActual)
                                colRef = tablaReferencia.valor
                                for col in colRef:
                                    nomConstraintPK = col.atributos.get('primary')
                                    if nomConstraintPK != None:
                                        consPK:Simbolo = ent.buscarSimbolo(nomConstraintPK)
                                        arrPk = consPK.valor
                                        if len(arrPk) == 1:
                                            if tablaReferencia.valor[arrPk[0]].tipo.tipo == nuevaColumna.tipo.tipo:
                                                hayForanea = True
                                                hayAtr = True
                                                nuevoSym.tipo = TipoSimbolo.CONSTRAINT_FOREIGN # FK_database_tabla_tablaReferencia
                                                nuevoSym.nombre = str("FK_" + dbActual + "_" + self.id + "_" + atrColumna.valor)
                                                nuevaColumna.atributos.update({'foreign':str("FK_" + dbActual + "_" + self.id + "_" + atrColumna.valor)})
                                                break
                                
                                print(hayForanea)
                                if not hayForanea:
                                    variables.consola.insert(INSERT,"No se puede establecer llave foranea entre tabla '" + self.id + "' y '" + atrColumna.valor + "'\n")
                        
                        if hayAtr: listaAtrCol.append(nuevoSym)
                
                listaColumnas.append(nuevaColumna)
            
            if tt.tipo == AtributosColumna.PRIMARY:
                if hayPrimaria: 
                    variables.consola.insert(INSERT,str("La tabla \'" + self.id + "\' ya contiene llave primaria declarada\n"))
                else: 
                    primariaAdd:Primaria = tt
            
            if tt.tipo == AtributosColumna.REFERENCES:
                if hayForanea: 
                    variables.consola.insert(INSERT,str("La tabla \'" + self.id + "\' ya contiene llave foranea declarada\n"))
                else:
                    foraneaAdd:Foranea == tt
                    rr = DBMS.extractTable(dbActual,foraneaAdd.tabla)
            
            if tt.tipo == AtributosColumna.CONSTRAINT:
                print(tt.contenido)

                    


        nuevaTabla.valor = listaColumnas
        if dbActual != None:
            estado = DBMS.createTable(dbActual,self.id, self.numColumnas)
            if estado == 0: 
                nuevaTabla.baseDatos = dbActual
                r = ent.nuevoSimbolo(nuevaTabla)
                print(r)
                if r == "ok":
                    for x in listaAtrCol:
                        ent.nuevoSimbolo(x)
                    
                    alreadyPrimary = False
                    for x in range(len(listaColumnas)):
                        if not alreadyPrimary:
                            pk = listaColumnas[x].atributos.get('primary')
                            if pk != None: 
                                rrr = DBMS.alterAddPK(dbActual,self.id,[x])
                                if rrr != 0: 
                                    variables.consola.insert(INSERT,"No se ha podido agregar PK en tabla \'" + self.id + "\'\n")
                                else: 
                                    alreadyPrimary = True
                                    sym = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY,str("PK_" + dbActual + "_" + self.id))
                                    sym.valor = [x]
                                    ent.nuevoSimbolo(sym)
                    

                    if not alreadyPrimary:
                        tablaB:Simbolo = ent.buscarSimbolo(nuevaTabla.nombre)
                        if tablaB != None:
                            if primariaAdd != None:
                                listaPrim = primariaAdd.primarias
                                listPK = []
                                for p in listaPrim:
                                    for col in range(len(tablaB.valor)):
                                        if p.valor == tablaB.valor[col].nombre:
                                            listPK.append(col)
                                        #print(p.valor)
                                        #print(col.nombre)
                                
                                if len(listPK) > 0:
                                    n = DBMS.alterAddPK(dbActual,self.id,listPK)
                                    if n != 0:
                                        variables.consola.insert(INSERT,"No se ha podido agregar PK en tabla \'" + self.id + "\'\n")
                                    else: 
                                        alreadyPrimary = True
                                        sym = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY,str("PK_" + dbActual + "_" + self.id))
                                        sym.valor = listPK
                                        ent.nuevoSimbolo(sym)


                        

                    DBMS.showCollection()
                    return str("Tabla " + self.id + " creada exitosamente")
                
                return r
            #elif estado == 1: 

class Check(CreateTable):
    def __init__(self, condiciones):
        self.condiciones = condiciones
        self.tipo = AtributosColumna.CHECK

class Unique(CreateTable):
    def __init__(self, unicos):
        self.unicos = unicos
        self.tipo = AtributosColumna.UNICO

class Foranea(CreateTable):
    def __init__(self, foraneas, tabla:str, ref_lista):
        self.foraneas = foraneas
        self.tabla = tabla
        self.ref_lista = ref_lista
        self.tipo = AtributosColumna.REFERENCES

class Primaria(CreateTable):
    def __init__(self,primarias):
        self.primarias = primarias
        self.tipo = AtributosColumna.PRIMARY

class Atributo(CreateTable):
    def __init__(self,tipo:AtributosColumna,valor = None, exp = None):
        self.tipo = tipo
        self.valor = valor
        self.exp = exp

class Constraint(CreateTable):
    def __init__(self,identificador:str,objeto):
        self.id = identificador
        self.contenido = objeto
        self.tipo = AtributosColumna.CONSTRAINT

class Columna(CreateTable):
    def __init__(self,identificador:str,tipoDato,lista = None):
        self.identificador = identificador
        self.lista = lista #este recibe una lista
        self.tipoDato = tipoDato
        self.tipo = AtributosColumna.COLUMNA_SIMPLE

class ShowTables(Instruccion):
    def __init__(self, id):
        self.id = id

    def ejecutar(self, ent):
        variables.consola.insert(INSERT,"Ejecutando Show Tables para la base de datos: "+self.id+" \n")
        resultado = DBMS.showTables(self.id) 
        if(resultado==None):
            return "ERROR >> En la instrucción Show Tables("+self.id+"), base de datos: "+self.id+" NO existe"
        else:
            variables.x.title="DB: "+self.id
            variables.x.add_column("Tables",resultado)
            variables.consola.insert(INSERT,variables.x)
            variables.x.clear()
            variables.consola.insert(INSERT,"\n")
            return "Show Tables Exitoso"