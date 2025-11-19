from MatricesVisitor import MatricesVisitor
from MatricesParser import MatricesParser

class MatricesVisitorExec(MatricesVisitor):

    def __init__(self):
        self.matriz = {}  # Diccionario de matrices

    # ------------------------------
    # Declaración de matrices
    # ------------------------------
    def visitDecl_matriz(self, ctx):
        nombre = ctx.ID().getText()
        filas = int(ctx.INT(0).getText())
        columnas = int(ctx.INT(1).getText())
        literal = ctx.matriz_literal()
        matriz = self._leer_literal(literal)

        # Validar dimensiones
        if len(matriz) != filas or len(matriz[0]) != columnas:
            raise Exception(f"Dimensiones no coinciden para {nombre}")

        self.matriz[nombre] = matriz
        return None

    # ------------------------------
    # Asignación de matriz
    # ------------------------------
    def visitAsignacion_matriz(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.matriz[nombre] = valor
        return None

    # ------------------------------
    # Imprimir matriz
    # ------------------------------
    def visitImprimir(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.matriz:
            raise Exception(f"Matriz {nombre} no existe")

        print("\nMatriz", nombre)
        for fila in self.matriz[nombre]:
            print(fila)
        print()
        return None

    # ------------------------------
    # Expresiones
    # ------------------------------
    def visitSoloID(self, ctx):
        nombre = ctx.ID().getText()
        return self.matriz[nombre]

    def visitProductoPunto(self, ctx):
        A = self.matriz[ctx.ID(0).getText()]
        B = self.matriz[ctx.ID(1).getText()]
        return self._multiplicar(A, B)

    # ------------------------------
    # Helpers
    # ------------------------------

    def _leer_literal(self, ctx):
        filas = []
        for f in ctx.fila():
            valores = [int(n.getText()) for n in f.INT()]
            filas.append(valores)
        return filas

    def _multiplicar(self, A, B):
        filasA = len(A)
        colA = len(A[0])
        filasB = len(B)
        colB = len(B[0])

        if colA != filasB:
            raise Exception("Dimensiones incompatibles para producto punto")

        # Resultado vacío
        R = [[0] * colB for _ in range(filasA)]

        # Multiplicación clásica
        for i in range(filasA):
            for j in range(colB):
                for k in range(colA):
                    R[i][j] += A[i][k] * B[k][j]

        return R
