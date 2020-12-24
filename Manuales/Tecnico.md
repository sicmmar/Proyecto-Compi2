#### Universidad de San Carlos de Guatemala
#### Organización de Lenguajes y Compiladores 2 
#### Facultad de Ingeniería
#### Interprete TytusDB

## Introducción
El siguiente manual guiara a los usuarios que harán soporte al sistema, el cual les dará a
conocer los requerimientos y la estructura realizada para la construcción del sistema, en el desarrollo
de programa de escritorio, el cual muestra las herramientas necesarias para la construcción y la funcionalidad
del sistema.

## Objetivo
Informar y especificar al usuario la estructura y conformación del sistema con el fin de que
puedan hacer soporte y modificaciones o actualizaciones al sistema en general.

## Procesos
### Procesos de entrada
- Ingresar al programa de escritorio (acceso)
- Ingresar datos al programa para ejecutar el interprete
- Ingresar datos para para generación de reportes
- Ingresar o modificar información de la base de datos mediante los metodos INSERT, UPDATE, ALTER, DROP, CREATE y DELETE
- Ingresar al programa funciones matematicas, trigonometricas y binarias

### Procesos de salida
- Resultado de consultas a traves del SELECT
- Resultado de funciones matematicas, trigonometricas y binarias
- Reporte de arbol sintactico AST
- Reporte de errores lexicos
- Reporte de errores sintacticos
- Reporte de tabla de simbolos

## Requerimientos del sistema
### Requerimientos de hardware
- Equipo de computo; CPU, Teclado, Mouse y Monitor
- Memoria RAM 2GB o superior
- Procesador 1.4 GHz o superior
### Requerimientos de software
- Sistemas operativos (Windows 7/8/10 o Linux)
- Python 3
- Graphviz
- PLY



## Herramientas utilizadas para el desarrollo
### Python
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​ 
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y,
en menor medida, programación funcional.

### Visual Studio Code
Visual Studio Code es un editor de código fuente desarrollado por Microsoft para Windows, Linux y macOS. 
Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código.

## Analisis Lexico y Sintactico utilizando PLY
### Analisis Lexico
En el interprete tytusDB se implemento un analisis lexico utilizando la herramienta de PLY con las siguientes
consideraciones:
- **Expresiones regulares**
Una expresión regular, o expresión racional, ​​ también son conocidas como regex o regexp, ​ 
por su contracción de las palabras inglesas regular expression, es una secuencia de caracteres que conforma un patrón de búsqueda
```
int ::= digito+
decimales ::= digito+ "." digito+ (["e"] ["+"|"-""] digito+)?
id ::= [a-zA-Z_][a-zA-Z_0-9]*
cadena ::= """ "."*? """
cadenaString ::= "".*?""
```

- **Palabras Reservadas:**
Las palabras reservadas son aquellas que son propias del lenguaje y no pueden ser usadas para
nombrar etiquetas o variables.

| show   | database  | databases | like | select |
| ------ |---------| ---------| ---------| ------:|
| distinct | from  | alter  | rename | to |
| owner  | table    | add   | column | set |
| not | null | check   | constraint | unique |
| foreign | key | or   | replace | if |
| exists | mode | inherits   | primary | references |
| default | type | enum   | drop | update |
| where | smallint | integer   | bigint | decimal |
| double | precision | money   | character | varying |
| char | timestamp | without   | zone | date |
| time | interval | boolean   | true | false |
| year | month | day   | hour | minute |
| second | in | and   | between | symetric |
| isnull | notnull | unknown   | insert | into |
| values | group | by   | having | as |
| create | varchar | text   | is | delete |
| order | asc | desc   | when | case |
| else | then | end   | extract | current_time |
| current_date | any | all   | some | limit |
| offset | union | except   | intersect | with |
| use | int | tables   | collection |  |


- **Tokens:**
Son los caracteres que están permitidos dentro de nuestro lenguaje

| mas | menos   | elevado |
| ------ |---------| ------:|
| multiplicacion  | division   | modulo    |
| menor_igual  | mayor_igual    | diferente1   |
| diferente2 | ptcoma | para   |
| coma | int | decimales   |
| cadena | cadenastring | parc   |
| id | idpunto |    |

```
mas ::= "+"
menos ::= "-"
elevado ::= "^"
multiplicacion ::= "*"
division ::= "/"
modulo ::= "%"
menor ::= "<"
mayor ::= ">"
igual ::= "="
menor_igual ::= "<="
mayor_igual ::= ">="
diferente1 ::= "<>"
diferente2 ::= "!=""
para ::= "("
parc ::= ")"
ptcoma ::= ";"
coma ::= ","
punto ::= "."
```

- **Precedencia:**
Precedencia de operaciones para la producción de las expresiones

|Asociatividad|Símbolo|Descripción|
|:----------:|:-------------:|:---------:|
|Izquierda|```lsel```|Precedencia utilizada para los alias en la instrucción SELECT|
|Izquierda|```.```|Operador para separar atributos de una tabla|
|Derecha|```-,+```|Operador unario para números negativos y positivos|
|Izquierda|```^```|Potencia|
|Izquierda|```*,/,%```|Multiplicación, división y modular|
|Izquierda|```-,+```|Suma y Resta|
|Izquierda|```>,<,>=,<=,=,!=,<>```|Operaciones relacionales|
|Izquierda|```predicates```|Precedencia para predicados en consultas|
|Derecha|```NOT```|Negación lógica|
|Izquierda|```AND```|Operador AND lógico|
|Izquierda|```OR```| Operador OR lógico|

### Analisis Sintactico
En el interprete tytusDB se implemento un analisis sintactico utilizando la herramienta de PLY a traves de un analizador
ascendente utilizando la siguiente gramatica:
- [Ascendente](https://github.com/tytusdb/tytus/blob/main/parser/team14/Gramatica/ascendente.md)
- [Descendente](https://github.com/tytusdb/tytus/blob/main/parser/team14/Gramatica/descendente.md)

## Autores
### Grupo 14
* **Walter Josue Paredes Sol** - *201504326*
* **Asunción Mariana Sic Sor** - *201504051*
* **Wendy Aracely Chamalé Boch** - *201504284*
* **Carlos Eduardo Torres Caal** - *201504240*
