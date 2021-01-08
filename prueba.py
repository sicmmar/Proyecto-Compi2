from goto import with_goto
from CodigoIntermedio import CodigoIntermedio
from Entorno.Entorno import Entorno
@with_goto
def prueba():
	stack =[]
	ci = CodigoIntermedio(Entorno())
	ci.ejecutarsql("create database DBFase2 ;") 
	ci.ejecutarsql(" use DBFase2;" )
	ci.ejecutarsql("create function myFuncion(texto text) returns text as $$ begin return texto; end; $$ language plpgsql;")
	goto .L1
	label .Lf_myFuncion
	texto=stack[0]
	stack[0]= texto
	temp=stack[1]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L1
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
	ci.ejecutarsql("create function ValidaRegistros(tabla varchar,cantidad integer) returns integer as $$ DECLARE resultado INTEGER;DECLARE retorna INTEGER;begin if tabla  = 'tbProducto' then resultado =  Select COUNT(*) from tbProducto;if cantidad  = resultado then retorna = 1; else retorna = 0;end if;end if;if tabla  = 'tbProductoUp' then resultado =  Select COUNT(*) from tbProducto Where estado  = 2;if cantidad  = resultado then retorna = 1; else retorna = 0;end if;end if;if tabla  = 'tbbodega' then resultado =  Select COUNT(*) from tbbodega;if cantidad  = resultado then retorna = 1; else retorna = 0;end if;end if;return retorna; end; $$ language plpgsql;")
	goto .L2
	label .Lf_ValidaRegistros
	tabla=stack[0]
	cantidad=stack[1]
	resultado=''
	retorna=''
	t4=tabla == 'tbProducto'
	if t4: 
	 	 goto .L6
	goto .L7
	label .L6
	ci.ejecutarsql("select COUNT(*) from tbProducto ;")
	resultado=ci.ejecutarsql("select COUNT(*) from tbProducto ;")
	
	t6=cantidad == resultado
	if t6: 
	 	 goto .L8
	goto .L9
	label .L8
	retorna=1
	goto .L10
	label .L9
	retorna=0
	label .L10
	label .L7
	t12=tabla == 'tbProductoUp'
	if t12: 
	 	 goto .L14
	goto .L15
	label .L14
	ci.ejecutarsql("select COUNT(*) from tbProducto Where estado  == 2 ;")
	resultado=ci.ejecutarsql("select COUNT(*) from tbProducto Where estado  == 2 ;")
	
	t16=cantidad == resultado
	if t16: 
	 	 goto .L16
	goto .L17
	label .L16
	retorna=1
	goto .L18
	label .L17
	retorna=0
	label .L18
	label .L15
	t20=tabla == 'tbbodega'
	if t20: 
	 	 goto .L22
	goto .L23
	label .L22
	ci.ejecutarsql("select COUNT(*) from tbbodega ;")
	resultado=ci.ejecutarsql("select COUNT(*) from tbbodega ;")
	
	t22=cantidad == resultado
	if t22: 
	 	 goto .L24
	goto .L25
	label .L24
	retorna=1
	goto .L26
	label .L25
	retorna=0
	label .L26
	label .L23
	stack[0]= retorna
	temp=stack[2]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L2
	ci.ejecutarsql(" insert into tbCalificacion values(1, 'Create Table and Insert', ValidaRegistros('tbProducto', 8));")
	ci.ejecutarsql("update tbProducto set estado=2 Where estado  = 1;")
	ci.ejecutarsql(" insert into tbCalificacion values(2, 'Update', ValidaRegistros('tbProductoUp', 8));")
	ci.ejecutarsql("create function CALCULOS() returns integer as $$ DECLARE hora integer;DECLARE SENO decimal;DECLARE VALOR INTEGER;DECLARE ABSOLUTO decimal;begin hora =  Select EXTRACT( hour from timestamp '2001-02-16 20:38:40') ;SENO =  Select SIN(1);VALOR = TRUNC(SENO * hora );VALOR = VALOR + LENGTH(SUBSTRING('FASE2', 1, 4)) ;ABSOLUTO = ABS(SINH(- 1 ));ABSOLUTO = (ABSOLUTO * SQRT(225) );VALOR = (VALOR + ABSOLUTO ) / acosd(0.5) ;if VALOR  > 1 then VALOR = 20; else VALOR = 10;end if;return VALOR; end; $$ language plpgsql;")
	goto .L51
	label .Lf_CALCULOS
	hora=''
	SENO=''
	VALOR=''
	ABSOLUTO=''
	ci.ejecutarsql("select EXTRACT( hour from timestamp '2001-02-16 20:38:40')  ;")
	hora=ci.ejecutarsql("select EXTRACT( hour from timestamp '2001-02-16 20:38:40')  ;")
	
	ci.ejecutarsql("select SIN(1) ;")
	SENO=ci.ejecutarsql("select SIN(1) ;")
	
	VALOR=None
	t47=VALOR + 4
	VALOR=t47
	ABSOLUTO=1.1752011936438014
	t49=ABSOLUTO * 15.0
	ABSOLUTO=t49
	t51=VALOR + ABSOLUTO
	t50=t51 / 60.00000000000001
	VALOR=t50
	t53=VALOR > 1
	if t53: 
	 	 goto .L52
	goto .L53
	label .L52
	VALOR=20
	goto .L54
	label .L53
	VALOR=10
	label .L54
	stack[0]= VALOR
	temp=stack[0]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L51
	ci.ejecutarsql(" insert into tbCalificacion values(3, ' Valida Funciones', CALCULOS() );")
	ci.ejecutarsql("create table tbbodega ( idbodega integer not null primary key, bodega varchar(100) not null, estado integer);")
	ci.ejecutarsql("create index nombreIndex on tbbodega (bodega);")
	goto .L59
	label .Lp_sp_validainsert
	ci.ejecutarsql(" insert into tbbodega values(1, 'BODEGA CENTRAL', 1);")
	ci.ejecutarsql(" insert into tbbodega (idbodega, bodega) values (2, 'BODEGA ZONA 12');")
	ci.ejecutarsql(" insert into tbbodega (idbodega, bodega, estado) values (3, 'BODEGA ZONA 11', 1);")
	ci.ejecutarsql(" insert into tbbodega (idbodega, bodega, estado) values (4, 'BODEGA ZONA 1', 1);")
	ci.ejecutarsql(" insert into tbbodega (idbodega, bodega, estado) values (5, 'BODEGA ZONA 10', 1);")
	temp=stack[0]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L59
	stack.append('.L60')
	goto .Lp_sp_validainsert
	label .L60
	ci.ejecutarsql(" insert into tbCalificacion values(4, 'Valida Store Procedure', ValidaRegistros('tbbodega', 5));")
	ci.ejecutarsql("create index idx_bodega on tbbodega (bodega,estado);")
	ci.ejecutarsql("drop index idx_bodega;")
	ci.ejecutarsql("create index idx_bodega on tbbodega (bodega,estado);")
	goto .L61
	label .Lp_sp_validaupdate
	ci.ejecutarsql("update tbbodega set bodega='bodega zona 9' Where idbodega  = 4;")
	temp=stack[0]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L61
	stack.append('.L62')
	goto .Lp_sp_validaupdate
	label .L62
	ci.ejecutarsql("delete from tbbodega Where idbodega  = 4 ;")
	ci.ejecutarsql(" insert into tbCalificacion values(5, 'Valida Delete', ValidaRegistros('tbbodega', 4));")
	ci.ejecutarsql("select * from tbbodega ;")
	ci.ejecutarsql("create index idx_bodega on tbbodega (estado);")
	goto .L63
	label .Lp_sp_insertaproducto
	llave=stack[0]
	producto=stack[1]
	fecha=stack[2]
	ci.ejecutarsql(" insert into tbProducto values("+str(llave)+","+str(producto)+","+str(fecha)+", 1);")
	temp=stack[3]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L63
	stack.append("9")
	stack.append("'Bocina Inalambrica'")
	stack.append("'2021-01-06'")
	stack.append('.L64')
	goto .Lp_sp_insertaproducto
	label .L64
	stack.append("10")
	stack.append("'Audifonos con Microfono USB'")
	stack.append("'2021-01-06'")
	stack.append('.L65')
	goto .Lp_sp_insertaproducto
	label .L65
	stack.append("11")
	stack.append("'Bocina Inalambrica'")
	stack.append("'2021-01-06'")
	stack.append('.L66')
	goto .Lp_sp_insertaproducto
	label .L66
	stack.append("12")
	stack.append("'Monitor de 17'")
	stack.append("'2021-01-06'")
	stack.append('.L67')
	goto .Lp_sp_insertaproducto
	label .L67
	ci.ejecutarsql("DROP function myFuncion;")
	ci.ejecutarsql("select myFuncion('Valida drop function') ;")
	ci.ejecutarsql("create function fn_Mensaje(texto text) returns text as $$ begin return texto; end; $$ language plpgsql;")
	goto .L68
	label .Lf_fn_Mensaje
	texto=stack[0]
	stack[0]= texto
	temp=stack[1]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L68
	ci.ejecutarsql("select myFuncion('Crea funcion Nueva de Mensaje') ;")
	stack.append("13")
	stack.append("'Bocina Inalambrica Sony'")
	stack.append("'2021-01-06'")
	stack.append('.L69')
	goto .Lp_sp_insertaproducto
	label .L69
	stack.append("14")
	stack.append("'Audifonos con Microfono USB Lenovo'")
	stack.append("'2021-01-06'")
	stack.append('.L70')
	goto .Lp_sp_insertaproducto
	label .L70
	stack.append("15")
	stack.append("'Monitor de 21'")
	stack.append("'2021-01-06'")
	stack.append('.L71')
	goto .Lp_sp_insertaproducto
	label .L71
	stack.append("16")
	stack.append("'Monitor de 17' Lenovo'")
	stack.append("'2021-01-06'")
	stack.append('.L72')
	goto .Lp_sp_insertaproducto
	label .L72
	ci.ejecutarsql("create table tbinventario ( idinventario integer not null primary key, idproducto integer not null, idbodega integer not null, cantidad integer not null, fechacarga date not null, descripcion text);")
	ci.ejecutarsql("create function fn_retornaproducto(Vproducto varchar) returns integer as $$ DECLARE idp integer;begin idp =  Select idproducto from tbProducto Where producto  = Vproducto;return idp; end; $$ language plpgsql;")
	goto .L73
	label .Lf_fn_retornaproducto
	Vproducto=stack[0]
	idp=''
	ci.ejecutarsql("select idproducto from tbProducto Where producto  == Vproducto ;")
	idp=ci.ejecutarsql("select idproducto from tbProducto Where producto  == Vproducto ;")
	
	stack[0]= idp
	temp=stack[1]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L73
	ci.ejecutarsql("create function fn_retornabodega(Vbodega varchar) returns integer as $$ DECLARE idb integer;begin idb =  Select idbodega from tbbodega Where bodega  = Vbodega;return idb; end; $$ language plpgsql;")
	goto .L74
	label .Lf_fn_retornabodega
	Vbodega=stack[0]
	idb=''
	ci.ejecutarsql("select idbodega from tbbodega Where bodega  == Vbodega ;")
	idb=ci.ejecutarsql("select idbodega from tbbodega Where bodega  == Vbodega ;")
	
	stack[0]= idb
	temp=stack[1]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L74
	ci.ejecutarsql("create function sp_insertainventario(ide integer,Vproducto varchar,Vbodega varchar,cantidad integer,descripcion varchar) returns integer as $$ DECLARE idproducto integer;DECLARE idbodega integer;DECLARE idev integer;begin idev =  Select count(*) from tbinventario Where idinventario  = ide;if idev  = 0 then idproducto =  Select fn_retornaproducto(Vproducto);idbodega =  Select fn_retornabodega(Vbodega);end if;return ide; end; $$ language plpgsql;")
	goto .L75
	label .Lf_sp_insertainventario
	ide=stack[0]
	Vproducto=stack[1]
	Vbodega=stack[2]
	cantidad=stack[3]
	descripcion=stack[4]
	idproducto=''
	idbodega=''
	idev=''
	ci.ejecutarsql("select count(*) from tbinventario Where idinventario  == ide ;")
	idev=ci.ejecutarsql("select count(*) from tbinventario Where idinventario  == ide ;")
	
	t75=idev == 0
	if t75: 
	 	 goto .L76
	goto .L77
	label .L76
	ci.ejecutarsql("select fn_retornaproducto(Vproducto) ;")
	idproducto=ci.ejecutarsql("select fn_retornaproducto(Vproducto) ;")
	
	ci.ejecutarsql("select fn_retornabodega(Vbodega) ;")
	idbodega=ci.ejecutarsql("select fn_retornabodega(Vbodega) ;")
	
	ci.ejecutarsql(" insert into tbinventario values("+str(ide)+","+str(idproducto)+","+str(idbodega)+","+str(cantidad)+","+str(now)+","+str(descripcion)+");")
	label .L77
	stack[0]= ide
	temp=stack[5]
	stack=[]
	if temp =='.L60':
		goto .L60
	if temp =='.L62':
		goto .L62
	if temp =='.L64':
		goto .L64
	if temp =='.L65':
		goto .L65
	if temp =='.L66':
		goto .L66
	if temp =='.L67':
		goto .L67
	if temp =='.L69':
		goto .L69
	if temp =='.L70':
		goto .L70
	if temp =='.L71':
		goto .L71
	if temp =='.L72':
		goto .L72
	
	label .L75
	ci.ejecutarsql("select sp_insertainventario(1, 'Laptop Lenovo', 'BODEGA CENTRAL', 200, 'Laptop Lenovo T420 i7 8GB') ;")
	ci.ejecutarsql("select sp_insertainventario(2, 'Teclado Inalambrico', 'BODEGA CENTRAL', 100, 'Teclado Inalambrico Lenovo') ;")
	ci.ejecutarsql("select sp_insertainventario(3, 'Mouse Inalambrico', 'BODEGA ZONA 12', 50, '') ;")
	ci.ejecutarsql("select sp_insertainventario(4, 'Laptop HP', 'bodega zona 9', 20, 'Laptop HP i5 4GB RAM') ;")
	
	ci.getSym()
