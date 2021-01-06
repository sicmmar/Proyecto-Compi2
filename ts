digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='4'>tbProducto</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>DBFase2</TD><TD rowspan='4'></TD><TD>idproducto:integer</TD></TR>
<TR><TD>producto:varchar</TD></TR>
<TR><TD>fechacreacion:date</TD></TR>
<TR><TD>estado:integer</TD></TR>
<TR><TD>PK_DBFase2_tbProducto</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbProducto</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>idx_producto</TD><TD rowspan='2'>INDEX</TD><TD rowspan='2'>DBFase2</TD><TD rowspan='2'>tbProducto</TD><TD> columna : idproducto</TD></TR>
<TR><TD>unique</TD></TR>
<TR><TD rowspan='3'>tbCalificacion</TD><TD rowspan='3'>TABLA</TD><TD rowspan='3'>DBFase2</TD><TD rowspan='3'></TD><TD>idcalifica:integer</TD></TR>
<TR><TD>item:varchar</TD></TR>
<TR><TD>punteo:integer</TD></TR>
<TR><TD>PK_DBFase2_tbCalificacion</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbCalificacion</TD><TD>[0]</TD></TR><TR><TD rowspan='8'>tbempleado</TD><TD rowspan='8'>TABLA</TD><TD rowspan='8'>DBFase2</TD><TD rowspan='8'></TD><TD>idempleado:integer</TD></TR>
<TR><TD>primernombre:varchar</TD></TR>
<TR><TD>segundonombre:varchar</TD></TR>
<TR><TD>primerapellido:varchar</TD></TR>
<TR><TD>segundoapellido:varchar</TD></TR>
<TR><TD>fechadenacimiento:DATE</TD></TR>
<TR><TD>fechacontratacion:DATE</TD></TR>
<TR><TD>idestado:integer</TD></TR>
<TR><TD>U_DBFase2_tbempleado_idempleado</TD><TD>UNIQUE</TD><TD>DBFase2</TD><TD>tbempleado</TD><TD>idempleado</TD></TR>

<TR><TD>C_DBFase2_tbempleado_fechadenacimiento_birth_data</TD><TD>CONSTRAINT CHECK</TD><TD>DBFase2</TD><TD>tbempleado</TD><TD>fechadenacimiento &#62; 1900-01-01</TD></TR>\n<TR><TD>C_DBFase2_tbempleado_fechacontratacion</TD><TD>CONSTRAINT CHECK</TD><TD>DBFase2</TD><TD>tbempleado</TD><TD>fechacontratacion &#62; fechadenacimiento</TD></TR>\n<TR><TD>PK_DBFase2_tbempleado</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbempleado</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>idx_califica</TD><TD rowspan='2'>INDEX</TD><TD rowspan='2'>DBFase2</TD><TD rowspan='2'>tbCalificacion</TD><TD> columna : idcalifica</TD></TR>
<TR><TD>unique</TD></TR>
<TR><TD rowspan='2'>idx2</TD><TD rowspan='2'>INDEX</TD><TD rowspan='2'>DBFase2</TD><TD rowspan='2'>tbCalificacion</TD><TD> columna : item</TD></TR>
<TR><TD>orden: desc nulls last</TD></TR>
</TABLE>>]
}
