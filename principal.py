import gramatica2 as g

f = open("./entradaproyecto.txt", "r")
input = f.read()

g.parse(input)