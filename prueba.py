from goto import with_goto
from CodigoIntermedio import CodigoIntermedio
from Entorno.Entorno import Entorno
@with_goto
def prueba():
	stack =[]
	ci = CodigoIntermedio(Entorno())
	ci.ejecutarsql(create database DBFase2 ;) 
	ci.ejecutarsql( use DBFase2; )
	ci.ejecutarsql("create table tbProducto ( idproducto integer not null primary key, producto varchar(150) not null, fechacreacion date not null, estado integer);")
	ci.ejecutarsql("create unique index idx_producto on tbProducto (idproducto);")
	ci.ejecutarsql("create table tbCalificacion ( idcalifica integer not null primary key, item varchar(100) not null, punteo integer not null);")
	ci.ejecutarsql("create unique index idx_califica on tbCalificacion (idcalifica);")
	ci.ejecutarsql( insert into tbProducto values(1, 'Laptop Lenovo', now(), 1);)
	ci.ejecutarsql( insert into tbProducto values(2, 'Bateria para Laptop Lenovo T420', now(), 1);)
	ci.ejecutarsql( insert into tbProducto values(3, 'Teclado Inalambrico', now(), 1);)
	ci.ejecutarsql( insert into tbProducto values(4, 'Mouse Inalambrico', now(), 1);)
	ci.ejecutarsql( insert into tbProducto values(5, 'WIFI USB', now(), 1);)
	ci.ejecutarsql("create index test1_id_index on test1 (id);")
	ci.ejecutarsql("create index name on nuevo using hash (nose);")
	ci.ejecutarsql("create index test2_mm_idx on test2 (major,minor);")
	ci.ejecutarsql("create index test2_n_low on test2 (nuevo NULLS FIRST);")
	ci.ejecutarsql("create index test3_desc_index on test3 (id DESC NULLS LAST);")
	ci.ejecutarsql("create unique index indice on employees (columna1,columna2);")
	ci.ejecutarsql("create index test1_lower_col1_idx on test1 (None);")
	ci.ejecutarsql("create index access_log_client_ip_ix on access_log (client_ip);")
	ci.ejecutarsql("create index mytable_cat_1 on mytable (data);")
	ci.ejecutarsql("create index mytable_cat_2 on mytable (data);")
	ci.ejecutarsql("create index mytable_cat_3 on mytable (data);")
	
