# Lenguaje para Producto Punto entre Matrices (ANTLR + Python)

Este proyecto implementa un lenguaje de programación personalizado, diseñado para declarar matrices, asignar valores y realizar el producto punto (multiplicación matricial) entre matrices de cualquier dimensión compatible.

El lenguaje se implementa con:

- ANTLR4 – para la construcción del Lexer y Parser

- Python (Visitor) – para ejecutar las operaciones semánticas

- Gramática Matrices.g4 – define toda la sintaxis del lenguaje

El objetivo es ofrecer un lenguaje simple que permita escribir programas como:
```
matriz A[2,3] = [[1,2,3],[4,5,6]];
matriz B[3,2] = [[7,8],[9,10],[11,12]];
matriz C = A punto B;
imprimir(C);

```
Resultado
```
Matriz C
[58, 64]
[139, 154]

```
### Estructura del Lenguaje
Declaración de matrices
```
matriz A[filas,columnas] = [[...],[...],...];
```
Producto punto
```
matriz C = A punto B;

```
Impresión
```
imprimir(C);
```
## **Gramática utilizada – Matrices.g4**

La gramática define:

- Declaraciones de matrices

- Dimensiones

- Literales matriciales

- Operación punto

- Comando imprimir

- Asignaciones

El parser se genera con:
```
antlr4 -Dlanguage=Python3 -visitor Matrices.g4
```
Instalar ANTLR en Linux:
```
sudo apt install antlr4
```
## Cómo ejecutar el proyecto
1. Crear entorno virtual 
```
python3 -m venv venv
source venv/bin/activate
```
2. Generar los archivos de ANTLR
Debes usar la flag -visitor:
```
antlr4 -Dlanguage=Python3 -visitor Matrices.g4
```
3. Ejecutar el programa con un archivo de entrada
```
python main.py test.txt
```

# EJEMPLO
<img width="1920" height="1080" alt="Screenshot_2025-11-19_20_21_01" src="https://github.com/user-attachments/assets/a2584d9a-37a9-4503-b219-1b6dc4361c17" />




