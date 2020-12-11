> # Gramática Descendente
```
INIT ::= INSTRUCCIONES

INSTRUCCIONES ::= INSTRUCCION INSTRUCCIONES'

INSTRUCCIONES' ::= INSTRUCCION INSTRUCCIONES'
            | Ɛ

INSTRUCCION ::= SELECT ptcoma
            | CREATETABLE
            | UPDATE ptcoma
            | DELETE ptcoma
            | ALTER ptcoma
            | DROP ptcoma
            | INSERT ptcoma
            | CREATETYPE ptcoma
            | CASE
            | CREATEDB ptcoma
            | SHOWDB ptcoma

CASE ::= case LISTAWHEN ELSE end
        | case LISTAWHEN end

LISTAWHEN ::= WHEN LISTAWHEN'

LISTAWHEN' ::= WHEN LISTAWHEN'
            | Ɛ

WHEN : when LEXP then LEXP

ELSE ::= else LEXP

INSERT ::= insert into id values para LEXP parc

DROP ::= drop table id
        | drop databases if exist id
        | drop databases id

ALTER ::= alter databases id RO
        | ALTERTABLE

RO ::= rename to id
        | owner to id

ALTERTABLE ::= alter table id OP

OP ::= add ADD
    | drop column ALTERDROP
    | alter column id set not null
    | alter column id set null
    | LISTAALC
    | drop ALTERDROP
    | rename column id to id

LISTAALC ::= ALC LISTAALC'

LISTAALC' ::= coma ALC LISTAALC'
            | Ɛ

ALC ::= alter column id type TIPO

ALTERDROP ::= constraint id
            | column LEXP
            | check id
```