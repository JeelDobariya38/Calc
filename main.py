from calc import calc_execute
from utils import print_help_msg
from customerr import CalcException
from sys import argv


def main():
    isquitted = False

    print("Welcome to Calc REPL!!!!!")
    print("Type 'help' for help")
    print()

    while not isquitted:
        try:
            code = input(">> ").strip()
            if code == "quit" or code == "exit":
                isquitted = True
                print()
            elif code[:4] == "help":
                context = code[5:]
                print_help_msg(context.strip())
            else:
                print(calc_execute(code))
        except CalcException as e:
            print(e)


if __name__ == "__main__":
    main()
