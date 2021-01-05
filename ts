digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='8'>tbempleado</TD><TD rowspan='8'>TABLA</TD><TD rowspan='8'>test</TD><TD rowspan='8'></TD><TD>idempleado:integer</TD></TR>
<TR><TD>primernombre:varchar</TD></TR>
<TR><TD>segundonombre:varchar</TD></TR>
<TR><TD>primerapellido:varchar</TD></TR>
<TR><TD>segundoapellido:varchar</TD></TR>
<TR><TD>fechadenacimiento:DATE</TD></TR>
<TR><TD>fechacontratacion:DATE</TD></TR>
<TR><TD>idestado:integer</TD></TR>
<TR><TD>U_test_tbempleado_idempleado</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbempleado</TD><TD>idempleado</TD></TR>

<TR><TD>C_test_tbempleado_fechadenacimiento_birth_data</TD><TD>CONSTRAINT CHECK</TD><TD>test</TD><TD>tbempleado</TD><TD>fechadenacimiento &#62; 1900-01-01</TD></TR>\n<TR><TD>C_test_tbempleado_fechacontratacion</TD><TD>CONSTRAINT CHECK</TD><TD>test</TD><TD>tbempleado</TD><TD>fechacontratacion &#62; fechadenacimiento</TD></TR>\n<TR><TD>PK_test_tbempleado</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbempleado</TD><TD>[0]</TD></TR></TABLE>>]
}
