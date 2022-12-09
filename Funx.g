grammar Funx;
root : expr EOF ;

comp : VAR ('=' | '!=' | '<'| '>' | '<=' | '>=') (NUM | VAR)    # Igualtat
;

cond : 'if' comp '{' expr '}' ('else' '{' expr '}')*            # Condicional
;

while : 'while' comp '{' (expr)* '}'                            # Iteracio
;

funcio : NOM_FUN (VAR)* '{' (expr)* '}'                         # DecFuncio
;

evalFuncio :  NOM_FUN (expr)*                                   # EvFuncio
;

expr 
     : '(' expr ')'                 # ParentExpr
     | COMMENT                      # Comment 
     | expr MUL expr                # Multiplicacio
     | expr DIV expr                # Divisio
     | <assoc=right> expr POT expr  # Potencia
     | expr SUM expr                # Suma
     | expr RES expr                # Resta
     | NUM                          # Valor
     | funcio                       # DecFuncioInput
     | evalFuncio                   # EvFuncioInput
     | while                        # IteracioInput
     | VAR '<-' expr                # Assignacio
     | comp                         # IgualtatInput
     | cond                         # CondicionalInput
     | VAR                          # Variable
     ;


NOM_FUN : [A-Z]+[a-zA-Z]+DIGIT* ;
VAR : ALPHA ( ALPHA | DIGIT )*;
NUM : [0-9]+ ;
MUL : '*' ;
DIV : '/' ;
POT : '^' ;
SUM : '+' ;
RES : '-' ;
DIGIT: [0-9];
ALPHA: [a-zA-Z_];
ASS : '<-' ;
COMMENT : '#' ~[\r\n]*;


WS  : [ \n]+ -> skip ;