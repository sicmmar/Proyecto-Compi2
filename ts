digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='6'>tbusuario</TD><TD rowspan='6'>TABLA</TD><TD rowspan='6'>test</TD><TD rowspan='6'></TD><TD>idusuario:integer</TD></TR>
<TR><TD>nombre:varchar</TD></TR>
<TR><TD>apellido:varchar</TD></TR>
<TR><TD>usuario:varchar</TD></TR>
<TR><TD>password:varchar</TD></TR>
<TR><TD>fechacreacion:date</TD></TR>
<TR><TD>U_test_tbusuario_usuario</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbusuario</TD><TD>usuario</TD></TR>

<TR><TD>PK_test_tbusuario</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbusuario</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>tbrol</TD><TD rowspan='2'>TABLA</TD><TD rowspan='2'>test</TD><TD rowspan='2'></TD><TD>idrol:integer</TD></TR>
<TR><TD>rol:varchar</TD></TR>
<TR><TD>PK_test_tbrol</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbrol</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>tbrolxusuario</TD><TD rowspan='2'>TABLA</TD><TD rowspan='2'>test</TD><TD rowspan='2'></TD><TD>idrol:integer</TD></TR>
<TR><TD>idusuario:integer</TD></TR>
<TR><TD>FK_test_tbrolxusuario_tbrol_FK_rol</TD><TD>CONSTRAINT FORANEA</TD><TD>test</TD><TD>tbrolxusuario</TD><TD></TD></TR><TR><TD>FK_test_tbrolxusuario_tbusuario_FK_usuario</TD><TD>CONSTRAINT FORANEA</TD><TD>test</TD><TD>tbrolxusuario</TD><TD></TD></TR></TABLE>>]
}
