import colorama
import os
from calc import run_cli
from dotenv import load_dotenv
import uvicorn

load_dotenv()


def warning():
    print(colorama.Fore.RED + "Calc is under it development version..")
    print("therefore, it can have bug and error..")
    print("if, you encounter any, please kindly report them (on github),")
    print("and have valuable place in calc development process")
    print(colorama.Style.RESET_ALL + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()


if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    climode = os.getenv("CLI_MODE")

    if environment == "Development":
        warning()

    if climode:
        run_cli()

    elif environment == "Development":
        if not port:
            port = 8000

        try:
            uvicorn.run("api.app:app", host="127.0.0.1", port=int(port), log_level="info")
        except KeyboardInterrupt:
            print("Quitting the server!!!")

    else:
        if not host:
            host = "0.0.0.0"

        if not port:
            port = 80
        try:
            uvicorn.run("api.app:app", host=host, port=int(port), log_level="info")
        except KeyboardInterrupt:
            print("Quitting the server!!!")
