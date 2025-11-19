grammar Matrices;

programa
    :   lista_sentencias EOF
    ;

lista_sentencias
    :   sentencia*
    ;

sentencia
    :   decl_matriz ';'
    |   asignacion_matriz ';'
    |   imprimir ';'
    ;

decl_matriz
    :   'matriz' ID '[' INT ',' INT ']' '=' matriz_literal
    ;

asignacion_matriz
    :   'matriz' ID '=' expr
    |   ID '=' expr
    ;

imprimir
    :   'imprimir' '(' ID ')'
    ;

expr
    :   ID 'punto' ID         #productoPunto
    |   ID                    #soloID
    ;

matriz_literal
    :   '[' fila (',' fila)* ']'
    ;

fila
    :   '[' INT (',' INT)* ']'
    ;

ID  :   [a-zA-Z_] [a-zA-Z0-9_]* ;
INT :   [0-9]+ ;

WS  :   [ \t\r\n]+ -> skip ;
