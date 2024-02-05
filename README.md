# 0x00. AirBnB clone - The console

# Welcome to the AirBnB clone project!
=pic

For this project, we expect you to look at these concepts:

* Python packages
* AirBnB clone

## AirBnB Clone - Command Line Interface (CLI)
## Project Description
Welcome to the AirBnB Clone project! This project aims to build a simple command-line interface (CLI) for managing AirBnB objects. The CLI allows users to perform various operations such as creating new objects, retrieving objects, updating attributes, and more.

## Command Interpreter

The command interpreter is a shell-like interface designed specifically for managing AirBnB objects. It enables users to interact with the system through a set of commands. Below, you'll find information on how to start and use the command interpreter.

### How to Start the Command Interpreter

To start the command interpreter, run the `console.py` script:

$ ./console.py

### How to Use the Command Interpreter
The command interpreter supports several commands for managing AirBnB objects. Here are some examples:

* Create a new object:
(hbnb) create User

* Retrieve an object:
(hbnb) show User 123
* Update attributes of an object:
(hbnb) update Place 456 name "New Place Name"

* Destroy an object:
(hbnb) destroy State 789

* Exit the command interpreter:
(hbnb) quit

# Requirements
* Python 3.8.5
* pycodestyle (version 2.8.*)

# Project Structure
i) console.py: Main script for the command interpreter.
ii) models/: Folder containing classes for AirBnB objects.
iii) tests/: Folder for unit tests.

# Running Tests
Execute all tests using the following command:
$ echo "python3 -m unittest discover tests" | bash

# More Info
## Execution
Your shell should work like this in interactive mode:
=pic


But also in non-interactive mode: (like the Shell project in C)
=pic


All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
=pic
