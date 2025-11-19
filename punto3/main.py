import sys
from antlr4 import *
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser
from MatricesVisitorExec import MatricesVisitorExec

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.txt")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf8')
    lexer = MatricesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MatricesParser(stream)
    tree = parser.programa()

    visitor = MatricesVisitorExec()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
