# -----------------------------------------------------------------------------
# Rainman Sián
# 26-02-2020
#
# Ejemplo interprete sencillo con Python utilizando ply en Ubuntu
# -----------------------------------------------------------------------------

reservadas = {
    'show': 'show',
    'databases': 'databases',
    'select': 'select',
    'distinct': 'distinct',
    'from': 'from',
    'alter': 'alter',
    ' rename': 'rename',
    'to': 'to',
    'owner': 'owner',
    'table': 'table',
    'add': 'add',
    'column': 'column',
    'set': 'set',
    'not': 'not',
    'null': 'null',
    'check': 'check',
    'constraint': 'constraint',
    'unique': 'unique',
    'foreign': 'foreign',
    'key': 'key',
    'or': 'or',
    'replace': 'replace',
    'if': 'if',
    'exist': 'exist',
    'mode': 'mode',
    'inherits': 'inherits',
    'primary': 'primary',
    'references': 'references',
    'default': 'default',
    'type': 'type',
    'enum': 'enum',
    'drop': 'drop',
    'update': 'update',
    'where': 'where',
    'smallint': 'smallint',
    'integer': 'integer',
    'bigint': 'bigint',
    'decimal': 'decimal',
    'numeric': 'numeric',
    'real': 'real',
    'double': 'double',
    'precision': 'precision',
    'money': 'money',
    'character': 'character',
    'varyng': 'varyng',
    'char': 'char',
    'timestamp': 'timestamp',
    'without': 'without',
    'zone': 'zone',
    'date': 'date',
    'time': 'time',
    'interval': 'interval',
    'boolean': 'boolean',
    'true': 'true',
    'false': 'false',
    'year': 'year',
    'month': 'month',
    'day': 'day',
    'hour': 'hour',
    'minute': 'minute',
    'second': 'second',
    'in': 'in',
    'like': 'like',
    'ilike': 'ilike',
    'similar': 'similar',
    'and': 'and',
    'between': 'between',
    'symetric': 'symetric',
    'isnull': 'isnull',
    'notnull': 'notnull',
    'unknown': 'unknown',
    'insert': 'insert',
    'into': 'into',
    'values': 'values',
    'group': 'group',
    'by': 'by',
    'having': 'having'
}

tokens = [
             'mas',
             'menos',
             'elevado',
             'multiplicacion',
             'division',
             'modulo',
             'menor',
             'mayor',
             'igual',
             'menor_igual',
             'mayor_igual',
             'diferente1',
             'diferente2',
             'ptcoma',
             'llavea',
             'llavec',
             'para',
             'parac',
             'dospuntos',
             'coma',
             'punto',
             'int',
             'decimal',
             'varchar',
             'char',
             'parc',
             'simboloor',
             'id'
         ] + list(reservadas.values())

# Tokens
t_mas = r'\+'
t_menos = r'-'
t_elevado = r'\^'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_menor = r'<'
t_mayor = r'>'
t_igual = r'='
t_menor_igual = r'<='
t_mayor_igual = r'>='
t_diferente1 = r'<>'
t_diferente2 = r'!='
t_simboloor = r'\|'
t_llavea = r'{'
t_llavec = r'}'
t_para = r'\('
t_parc = r'\)'
t_ptcoma = r';'
t_dospuntos = r':'
t_coma = r','
t_punto = r'\.'


def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')
    return t


def t_varchar(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'punto'),
    ('left', 'mas', 'menos'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
)

# ----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática


def p_init(t):
    'init            : instrucciones'


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '


def p_instruccion(t):
    '''instruccion      : SELECT '''


def p_SELECT(t):
    ''' SELECT : select distinct  LEXP from LFROM WHERE
	          | select  LEXP from LFROM WHERE
	'''


def p_LFROM(t):
    '''LFROM : LEXP
	        |  para SELECT parc
'''


def p_WHERE(t):
    ''' WHERE : where EXP ptcoma
                | where EXP GROUP
	            | GROUP'''


def p_GROUP(t):
    ''' GROUP :  group by EXP HAVING ptcoma
	            | HAVING'''


def p_HAVING(t):
    ''' HAVING : having EXP
	| ptcoma '''


def p_LEXP(t):
    '''LEXP : LEXP coma EXP
	| EXP
	| multiplicacion'''


def p_EXP(t):
    '''EXP : EXP mas EXP
            | EXP menos EXP
            | EXP multiplicacion  EXP
            | EXP division EXP
            | EXP modulo EXP
            | EXP elevado EXP
            | EXP and EXP
            | EXP or EXP
            | EXP mayor EXP
            | EXP menor EXP
            | EXP mayor_igual EXP
            | EXP menor_igual EXP
            | EXP igual EXP
            | EXP diferente1 EXP
            | EXP diferente2 EXP
            | EXP punto EXP
            | mas EXP
            | menos EXP
            | not EXP 
            | para EXP parc 
            | int
            | decimal
            | varchar
            | char
            | true
            | false
            | id'''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)

#commit :)