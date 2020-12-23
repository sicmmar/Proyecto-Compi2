digraph TablaSym {
	node [shape=record]
	TS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>NOMBRE</TD><TD>TIPO</TD><TD>BASE DE DATOS</TD><TD>TABLA</TD><TD>VALOR</TD></TR><TR><TD rowspan='4'>tbpuesto</TD><TD rowspan='4'>TABLA</TD><TD rowspan='4'>test</TD><TD rowspan='4'></TD><TD>idpuesto:smallint</TD></TR>
<TR><TD>puesto:character</TD></TR>
<TR><TD>salariobase:money</TD></TR>
<TR><TD>tinecomision:boolean</TD></TR>
<TR><TD>PK_test_tbpuesto</TD><TD>CONSTRAINT PRIMARIA</TD><TD>test</TD><TD>tbpuesto</TD><TD>[0]</TD></TR><TR><TD>U_test_tbpuesto_puesto_c54</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbpuesto</TD><TD>puesto</TD></TR>

<TR><TD>U_test_tbpuesto_salariobase_c54</TD><TD>UNIQUE</TD><TD>test</TD><TD>tbpuesto</TD><TD>salariobase</TD></TR>

</TABLE>>]
}
