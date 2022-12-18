grammar Funx;
root : expr EOF ;

expr : COMMENT                                             # Comment
     | '(' expr ')'                                        # ParentExpr
     | expr MUL expr                                       # Multiplicacio
     | expr DIV expr                                       # Divisio
     | <assoc=right> expr POT expr                         # Potencia
     | expr SUM expr                                       # Suma
     | expr RES expr                                       # Resta
     | 'while' expr '{' (expr)* '}'                        # Iteracio
     | expr  ('=' | '!=' | '<'| '>' | '<=' | '>=') expr    # Igualtat
     | 'if' expr '{' expr '}' ('else' '{' expr '}')*       # Condicional
     | NOM_FUN (VAR)* '{' (expr)* '}'                      # DecFuncio
     | NOM_FUN (expr)*                                     # EvFuncio
     | VAR '<-' expr                                       # Assignacio
     | NUM                                                 # Valor
     | VAR                                                 # Variable
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
COMMENT : '#' ~[\r\n]*;

WS : [ \n]+ -> skip ;