from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor


while True:
    input_stream = InputStream(input('$> '))
    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)

    tree = parser.root() 
    visitor = TreeVisitor()
    visitor.visit(tree)