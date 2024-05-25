from calc import repl_executor, script_executor
import sys
import os
from utils import print_help_msg, print_version
from colorama import Fore, Style


def warning():
    print(Fore.RED + "Calc is under it development version..")
    print("therefore, it can have bug and error..")
    print("if you encounter any, please kindly report them,")
    print("and have valuable place in calc development")
    print(Style.RESET_ALL+ "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()

def arg_parse():
    if len(sys.argv) >= 1:
        return sys.argv[1:]
    return False


def main():
    args = arg_parse()
    if args:
        if args[0].startswith("--"):
            if args[0] == "--version":
                print_version()
                return 0
            elif args[0] == "--help":
                print_help_msg()
                return 0
            else:
                raise ValueError(f"Invalid argument \"{args[0]}\"")
        else:
            return script_executor(args[0])
    else:
        return repl_executor()


if __name__ == "__main__":
    env = os.environ['Environment']
    if env == "Dev":
        warning()
    main()
