from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from os import path
from utils import print_help_msg
from customerr import CalcException


def read_code(scriptname):
    with open(scriptname) as script:
        return script.readlines()


def calc_execute(code):
    lexer = Lexer(code)
    tokens = lexer.tokonize()
    print("tokens:", tokens)
    print()
    parser = Parser(tokens)
    parsetree = parser.parse()
    print("Tree:", parsetree)
    interpreter = Interpreter(parsetree)
    return interpreter.interpret()


def script_executor(scriptname): # TODO: add feature of read and executing script
    if path.exists(scriptname):
        codelines = read_code(scriptname)
        for codeline in codelines:
            calc_execute(codeline)
    else:
        raise CalcException(f"Script \"{scriptname}\" not found!!")


def repl_executor():
    print("Welcome to Calc REPL!!!!!")
    print("Type 'help' for help")
    print()

    while True:
        try:
            code = input(">> ").strip()
            if code == "quit" or code == "exit":
                print()
                return 0
            elif code[:4] == "help":
                context = code[5:]
                print_help_msg(context.strip())
            else:
                print(calc_execute(code))
        except CalcException as e:
            print(e)
