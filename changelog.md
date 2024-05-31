# Changelog

## v0.1.0 - Initial Release

### Added

- **CLI Version (`jeeldobariya2325/calc:v0.1.0-cli`):**

  - Basic REPL for Basic mathematical expressions.
  - Command-line interface for direct input and evaluation of math expressions.

- **Backend API Version (`jeeldobariya2325/calc:v0.1.0-backend`):**

  - HTTP API to evaluate mathematical expressions via POST requests.
  - Server setup using Uvicorn.

### Features

- **Command Line Interface (CLI):**

  - Directly input and evaluate mathematical expressions from the terminal.

- **HTTP API:**

  - Send mathematical expressions to the server and receive evaluated results.
  - API endpoint: `/evaluate` for POST requests with math expressions.

### Installation Options

- **Local Installation:**

  - Clone the repository and set up locally with Python 3.10+ and Git.
  - Install dependencies via `pip` and run the REPL or the API.

- **Docker Installation:**

  - Build and run Docker images for CLI, backend, and frontend.
  - Separate tags for CLI (`latest-cli`), backend (`latest-backend`)

- **Pythonic Installation (using pip):**
  - Install directly from the Git repository.
  - Run the CLI tool from the terminal.

### Notes

- Ensure Docker Desktop is installed for containerized setups.
- Python 3.10 or above is required for local and pip installations.
- For development, clone the repository and build the Docker images as needed.
- Access the web frontend at `http://localhost:8080` when running the frontend Docker container.

---

## Future Releases

### Planned Features

- Enhanced error handling for mathematical expressions.
- Additional mathematical functions and operations.
- Improved web frontend interface with more features.
- Detailed documentation and usage examples.
