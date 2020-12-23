digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='4'>tbpuesto</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>test</TD><TD rowspan='4'></TD><TD>idpuesto:smallint</TD></TR>
<TR><TD>puesto:character</TD></TR>
<TR><TD>salariobase:money</TD></TR>
<TR><TD>tinecomision:boolean</TD></TR>
<TR><TD>PK_test_tbpuesto</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbpuesto</TD><TD>[0]</TD></TR><TR><TD rowspan='4'>tbpuesto2</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>test</TD><TD rowspan='4'></TD><TD>idpuesto:smallint</TD></TR>
<TR><TD>puesto:character</TD></TR>
<TR><TD>salariobase:money</TD></TR>
<TR><TD>tinecomision:boolean</TD></TR>
<TR><TD>PK_test_tbpuesto2</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbpuesto2</TD><TD>[0]</TD></TR><TR><TD>U_test_tbpuesto2_puesto_c54</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbpuesto2</TD><TD>puesto</TD></TR>

<TR><TD>U_test_tbpuesto2_salariobase_c54</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbpuesto2</TD><TD>salariobase</TD></TR>

<TR><TD rowspan='5'>area</TD><TD rowspan='5'>ENUM</TD><TD rowspan='5'>test</TD><TD rowspan='5'></TD><TD>CONTABILIDAD</TD></TR>
<TR><TD>ADMINISTRACION</TD></TR>
<TR><TD>VENTAS</TD></TR>
<TR><TD>TECNOLOGIA</TD></TR>
<TR><TD>FABRICA</TD></TR>
<TR><TD rowspan='3'>tbempleadopuesto</TD><TD rowspan='3'>TABLA</TD><TD rowspan='3'>test</TD><TD rowspan='3'></TD><TD>idempleado:integer</TD></TR>
<TR><TD>idpuesto:integer</TD></TR>
<TR><TD>departamento:area</TD></TR>
<TR><TD rowspan='4'>tbventa</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>test</TD><TD rowspan='4'></TD><TD>idventa:integer</TD></TR>
<TR><TD>idempleado:integer</TD></TR>
<TR><TD>montoventa:money</TD></TR>
<TR><TD>ventaregistrada:boolean</TD></TR>
<TR><TD>C_test_tbventa_montoventa_ventavalida</TD><TD>CONSTRAINT CHECK</TD><TD>test</TD><TD>tbventa</TD><TD>montoventa &#62; 0</TD></TR>\n<TR><TD>PK_test_tbventa</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbventa</TD><TD>[0]</TD></TR><TR><TD rowspan='5'>employees</TD><TD rowspan='5'>TABLA</TD><TD rowspan='5'>test</TD><TD rowspan='5'></TD><TD>id:integer</TD></TR>
<TR><TD>first_name:varchar</TD></TR>
<TR><TD>last_name:varchar</TD></TR>
<TR><TD>salary:money</TD></TR>
<TR><TD>codarea:integer</TD></TR>
<TR><TD rowspan='2'>area</TD><TD rowspan='2'>TABLA</TD><TD rowspan='2'>test</TD><TD rowspan='2'></TD><TD>codigo:integer</TD></TR>
<TR><TD>nombre:varchar</TD></TR>
</TABLE>>]
}
