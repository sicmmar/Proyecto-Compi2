digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='4'>tbProducto</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>DBFase2</TD><TD rowspan='4'></TD><TD>idproducto:integer</TD></TR>
<TR><TD>producto:varchar</TD></TR>
<TR><TD>fechacreacion:date</TD></TR>
<TR><TD>estado:integer</TD></TR>
<TR><TD>PK_DBFase2_tbProducto</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbProducto</TD><TD>[0]</TD></TR><TR><TD>idx_producto</TD><TD>INDEX</TD><TD>DBFase2</TD><TD>tbProducto</TD><TD>idproducto</TD></TR></TABLE>>]
}
