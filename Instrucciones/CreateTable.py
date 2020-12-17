from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo

class CreateTable(Instruccion):
    def __init__(self, id:str, listaDef):
        self.id = id
        self.listaDef = listaDef
        self.numColumnas = 0

    def ejecutar(self, ent:Entorno):
        dbActual = ent.getDataBase()
        tam = len(self.listaDef)
        nuevaTabla = Simbolo(TipoSimbolo.TABLA,self.id)
        listaColumnas = []
        listaAtrCol = []
        hayPrimaria = False
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
                            hayAtr = True
                            hayPrimaria = True
                            nuevoSym.nombre = str("PK_" + self.id)
                            nuevoSym.tipo = TipoSimbolo.CONSTRAINT_PRIMARY
                            nuevaColumna.atributos.update({'primary':str("PK_" + self.id + "_" + tt.identificador)})
                        elif atrColumna.tipo == AtributosColumna.REFERENCES:
                            rr = DBMS.extractTable(dbActual,atrColumna.valor)
                            if rr == None:
                                return str("La tabla \'" + atrColumna.valor + "\' a la que está referenciando, no existe")
                            else:
                                #tablaReferencia:Simbolo = ent.buscarSimbolo(atrColumna.valor)

                                hayAtr = True
                                nuevoSym.tipo = TipoSimbolo.CONSTRAINT_FOREIGN
                                nuevoSym.nombre = str("FK_" + self.id + "_" + tt.identificador)
                                nuevaColumna.atributos.update({'foreign':str("FK_" + self.id + "_" + tt.identificador)})
                        
                        if hayAtr: listaAtrCol.append(nuevoSym)
                
                listaColumnas.append(nuevaColumna)
            
            if tt.tipo == AtributosColumna.PRIMARY:
                if hayPrimaria: return str("La tabla \'" + self.id + "\' ya contiene llave primaria declarada")
                #else:
                    


        nuevaTabla.valor = listaColumnas
        if dbActual != None:
            estado = DBMS.createTable(dbActual,self.id, self.numColumnas)
            if estado == 0: 
                nuevaTabla.baseDatos = dbActual
                ent.nuevoSimbolo(nuevaTabla)
                for x in listaAtrCol:
                    ent.nuevoSimbolo(x)
                
                alreadyPrimary = False
                for x in range(len(listaColumnas)):
                    if not alreadyPrimary:
                        pk = listaColumnas[x].atributos.get('primary')
                        if pk != None: print("res PK:",DBMS.alterAddPK(dbActual,self.id,[x]))
                        alreadyPrimary = True

                DBMS.showCollection()
                return str("Tabla " + nuevaTabla.nombre + " creada exitosamente")
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