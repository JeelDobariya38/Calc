from .interpreter import Interpreter
from .lexer import Lexer
from .parser import Parser


def calc_execute(code):
    lexer = Lexer(code)
    tokens = lexer.tokonize()
    parser = Parser(tokens)
    parsetree = parser.parse()
    interpreter = Interpreter(parsetree)
    return interpreter.interpret()
