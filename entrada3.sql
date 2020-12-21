CREATE DATABASE IF NOT EXISTS test
    OWNER = 'root'
    MODE = 1;

USE test;

create table tblibrosalario
( idempleado integer not null,
  aniocalculo integer not null CONSTRAINT aniosalario CHECK (aniocalculo > 0),
  mescalculo  integer not null CONSTRAINT mescalculo CHECK (mescalculo < 12),
  salariobase  money not null,
  comision     decimal,
  primary key(idempleado)
 );


insert into tblibrosalario values(4,2020,10,2500,6885);
insert into tblibrosalario values(5,2020,10,2750,5370);
insert into tblibrosalario (idempleado,aniocalculo,mescalculo,salariobase) values(1,2020,10,4500);

update tbventa set ventaregistrada = true 
where idempleado = 4
and fechaventa between '2020-10-01' and '2020-10-31';

update tbventa set ventaregistrada = true 
where idempleado = 5
and fechaventa between '2020-10-01' and '2020-10-31';

select *
from tbventa where ventaregistrada = false;

SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT date_part('hour', INTERVAL '4 hours 3 minutes');
SELECT now();
SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(MINUTE FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(SECOND FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(MONTH FROM TIMESTAMP '2001-02-16 20i:38:40');
SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT date_part('minutes', INTERVAL '4 hours 3 minutes');
SELECT date_part('seconds', INTERVAL '4 hours 3 minutes 15 seconds');
SELECT CURRENT_DATE;
SELECT CURRENT_TIME;
SELECT TIMESTAMP 'now';

create table tblibrosalariohis
( idhistorico integer not null primary key
) INHERITS (tblibrosalario);

SELECT idempleado,abs(comision),cbrt(comision),DIV(325,5)
FROM tblibrosalario;

SELECT factorial(17) AS factorial, 
EXP(2.0) as Exponencial,
LN(5.0) "Logaritmo Natural",
PI(),
POWER(5,2);


SELECT 
  width_bucket(3, 1, 12, 3),
  width_bucket(5, 1, 12, 3),
  width_bucket(9, 1, 12, 3);


create table tbfuncionesmath
(
	idfuncion int not null primary key,
	seno decimal(10,2),
	coseno decimal(10,2)
);

insert into tbfuncionesmath values(1,0,0);
insert into tbfuncionesmath values(2,0,0);
insert into tbfuncionesmath values(3,0,0);
insert into tbfuncionesmath values(4,0,0);

update tbfuncionesmath set seno = SIN(1),coseno = COS(0) where idfuncion = 1;
update tbfuncionesmat set seno = SIND(1),coseno = TAN(0) where idfuncion = 1;
--Error 42P01
update tbfuncionesmath set seno = SIND(1),coseno = TAN(0) where idfuncion = 1;
update tbfuncionesmath set seno = TAND(0),coseno = COSD(0) where idfuncion = 2;

delete from tbfuncionesmath where idfuncion = 1;

select * from tbfuncionesmath;