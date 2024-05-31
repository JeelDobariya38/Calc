from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()


environment = os.getenv("ENVIRONMENT")
host = os.getenv("HOST")
port = os.getenv("PORT")


if environment == "Development":
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
