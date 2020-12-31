from goto import with_goto
import gramatica2 as grammar
from Entorno.Entorno import Entorno

global instr
instr = []
global ent
ent = Entorno(None)

def main():
    t1 = "CREATE DATABASE IF NOT EXISTS test OWNER = 'root' MODE = 1;"
    instr.append("")
    t0 = 0
    instr[t0] = t1
    t2 = "USE test;"
    instr.append("")
    t0 = t0 + 1
    instr[t0] = t2
    t3 = "create table tbpuesto ( idpuesto smallint not null, puesto character(25), salariobase money,primary key (idpuesto));"
    instr.append("")
    t0 = t0 + 1
    instr[t0] = t3

    func_intermedia()

def func_intermedia():
    obj = []
    for x in instr:
        obj.append(grammar.parse(x))


    for y in obj:
        for h in y:
            print (h)
            h.ejecutar(ent)

    

main()