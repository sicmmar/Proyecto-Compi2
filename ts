digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD>sp_validainsert</TD><TD>PROCEDURE</TD><TD></TD><TD></TD><TD></TD></TR>
<TR><TD>sp_validaupdate</TD><TD>PROCEDURE</TD><TD></TD><TD></TD><TD></TD></TR>
<TR><TD rowspan='3'>sp_insertaproducto</TD><TD rowspan='3'>PROCEDURE</TD><TD rowspan='3'></TD><TD rowspan='3'></TD><TD>llave:integer</TD></TR>
<TR><TD>producto:varchar</TD></TR>
<TR><TD>fecha:date</TD></TR>
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
<TR><TD rowspan='2'>ValidaRegistros</TD><TD rowspan='2'>FUNCION : integer</TD><TD rowspan='2'></TD><TD rowspan='2'></TD><TD>tabla:varchar</TD></TR>
<TR><TD>cantidad:integer</TD></TR>
<TR><TD>CALCULOS</TD><TD>FUNCION : integer</TD><TD></TD><TD></TD><TD></TD></TR>
<TR><TD rowspan='3'>tbbodega</TD><TD rowspan='3'>TABLA</TD><TD rowspan='3'>DBFase2</TD><TD rowspan='3'></TD><TD>idbodega:integer</TD></TR>
<TR><TD>bodega:varchar</TD></TR>
<TR><TD>estado:integer</TD></TR>
<TR><TD>PK_DBFase2_tbbodega</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbbodega</TD><TD>[0]</TD></TR><TR><TD rowspan='1'>nombreIndex</TD><TD rowspan='1'>INDEX</TD><TD rowspan='1'>DBFase2</TD><TD rowspan='1'>tbbodega</TD><TD> columna : bodega</TD></TR>
<TR><TD rowspan='1'>idx_bodega</TD><TD rowspan='1'>INDEX</TD><TD rowspan='1'>DBFase2</TD><TD rowspan='1'>tbbodega</TD><TD> columna : bodega</TD></TR>
<TR><TD rowspan='1'>idx_bodega</TD><TD rowspan='1'>INDEX</TD><TD rowspan='1'>DBFase2</TD><TD rowspan='1'>tbbodega</TD><TD> columna : estado</TD></TR>
<TR><TD rowspan='1'>fn_Mensaje</TD><TD rowspan='1'>FUNCION : text</TD><TD rowspan='1'></TD><TD rowspan='1'></TD><TD>texto:text</TD></TR>
<TR><TD rowspan='6'>tbinventario</TD><TD rowspan='6'>TABLA</TD><TD rowspan='6'>DBFase2</TD><TD rowspan='6'></TD><TD>idinventario:integer</TD></TR>
<TR><TD>idproducto:integer</TD></TR>
<TR><TD>idbodega:integer</TD></TR>
<TR><TD>cantidad:integer</TD></TR>
<TR><TD>fechacarga:date</TD></TR>
<TR><TD>descripcion:text</TD></TR>
<TR><TD>PK_DBFase2_tbinventario</TD><TD>CONSTRAINT PRIMARIA</TD><TD>DBFase2</TD><TD>tbinventario</TD><TD>[0]</TD></TR><TR><TD rowspan='1'>fn_retornaproducto</TD><TD rowspan='1'>FUNCION : integer</TD><TD rowspan='1'></TD><TD rowspan='1'></TD><TD>Vproducto:varchar</TD></TR>
<TR><TD rowspan='1'>fn_retornabodega</TD><TD rowspan='1'>FUNCION : integer</TD><TD rowspan='1'></TD><TD rowspan='1'></TD><TD>Vbodega:varchar</TD></TR>
<TR><TD rowspan='5'>sp_insertainventario</TD><TD rowspan='5'>FUNCION : integer</TD><TD rowspan='5'></TD><TD rowspan='5'></TD><TD>ide:integer</TD></TR>
<TR><TD>Vproducto:varchar</TD></TR>
<TR><TD>Vbodega:varchar</TD></TR>
<TR><TD>cantidad:integer</TD></TR>
<TR><TD>descripcion:varchar</TD></TR>
</TABLE>>]
}
