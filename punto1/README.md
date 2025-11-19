# **Generación de una Gramática de Atributos para un Lenguaje SQL (CRUD)**

1. ## **Fundamentos del Diseño**
### Gramática de Atributos

Una gramática de atributos extiende una gramática libre de contexto agregando:

- Atributos sintácticos y semánticos

- Acciones semánticas para calcular los atributos

- Propagación y dependencia entre símbolos

En este caso se usan atributos como:

- codigo → instrucción SQL generada

- lista → lista de campos

- nombre → nombre de tabla

- exp → expresión de condición

**ETDS (Esquema de Traducción Dirigido por la Sintaxis)**

El ETDS se construye añadiendo acciones semánticas incrustadas en las reglas de producción.
Estas acciones permiten ensamblar consultas SQL durante el análisis sintáctico.

Ejemplo conceptual:
```
Select → "SELECT" Campos "FROM" Tabla Condicion
    { Select.codigo = "SELECT " + Campos.lista + " FROM " + Tabla.nombre + Condicion.exp }
 ```
2. ## **Función Generadora — Modelo Solicitado**
El proyecto se basa en una función que sigue el formato:

Eje(x, y, z): return Result
En este contexto:

- x = operaciones CRUD

- y = atributos asociados

- z = reglas del ETDS
## **Implementación del modelo**
```
def Eje(operaciones, atributos, reglas):
    """
    Construye la gramática de atributos para un lenguaje con consultas SQL CRUD.

    operaciones: lista de comandos CRUD soportados.
    atributos: conjunto de atributos sintácticos y semánticos.
    reglas: producciones con acciones semánticas (ETDS).

    return: estructura que representa la gramática completa.
    """

    gramatica = {
        "operaciones": operaciones,
        "atributos": atributos,
        "reglas": reglas
    }

    return gramatica
```
La función devuelve una estructura formal que representa la gramática completa.

3. ## **Diseño de la Gramática de Atributos**
A continuación se presenta el diseño completo de la gramática que permite procesar operaciones SQL tipo CRUD.
Los atributos se calculan mediante reglas semánticas integradas.

### **No terminales definidos**
- Consulta

- Select

- Insert

- Update

- Delete

- Campos

- Tabla

- Condicion
  
**Atributos usados**
  
| Símbolo     | Atributo | Función                  |
| ----------- | -------- | ------------------------ |
| `Consulta`  | `codigo` | Código SQL completo      |
| `Select`    | `codigo` | Consulta SELECT generada |
| `Insert`    | `codigo` | Consulta INSERT          |
| `Update`    | `codigo` | Consulta UPDATE          |
| `Delete`    | `codigo` | Consulta DELETE          |
| `Campos`    | `lista`  | Lista de campos          |
| `Tabla`     | `nombre` | Nombre de la tabla       |
| `Condicion` | `exp`    | Condición WHERE          |

**Producciones con Acciones Semánticas (ETDS)**
Inicio
```
Consulta → Select
    { Consulta.codigo = Select.codigo }

Consulta → Insert
    { Consulta.codigo = Insert.codigo }

Consulta → Update
    { Consulta.codigo = Update.codigo }

Consulta → Delete
    { Consulta.codigo = Delete.codigo }
```
SELECT
```
Select → "SELECT" Campos "FROM" Tabla Condicion
    { Select.codigo = "SELECT " + Campos.lista + 
                      " FROM " + Tabla.nombre + 
                      Condicion.exp }
```
INSERT
```
Insert → "INSERT INTO" Tabla "(" Campos ")" 
         "VALUES" "(" Valores ")"
    { Insert.codigo = "INSERT INTO " + Tabla.nombre +
                      "(" + Campos.lista + ") VALUES (" +
                      Valores.lista + ")" }
```
UPDATE
```
Update → "UPDATE" Tabla "SET" Asignaciones Condicion
    { Update.codigo = "UPDATE " + Tabla.nombre +
                      " SET " + Asignaciones.lista +
                      Condicion.exp }
```
DELETE
```
Delete → "DELETE FROM" Tabla Condicion
    { Delete.codigo = "DELETE FROM " + Tabla.nombre +
                      Condicion.exp }
```
Producciones auxiliares
```
Campos → Campo
    { Campos.lista = Campo.nombre }

Campos → Campo "," Campos
    { Campos.lista = Campo.nombre + "," + Campos.lista }
```
```
Tabla → id
    { Tabla.nombre = id.lexema }
```
```
Condicion → "WHERE" Exp
    { Condicion.exp = " WHERE " + Exp.codigo }

Condicion → ε
    { Condicion.exp = "" }
```
4. ### **Ejemplo de Construcción con la Función Eje**
```
gramaticaCRUD = Eje(
    operaciones=["SELECT", "INSERT", "UPDATE", "DELETE"],
    atributos=["codigo", "lista", "nombre", "exp"],
    reglas=[
        "Consulta → Select | Insert | Update | Delete",
        "Select → 'SELECT' Campos 'FROM' Tabla Condicion",
        "Insert → 'INSERT INTO' Tabla '(' Campos ')' 'VALUES' '(' Valores ')'",
        "Update → 'UPDATE' Tabla 'SET' Asignaciones Condicion",
        "Delete → 'DELETE FROM' Tabla Condicion"
    ]
)
```
Esto construye la estructura necesaria para el analizador y el traductor dirigido por sintaxis.
5. ### **Ejemplo de Traducción Sintáctica**
Entrada del lenguaje:
```
SELECT nombre,edad FROM usuarios WHERE edad > 18
```
SELECT nombre,edad FROM usuarios WHERE edad > 18
```
SELECT nombre,edad FROM usuarios WHERE edad > 18
```
## Conclusión

Este proyecto implementa:

✔ La función modelo solicitada
✔ Una gramática de atributos completa
✔ Un ETDS funcional
✔ El diseño conceptual necesario para justificar la solución
✔ Producciones CRUD correctamente definidas
✔ Un ejemplo práctico de uso

