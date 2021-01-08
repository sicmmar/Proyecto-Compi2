from goto import with_goto
from CodigoIntermedio import CodigoIntermedio
from Entorno.Entorno import Entorno
@with_goto
def prueba():
	stack =[]
	ci = CodigoIntermedio(Entorno())
	ci.ejecutarsql("create database DBFase2 ;") 
	ci.ejecutarsql(" use DBFase2;" )
	goto .L1
	label .Lf_myFuncion
	texto=stack[0]
	stack[0]= texto
	temp=stack[1]
	stack=[]
	
	label .L1
	ci.ejecutarsql("create function myFuncion(texto text) returns text as $$ begin return texto; end; $$ language plpgsql;")
	ci.ejecutarsql("select myFuncion('INICIO CALIFICACION FASE 2') ;")
	ci.ejecutarsql("create table tbProducto ( idproducto integer not null primary key, producto varchar(150) not null, fechacreacion date not null, estado integer);")
	ci.ejecutarsql("create unique index idx_producto on tbProducto (idproducto);")
	ci.ejecutarsql("create table tbCalificacion ( idcalifica integer not null primary key, item varchar(100) not null, punteo integer not null);")
	ci.ejecutarsql("create unique index idx_califica on tbCalificacion (idcalifica);")
	ci.ejecutarsql(" insert into tbProducto values(1, 'Laptop Lenovo', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(2, 'Bateria para Laptop Lenovo T420', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(3, 'Teclado Inalambrico', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(4, 'Mouse Inalambrico', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(5, 'WIFI USB', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(6, 'Laptop HP', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(7, 'Teclado Flexible USB', now(), 1);")
	ci.ejecutarsql(" insert into tbProducto values(8, 'Laptop Samsung', '2021-01-02', 1);")
	ci.ejecutarsql("select myFuncion('Crea Funcion') ;")
	
	ci.getSym()
