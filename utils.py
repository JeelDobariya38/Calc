APPNAME = "Calc"
VERSION = "0.1.0"

def print_avaliable_commands():
    print("Available commands: ")
    print(" - quit, \n - exit, \n - help")

def print_help_msg(context = ""):
    if context == "quit" or context == "exit":
        print(f"Command \"quit\" and \"exit\" are use to exit {APPNAME}!!")
    elif context == "version":
        print(f"{APPNAME} v{VERSION}")
    elif context == "command":
        print_avaliable_commands()
    else:
        print(f"{APPNAME} | v{VERSION}")
        print()
        print("Useage: for automatic math related tasks..")
        print()
        print("Commands: ")
        print("\t  - <expression> = to evaluate an expression")
        print("\t  - help = for printing help message")
        print("\t  - quit | exit = for adding two numbers")
        print()
