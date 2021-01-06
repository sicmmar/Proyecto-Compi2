digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='1'>myFuncion</TD><TD rowspan='1'>FUNCION : text</TD><TD rowspan='1'></TD><TD rowspan='1'></TD><TD>texto:text</TD></TR>
<TR><TD rowspan='4'>tbProducto</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>DBFase2</TD><TD rowspan='4'></TD><TD>idproducto:integer</TD></TR>
<TR><TD>producto:varchar</TD></TR>
<TR><TD>fechacreacion:date</TD></TR>
<TR><TD>estado:integer</TD></TR>
<TR><TD>PK_DBFase2_tbProducto</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbProducto</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>idx_producto</TD><TD rowspan='2'>INDEX</TD><TD rowspan='2'>DBFase2</TD><TD rowspan='2'>tbProducto</TD><TD> columna : idproducto</TD></TR>
<TR><TD>unique</TD></TR>
<TR><TD rowspan='3'>tbCalificacion</TD><TD rowspan='3'>TABLA</TD><TD rowspan='3'>DBFase2</TD><TD rowspan='3'></TD><TD>idcalifica:integer</TD></TR>
<TR><TD>item:varchar</TD></TR>
<TR><TD>punteo:integer</TD></TR>
<TR><TD>PK_DBFase2_tbCalificacion</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbCalificacion</TD><TD>[0]</TD></TR><TR><TD rowspan='2'>idx_califica</TD><TD rowspan='2'>INDEX</TD><TD rowspan='2'>DBFase2</TD><TD rowspan='2'>tbCalificacion</TD><TD> columna : idcalifica</TD></TR>
<TR><TD>unique</TD></TR>
<TR><TD rowspan='2'>ValidaRegistros</TD><TD rowspan='2'>FUNCION : int</TD><TD rowspan='2'></TD><TD rowspan='2'></TD><TD>tabla:varchar</TD></TR>
<TR><TD>cantidad:integer</TD></TR>
</TABLE>>]
}
