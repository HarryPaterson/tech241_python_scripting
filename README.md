<h1 style="text-align: center;">Scripting</h1>

### Contents
* Basics
* Os Module
* Shell execution


### Basics


Scripting in Python refers to the process of writing and executing scripts using Python. Python is a high-level, interpreted language that prioritizes code readability and simplicity. It provides a rich set of built-in functions and libraries, making it well-suited for scripting tasks such as automation and managing configurations.

#### The 7 Core Modules
```
# Basics of scripting in Python

# Libraries and Modules - Libraries bigger, Modules smaller

# Seven "core" modules in Python

import sys

# Get Python version
print(sys.version)

import os

# Get current working directory
print(os.getcwd())

import subprocess

subprocess.run(["python", "hello_world.py"])

import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

import random

random = random.randrange(1, 10)
print(random)

import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

import json

x = {
    "name": "John",
    "age": 30,
    "city": "Liverpool"
}

y = json.dumps(x)

print(y)
```

### Os Module


In Python, the os module is a built-in module that provides functions and methods for interacting with the operating system. It allows you to perform various operating system-related tasks, such as file and directory operations, process management, environment variables, and more.

#### Example 
```
# Using os to do things

import os

# Echo to the terminal
# os.system('echo "Hello world!"')

# make and change directories

# create a directory


# Directory name
directory = "test_dir"

# Parent directory
parent_dir = "C:/Users/User"

# Path
path = os.path.join(parent_dir, directory)

# os.mkdir(path)

# Putting a new file in the new dir

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is wrriten here"
    file1.write(toFile)

print("File " + filename + " created in " + directory + " folder")
```

### Shell execution

Shell execution in  refers to the ability to run shell commands or execute shell scripts from within a Python program. It allows you to interact with the command-line interface of the underlying operating system, execute system commands, and capture their output or handle their execution results.

#### Example
```
import os
import subprocess

# Stores the file path to the current file
script_dir = os.path.dirname(__file__)

# Stores the filepath to the script you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")

# Calls the shell file and runs it
subprocess.call(['sh', script_absolute_path])
```