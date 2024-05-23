APPNAME = "Calc"
VERSION = "0.1.0"

def print_avaliable_commands():
    print("Available commands: ")
    print(" - quit, \n - exit, \n - help")

def print_version():
    print(f"{APPNAME} v{VERSION}")

def print_help_msg(context = ""):
    if context == "quit" or context == "exit":
        print(f"Command \"quit\" and \"exit\" are use to exit {APPNAME}!!")
    elif context == "version":
        print_version()
    elif context == "command":
        print_avaliable_commands()
    else:
        print(f"{APPNAME} | v{VERSION}")
        print()
        print("Useage: python main.py <script>.calc")
        print(" OR ")
        print("Useage: calc <script>.calc")
        print()
        print("args: ")
        print("\t  --version      :- to evaluate an expression")
        print("\t  --help [args]  :- for printing help message")
