# Calc - Math Interpreter

## Overview

Calc is a math interpreter designed to help you with your math homework.

## Installation

**App Requires**: Python 3.10+

You can install Calc in three ways:

1. **Install Locally**
2. **Install Containerizedly** [Recommended for professional use]
3. **Install Pythonically** [Recommended for aspiring developers]

### Install Locally

**Installer Requirements:** Python (3.10+) & Git

1. Set up Git & GitHub for cloning a repository locally.
   ```bash
   git --version
   ```

2. Clone the repository locally by running:

   - It's recommended to run this command in a separate directory.

   ```bash
   git clone https://github.com/JeelDobariya38/Calc.git
   ```

3. Set up Python 3.10 or above on your machine.
   ```bash
   python --version
   ```

4. Run the REPL of Calc:
   ```bash
   python main.py
   ```

### Install Containerizedly (Using Docker) [for advanced users]

**Installer Requirements:** Docker Desktop

#### For Development Use (only valid for developers)

1. Set up Git and Docker Desktop for cloning and spinning containers.
   ```bash
   git --version
   docker --version
   ```

2. Clone the repository.
   ```bash
   git clone https://github.com/JeelDobariya38/Calc.git
   ```

3. Goto Calc Directory.
   ```bash
   cd Calc
   ```

4. Build the image.
   ```bash
   docker build -t calc .
   ```

5. Spin a container from the newly built image.
   ```bash
   docker run -it -p 8000:8000 --name calc_app calc
   ```

#### For Production Use (for final production usage)

**Currently not supported**

### Install Pythonically (Using pip or any other package manager) [for beginner users]

**Installer Requirements:** Python (^3.10), pip & Git

1. Set up Python3.10 and Git.
   ```bash
   git --version
   python --version
   pip --version
   ```

2. Install the package from the Git repository:
   ```bash
   pip install git+https://github.com/JeelDobariya38/Calc.git
   ```

3. Run the CLI tool from the terminal:
   ```bash
   calc
   ```

## Report Bugs

If you encounter any bugs or have any questions related to Calc, feel free to create an issue on our GitHub repository.

If you have any feature requests or want to contribute, feel free to create an issue or pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt).
