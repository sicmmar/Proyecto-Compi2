CREATE DATABASE IF NOT EXISTS test
    OWNER = 'root'
    MODE = 1;

USE test;

create table tbpuesto 
( idpuesto smallint not null,
  puesto character(25),
  salariobase money,
 primary key (idpuesto)
);

alter table tbpuesto add constraint c54 unique (puesto,salariobase);

insert into tbpuesto values (1,'Recepcionista',4000.00);

alter table tbpuesto
add column tinecomision boolean;

select * from tbpuesto;

insert into tbpuesto values (2,'Asistente Contable',4500.00,false);
insert into tbpuesto values(3,'Contador General',9000.00,false);
insert into tbpuesto values(4,'Asistente de RRHH',4000.00,false);
insert into tbpuesto values(5,'Recepcionista Gerencia',5000.00,false);
insert into tbpuesto values(6,'Vendedor 1',2500.00,true);
insert into tbpuesto values(7,'Vendedor 2',2750.00,true);
insert into tbpuesto values(8,'Vendedor 3',3000.00,true);
insert into tbpuesto values(9,'Jefe de Ventas',4000.00,true);
insert into tbpuesto values(10,'Jefe de Ventas Regional',2500.00,true);

select * from tbpuesto;

alter table tbpuesto drop constraint  c54;

insert into tbpuesto values (2,'Asistente Contable',4500.00,false);
insert into tbpuesto values(3,'Contador General',9000.00,false);
insert into tbpuesto values(4,'Asistente de RRHH',4000.00,false);
insert into tbpuesto values(5,'Recepcionista Gerencia',5000.00,false);
insert into tbpuesto values(6,'Vendedor 1',2500.00,true);
insert into tbpuesto values(7,'Vendedor 2',2750.00,true);
insert into tbpuesto values(8,'Vendedor 3',3000.00,true);
insert into tbpuesto values(9,'Jefe de Ventas',4000.00,true);
insert into tbpuesto values(10,'Jefe de Ventas Regional',2500.00,true);

delete from tbpuesto where salariobase = 5000.00;

select * from tbpuesto;


CREATE TYPE area AS ENUM ('CONTABILIDAD','ADMINISTRACION','VENTAS','TECNOLOGIA','FABRICA');

CREATE TABLE tbempleadopuesto
(
	idempleado integer not null,
	idpuesto   integer not null,
	departamento area
);

insert into tbempleadopuesto values(1,1,'ADMINISTRACION');
insert into tbempleadopuesto values(2,1,'CONTABILIDAD');
insert into tbempleadopuesto values(3,3,'CONTABILIDAD');
insert into tbempleadopuesto values(4,6,'VENTAS');
insert into tbempleadopuesto values(5,6,'VENTAS');
insert into tbempleadopuesto values(6,6,'OTRO');

select * from tbempleadopuesto;


UPDATE tbempleadopuesto SET idpuesto = 2 where idempleado = 2;

/*select departamento,count(*) CantEmpleados
from tbempleadopuesto
group by departamento;*/

create table tbventa 
(  idventa integer not null primary key,
   idempleado integer,
   fechaventa date constraint validaventa check (fechaventa > '1900-01-01'),
   montoventa money constraint ventavalida check (montoventa > 0.00),
   ventaregistrada boolean,
   descripcion text
);


insert into tbventa values(1,4,'2020-10-12',450.00,false,'Venta de bomba de agua para toyota');
insert into tbventa values(2,4,'2020-10-13',250.00,false,'Tasa distribuidor Mazda 626');
insert into tbventa values(3,4,'2020-10-13',650.00,false,'Radiador para Mazda 626');
insert into tbventa values(4,4,'2020-10-13',125.00,false,'Filtro de aire volkswagen');
insert into tbventa values(5,4,'2020-10-13',175.00,false,'Juego de Candelas volkswagen');
insert into tbventa values(6,4,'2020-10-13',220.00,false,'Aceite 20w50');
insert into tbventa values(7,5,'2020-10-13',1250.00,false,'Cremallera Mazda 3');
select * from tbventa;
alter table tbventa rename column descripcion to detalle;
insert into tbventa values(8,5,'2020-10-14',980.00,false,'Cremallera timon hidraulico mazda');
insert into tbventa values(9,5,'2020-10-14',1200.00,false,'Lodera Universal para pickup');
insert into tbventa values(10,5,'2020-10-14',475.00,false,'Sobre Lodera de Fibra de Carbon');
insert into tbventa values(11,5,'2020-10-14',780.00,false,'Bomba Auxiliar de agua para volkswagen');
insert into tbventa values(12,4,'2020-10-14',3500.00,false,'Bomba de agua para volkswagen');
insert into tbventa values(13,5,'2020-10-14',200.00,false,'Compresor de aire acondicionado');
insert into tbventa values(14,5,'2020-10-15',2000.00,false,'Bomba Auxiliar de agua para volkswagen');
select * from tbventa;

alter table tbventa drop column fechaventa, ventaregistrada;

select * from tbventa;


select primernombre,segundonombre,primerapellido,sum(montoventa)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;

select primernombre,segundonombre,primerapellido,fechaventa,sum(montoventa)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido,fechaventa;

select primernombre,segundonombre,primerapellido,sum(montoventa) TotalVenta
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;

select primernombre,primerapellido,EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40') diaventa,sum(montoventa)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by 1,2,3
order by 1;