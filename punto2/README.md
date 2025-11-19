# Lenguaje para Producto Punto entre Matrices

Este proyecto define una gramática formal para un lenguaje sencillo cuyo propósito es permitir la declaración, construcción y multiplicación de matrices, incluyendo verificación de dimensiones y cálculo automático del producto punto.

El objetivo principal es modelar cómo un lenguaje puede describir matrices, operar con ellas y producir nuevos resultados, utilizando reglas sintácticas y semánticas claras.

## **Características del Lenguaje**

**El lenguaje permite:**

 - Declaración de matrices con dimensiones explícitas

Ejemplo:
```
matriz A[2,3] = [[1,2,3],[4,5,6]];
```
- Multiplicación de matrices usando el operador punto
```
C = A punto B;
```
- Impresión del resultado
```
  imprimir(C);
```
- Matrices literales anidadas con sintaxis estilo JSON
```
[[1,2],[3,4]]
```
## **Gramática del Lenguaje**
```
<programa>           ::= <lista_sentencias>

<lista_sentencias>   ::= <sentencia> ";" <lista_sentencias>
                       |  ε

<sentencia>          ::= <declaracion_matriz>
                       | <asignacion>
                       | <impresion>

<declaracion_matriz> ::= "matriz" identificador "[" <entero> "," <entero> "]" "=" <matriz_literal>
<asignacion>         ::= identificador "=" <expresion>
<impresion>          ::= "imprimir" "(" identificador ")"

<matriz_literal>     ::= "[" <lista_filas> "]"

<lista_filas>        ::= <fila> "," <lista_filas>
                       |  <fila>

<fila>               ::= "[" <lista_numeros> "]"

<lista_numeros>      ::= numero "," <lista_numeros>
                       | numero

<expresion>          ::= identificador
                       | <expresion> "punto" <expresion>
                       | <matriz_literal>

```
### **Semántica del Operador punto (Producto Punto)**

El operador punto implementa la multiplicación matricial clásica:
```
C = A punto B
```
se verifica:
```
columnas(A) == filas(B)
```
i la condición se cumple:

El resultado tiene
- filas = filas(A)
- columnas = columnas(B)

Cada elemento se calcula como:
```
C[i][j] = Σ ( A[i][k] * B[k][j] )
```
