CREATE DATABASE IF NOT EXISTS test
    OWNER = 'root'
    MODE = 1;

USE test;

CREATE TABLE tbusuario (
    idusuario integer NOT NULL primary key,
	nombre varchar(50),
	apellido varchar(50),
	usuario varchar(15)  UNIQUE NOT NULL,
	password varchar(15) NOT NULL,
	fechacreacion date 
);
CREATE TABLE tbroles (
    idrol integer NOT NULL primary key,
	rol varchar(15)
);
DROP TABLE tbroles;

CREATE TABLE tbrol (
    idrol integer NOT NULL primary key,
	rol varchar(15)
);



CREATE TABLE tbrolxusuario (
    idrol integer NOT NULL ,
	idusuario integer NOT NULL 
);

 alter table tbrolxusuario
 add constraint FK_rol
  foreign key (idrol)
  references tbrol(idrol);
  
   alter table tbrolxusuario
 add constraint FK_usuario
  foreign key (idusuario)
  references tbusuario(idusuario);

--insert into tbrolxusaurio values(1,1);
--Error 23503


insert into tbrol values (1,'Administrador');
insert into tbrol values (2,'Admin');
insert into tbrol values (3,'Ventas');
--insert into tbrole values (1,'root');
--Error 23505


select * from tbrol;


insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
--Error 22001

ALTER TABLE tbusuario
    ALTER COLUMN password TYPE varchar(80);
	
insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
insert into tbusuario values(1,'Maria Cristina','Lopez Ramirez','mlopez',MD5('Diciembre'),now());
insert into tbusuario values(1,'Hugo Alberto','Huard Ordoñez','hhuard',MD5('Rafael'),now());
--Error 23505

select * from tbusuario;

insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
insert into tbusuario values(2,'Maria Cristina','Lopez Ramirez','mlopez',MD5('Diciembre'),now());
insert into tbusuario values(3,'Hugo Alberto','Huard Ordoñez','hhuard',MD5('Rafael'),now());

insert into tbrolxusuario values(1,1);
insert into tbrolxusuario values(2,2);
insert into tbrolxusuario values(2,3);


select rol,nombre,apellido
from tbrolxusuario RU
inner join tbusuario U on U.idusuario = RU.idusuario
inner join tbrol R on R.idrol = RU.idrol;


select rol,nombre,apellido
from tbrolxusuario RU
right join tbusuario U on U.idusuario = RU.idusuario
right join tbrol R on R.idrol = RU.idrol;


select *
from tbrol R
where idrol not in (select idrol from tbrolxusuario);

select *
from tbrol R
where not exists (select idrol from tbrolxusuario RU where RU.idrol = R.idrol);


create table tbestado
( idestado integer not null PRIMARY KEY,
  estado varchar(30)
);

create table tbempleado 
( idempleado integer not null UNIQUE PRIMARY KEY,
  primernombre varchar(50) not null,
 segundonombre varchar(50),
 primerapellido varchar(50) not null,
 segundoapellido varchar(50),
 fechadenacimiento DATE CONSTRAINT birth_data CHECK (fechadenacimiento > '1900-01-01'),
 fechacontratacion DATE CHECK (fechacontratacion > fechadenacimiento),
 idestado integer
);

 alter table tbempleado
 add constraint FK_estado
  foreign key (idestado)
  references tbestado(idestado);
  
 create table tbempleadoidentificacion(
	idempleado integer not null primary key,
	identificacion varchar(25) not null,
	ididentificaciontipo integer
);

create table tbidentificaciontipo(
	ididentificaciontipo integer not null primary key,
	tipoidentificacion varchar(20)
);

 alter table tbempleadoidentificacion
 add constraint FK_identificaciontipo
  foreign key (ididentificaciontipo)
  references tbidentificaciontipo(ididentificaciontipo);

  insert into tbidentificaciontipo values(1,'DPI');
insert into tbidentificaciontipo values(2,'Nit');
insert into tbidentificaciontipo values(3,'Pasaporte');

insert into tbestado values(1,'Activo');
insert into tbestado values(2,'Inactivo');

insert into tbempleado (idempleado,primernombre,primerapellido,fechanacimiento,fechacontartacion,idestado) values(1,'Thelma','Esquit','1981-01-25','2014-07-06',1);

--Error 42703

insert into tbempleado (idempleado,primernombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(1,'Thelma','Esquit','1981-01-25','2014-07-06',1);
insert into tbempleado (idempleado,primernombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(2,'Maria','Lopez','1990-12-01','2016-09-21',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(3,'Julio','Roberto','Rodriguez','1985-06-05','2012-01-22',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(4,'Roberto','Benjamin','Duque','1996-04-09','2018-10-03',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(5,'Francisco','','Juarez','Perez','1997-10-05','2010-03-01',1);

--Error 42601

insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(5,'Francisco','','Juarez','Perez','1997-10-05','2010-03-01',1);

insert into tbempleadoidentificacion values(1,'4578-784525-6562',1);
insert into tbempleadoidentificacion values(1,'8874585-5',2);
insert into tbempleadoidentificacion values(2,'1245-488454-7854',1);
insert into tbempleadoidentificacion values(3,'2610-417055-0101',1);
--la linea 2 da error porque no hay llave primaria compuesta

drop table tbempleadoidentificacion;

 create table tbempleadoidentificacion(
	idempleado integer not null,
	ididentificaciontipo integer not null,
	identificacion varchar(25) not null,
	primary key(idempleado,ididentificaciontipo)
);


insert into tbempleadoidentificacion values(1,1,'4578-784525-6562');
insert into tbempleadoidentificacion values(1,2,'8874585-5');
insert into tbempleadoidentificacion values(2,1,'1245-488454-7854');
insert into tbempleadoidentificacion values(3,1,'2610-417055-0101');



select E.*,estado,I.identificacion,tipoidentificacion
from tbempleado E, tbestado ES,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado = E.idestado
and I.idempleado = E.idempleado
and IT.ididentificaciontipo = I.ididentificaciontipo;

select E.*,estado,I.identificacion,tipoidentificacion
from tbempleado E, bestado ES ,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado = E.idestado
and  I.idempleado = E.idempleado
and  IT.ididentificaciontipo = I.ididentificaciontipo;
--Error 42P01

select E.*,estado,I.identificacion,tipoidentificacion
from tbempleado E, tbestado ES ,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado = E.idestado
and  I.idempleado = E.idempleado
and  IT.ididentificaciontipo = I.ididentificaciontipo;


