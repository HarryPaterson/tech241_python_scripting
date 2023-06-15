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