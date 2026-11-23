print("****************************************************************************************************")
print("overview")
print("****************************************************************************************************")

# google provides a style guide
#    location:  https://google.github.io/styleguide/pyguide.html
#    - 4 spaces for indentation
#    - snake case for function names
#    - 80 characters maximum for line length


print('****************************************************************************************************')
print('io')
print('****************************************************************************************************')

# input
user = input('Enter your name: ')

# output
word1 = 'Hello '
print(f"{word1}{user}")

print('****************************************************************************************************')
print('types')
print('****************************************************************************************************')

from collections.abc import Iterable

#
# types - common
#

# an integer - <class 'int'>
# both are integers
i1 = 4
i2 = (4)
print(type(i1))
print(type(i2))

# a float - <class 'float'>
f = 4.0
print(type(f))

# a string - <class 'str'>
s = 'test'
print(type(s))

# an boolean - <class 'bool'>
b = True
print(type(b))

# a complex number - <class 'complex'>
c = 1 + 2j
print(type(c))

#
# types - composite
#

# a tuple - <class 'tuple'>,
tuple1 = (4, 2)

# comma is required to make this a tuple, compare to above
tuple2 = (4, )
print(type(tuple1))
print(type(tuple2))

# a dynamic array - <class 'list'>
list1 = [0]
print(type(list1))

# a hash table - <class 'dict'>
dict1 = {'a': 0}
print(type(dict1))

# a set - <class 'set'>
set1 = {1, 2, 3}
print(type(set1))

# set along with many others is a child class of Iterable
print('Is set an iterable?', isinstance(set1, Iterable))

#
# type annotations
#

# type annotaions - colloquially referred to as type hints
def add(a: int, b: int) -> int:
    return a + b
result: int = add(2, 3)
print(result)

print('****************************************************************************************************')
print('functions')
print('****************************************************************************************************')

# basic function definition
def print_hello(text):
  print(text)
print_hello('Hi')

# default parameter
def print_default(greeting = 'Hello'):
  print(greeting)
print_default()

# special attributes are enclosed by __
def special(a = 1, b = 2):
    ''' I am a docstring '''
    # print('__name__:', __name__)
    print(special.__doc__)
    print(special.__defaults__)
    # print(special.__code__)
special()

# lambda example
words = ["apple", "pie", "banana", "fig"]
sorted_words = sorted(words, key=lambda s: len(s))
print(sorted_words)  # ['pie', 'fig', 'apple', 'banana']

# function in function
def function1():
  def f(x): return 2 * x
  print(f(2))
function1()

# a variadic function accepts a variable number of arguments
# positional arguments (1, 2) must come before keyword arguments {'y':4,'x':3} in the function call
def f(*args, **kwargs):
    print(args)
    print(kwargs)

f(1,2, y=4, x=3)

print('****************************************************************************************************')
print('lists')
print('****************************************************************************************************')

words = ['amelia', 'harper', 'evelyn', 'chris', 'james', 'brian']
words1 = words[:2]     # index 0 to 1
words2 = words[2:]     # index 2 to end
print('original: ', words)           # words has not changed
print('split element 0 to 1: ', words1)
print('split element 2 to END: ', words2)

# common methods - append, pop
words.append('fabio')
print('append fabio: ', words)
print('pop fabio: ', words.pop())
print('back to original', words)

# common methods - sort
# use sort if you want to create a new list
words.sort()
print('sort original', words)

# common methods - remove
words.remove('amelia')
print('removed amelia', words)

# list comprehension - [ <return> for <value> in <Iterable> ]
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
# squares → [1, 4, 9, 16]

#
# generator objects
#

# this is a generator expression; it generates squares of numbers 1 to 5
# 1, 4, 9, 16 
squares = (x**2 for x in range(1, 6))

# prints <generator object <genexpr> at 0x778a156d9e50>
print(squares)

# prints <class 'generator'>
print(type(squares))

# values are not computed until sum is executed
# this saves memory as compared to a list comprehension
# squares is an iterator object and requires compatability
print('generator example',sum(squares))

print('****************************************************************************************************')
print('strings-excerpt')
print('****************************************************************************************************')


import textwrap


input_text = textwrap.dedent(
"""
    Summary of changes:
    - Updated auth middleware

    [STUB] Skipping external webhook
    - Added unit tests for token expiry
    - 4 empty lines below




""")

# taken from mvf
def _excerpt(text: str, max_lines: int = 30) -> str:
    # original input
    print('INPUT: \n\n', input_text)

    # strip
    stripped = text.strip()
    print('STRIPPED: \n\n', stripped)

    # create a list
    lines = stripped.splitlines()
    print('LINES: \n\n', lines)

    # remove stubs and ...
    meaningful = [l for l in lines if l.strip() and not l.startswith("[STUB]")]
    if len(meaningful) <= max_lines:
        return "\n".join(meaningful)
    test = "\n".join(meaningful[:max_lines]) + f"\n\n_(truncated — {len(meaningful)} lines total)_"
    return test 


output_text = _excerpt(input_text)
print('OUTPUT: \n\n', output_text)
print('****************************************************************************************************')
print('strings')
print('****************************************************************************************************')

# a formatted or f string
name = 'Joe'
age = 50
print(f'My name is {name} and I am {age} years old.')

# common string methods - upper, lower, capitalize
food = 'avocado'
print(food.upper())
print(food.lower())
print(food.capitalize())

# common string methods - split
# splits a string into a list
a = 'a, b, c'
b = a.split()

print(b) # ['a', 'b', 'c']

# replace characters in a string
c = a.replace('a', 'z') # z, b, c
print(c)


print('****************************************************************************************************')
print('control')
print('****************************************************************************************************')

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)


letters = ['a', 'b', 'c']
for letter in letters:
  print(letter)


for a in range(4):
  print(a)

# this is a nested list comprehension; equivalent of an embedded for loop that creates a list
# outer loop is - 'for row in matrix'; inner loop is - 'for number in row'
# prints [0, 1, 2, 3]
matrix = [[0,1], [2,3]]
flat_list = [number for row in matrix for number in row]
print(flat_list)

# prints 0, 1, 2, 3
i = 0
while i <= 3:
    print(i)
    i += 1

# prints Positive
x = 10
if x > 0:
    print('Positive')
elif x == 0:
    print('Zero')
else:
    print('Negative')

print('****************************************************************************************************')
print('math')
print('****************************************************************************************************')

import math
import random

# simple math
print(abs(-5))

# simple math
print(math.sqrt(2))

# seeding will cause random.uniform to always produce the same value
random.seed(42)
print(random.uniform(-1,1))

# sums up an iterable with an optional default start value
print(sum([1.5, 2.5], 1))

print('****************************************************************************************************')
print('import')
print('****************************************************************************************************')

import module
import orchestrator.state as state

# Access a function or variable inside it
result = module.add(1, 1)
print(result)

result = module.subtract(2, 1)
print(result)

result = module._multiply(2, 2)
print(result)

print('****************************************************************************************************')
print('objects')
print('****************************************************************************************************')

# 'is' checks if two names point to the same object in memory
dict1 = {'a': 0}
dict2 = dict1
dict3 = {'a': 0}

# prints True & False
print(dict1 is dict2)
print(dict1 is dict3)

#
# iterable objects - zip
#

# zip takes 2 or more iterables
a = [1,2]
b = ['x','y']
test = zip(a,b)

# output is <zip object at 0x767ef7f77d80>
print(test)

# output is [(1,'x'),(2,'y')]
print(list(test))

print('****************************************************************************************************')
print('classes')
print('****************************************************************************************************')

# python does not have access specifiers
class MySuperClass():

    def __init__(self):
        print("I'm a super class constructor")

    def superMethod(self):
        print("I'm a super class method")

# pass the super class in
class MyClass(MySuperClass):

    # self is required to instantiate
    def __init__(self):

        # calls constructor of the super class
        super().__init__()
        print("I'm a class constructor")

    def method(self):
        print("I'm a class method")

    def _private_method(self):
        print('This is intended to be a private method, but using an underscore is just convention')

Instance = MyClass()
Instance.method()
Instance.superMethod()
Instance._private_method()

from typing import TypedDict, Annotated
from pydantic import BaseModel, Field


# LangGraph uses annotions to pass reducer functions
def _last(a: str, b: str) -> str:
    return b if b else a


# this is a type dictionary used to define Factory State for langraph
class FactoryState(TypedDict):
    ticket_id: Annotated[str, _last]


# here is actual use of an annotation to not just check the type but also the value
class User(BaseModel):
    age: Annotated[int, Field(gt=0, le=120)]


User(age=0)   # raises ValidationError (gt = greater than)
User(age=1)   # valid

print('****************************************************************************************************')
print('classes-add')
print('****************************************************************************************************')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

# each calls the constructor __init__
p1 = Point(1, 2)
p2 = Point(3, 4)

# uses __add__
p4 = p1 + p2
print(p4.x, p4.y)

# self = p1, other = p2, uses add
p3 = p1.add(p2)
print(p3.x, p3.y)  


"""
Demonstrates an asynchronous FastAPI endpoint 
that fetches an HTTPBin response with HTTPX and serves it with Uvicorn.
"""

import httpx
from fastapi import FastAPI
import uvicorn

# the app object follows the ASGI standard and can be passed to uvicorn
app = FastAPI()

# a get request to "/" will call root
@app.get("/")
# with async, root is now a coroutine, a function that can pause itself
async def root():

    # this version requires async but a sync version is available as well
    # the name client is user defined and is what is handed back
    async with httpx.AsyncClient() as client:

        # await only works inside an async function
        # while waiting other coroutines can run
        r = await client.get("https://httpbin.org/delay/1")
    return {"status": r.status_code}

if __name__ == "__main__":
  uvicorn.run(app)

# uvicorn runs on port 8000 by default
# test using - curl http://127.0.0.1:8000/
'''
Class hierarchy for errors

BaseException
├── SystemExit          (sys.exit())
├── KeyboardInterrupt   (Ctrl+C)
├── GeneratorExit
└── Exception           (almost all normal errors)
    ├── ValueError
    ├── ZeroDivisionError
    └── ...
'''

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as e:
    print(f"Something unexpected happened: {e}")
finally:
    print(f"always prints")
"""
Tests the FastAPI endpoint running at http://127.0.0.1:8000/
"""

import httpx

URL = "http://127.0.0.1:8000/"


def main() -> None:
  response = httpx.get(URL, timeout=10.0)
  print("Status code:", response.status_code)
  print("Response JSON:", response.json())


if __name__ == "__main__":
  main()
import asyncio
import httpx

# with async, root is now a coroutine, a function that can pause itself
# after calling root() a coroutine object is returned from root()
async def root():
    # await only works inside an async function
    # while sleeping/paused other coroutines can run
    await asyncio.sleep(2)
    return {"status": 200}

print('waiting ...')

# program will wait for result here
# the coroutine object requires a runner; in this case asyncio.run() to run it
# it is now inside of an event loop
result = asyncio.run(root())
print(result)


async def fetch(client, label, seconds):
    await client.get(f"https://httpbin.org/delay/{seconds}")
    print(f"{label} done")

async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            fetch(client, "A", 3),
            fetch(client, "B", 1),
            fetch(client, "C", 2),
        )

print('waiting ...')

# program will wait for result here
asyncio.run(main())

from pathlib import Path
import threading
import time

_write_lock = threading.Lock()
FILE_PATH = Path("threads.txt")


def append_line(line: str) -> None:
  with _write_lock:
    content = FILE_PATH.read_text() if FILE_PATH.exists() else ""
    FILE_PATH.write_text(content + line + "\n")
    print('line is being written ...')
    time.sleep(1) # simulate a long write_text operation
    print('line is written:', line)


t1 = threading.Thread(target=append_line, args=("from thread 1",))
t2 = threading.Thread(target=append_line, args=("from thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()
# unpack lists
nums = [1, 2, 3]
print(nums)
print(*nums)
combined = [*nums, 4, 5]
print('combined - ', combined)

# unpack dictionaries
defaults = {"color": "red", "size": "M"}
overrides = {"color": "white", "size": "L", "notes": "fine"}
merged = {**defaults, **overrides}
print('merged - ', merged)

# function defenitions - packs instead of unpacks
def f(*args, **kwargs):
    print('packs - arguments and keyed arguments')
    print(args)
    print(kwargs)

f(1, 2, x=3)
print('****************************************************************************************************')
print('hashmap')
print('****************************************************************************************************')

# create
map1 = {
    'name': 'Chris',
    'age': 49
}

# read - Joe
print(map1['name'])

# update or add
map1['city'] = 'Austin'

# check key - True
print('age' in map1)

# iterate
for key, value in map1.items():
    print(key, value)

print('****************************************************************************************************')
print('context management')
print('****************************************************************************************************')

import time

class Timer:
    def __init__(self, name="default name"):
        self.name = name
        self.elapsed = 0.0

    def __enter__(self):
        print(f"[{self.name}] - enter - started...")
        self.start = time.perf_counter()
        return self 

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] - exit - finished in {self.elapsed:.4f} seconds")

with Timer("specific name") as timer:
    time.sleep(1)
    print(f"-> check: {time.perf_counter() - timer.start:.2f}s elapsed")

print(f"total time recorded by object: {timer.elapsed:.4f}s")

print('****************************************************************************************************')
print('decorator')
print('****************************************************************************************************')

def my_decorator(func):
  def wrapper():
      print("--- Before the function runs ---")
      func()
      print("--- After the function runs ---")
  return wrapper

@my_decorator
def say_hello():
  print("Hello!")

say_hello()

print('****************************************************************************************************')
print('files')
print('****************************************************************************************************')

import os
output_file = 'combined.py'
file_count = 1
with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in sorted(os.listdir(".")):
        if os.path.isfile(filename) and filename.endswith('.py') and  filename != output_file:
            with open(filename, 'r', encoding='utf-8') as current_file:
                file_content = current_file.read()
                outfile.write(file_content + '\n')
            file_count += 1

print("\n")
print(f'{output_file} combined {file_count} files')
print("\n")

print('****************************************************************************************************')
print('numpy-dot')
print('****************************************************************************************************')

import numpy as np

# Two vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dot product, output is 1*4 + 2*5 + 3*6 = 32
dot = np.dot(a, b)
print(dot)

print('****************************************************************************************************')
print('numpy-matrix')
print('****************************************************************************************************')

import numpy as np

# Matrix (2x3)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Vector (length 3)
v = np.array([7, 8, 9])

# Matrix-vector multiplication: [50, 122]
result = np.dot(A, v)
print(result)

'''
First row of A: [1, 2, 3]
Dot with v: 1*7 + 2*8 + 3*9 = 50

Second row of A: [4, 5, 6]
Dot with v: 4*7 + 5*8 + 6*9 = 122

So the result is: [50, 122]
'''

print('****************************************************************************************************')
print('CIRQ - HADAMARD GATE')
print('****************************************************************************************************')

import cirq

# place a single qbit named 'qbit' on a 1D line at index 0
# a 1D line represents both physical space and a mental model
qbit = cirq.LineQubit(0)

# creates a quantum circuit ( a series of quantum operations )
circuit = cirq.Circuit(

  # applies the Hadamard gate to the qbit, putting it into a superposition
  cirq.H(qbit),

  # measures qbit and and stores the result in a classical bit `q0`
  cirq.measure(qbit, key='q0')
)

# creates a simulator for quantum circuits so we can run the quantum circuit
sim = cirq.Simulator()

# executes the quantum circuit repetitively and stores the result
result = sim.run(circuit, repetitions=1024)

# one output is Counter({1: 537, 0: 487})
print(result.histogram(key='q0'))

print('****************************************************************************************************')
print('CIRQ - CNOT GATE')
print('****************************************************************************************************')

# place holder 
# CNOT is an entangling gate
# Place 2 on a line
print('****************************************************************************************************')
print('PYTORCH')
print('****************************************************************************************************')

import torch

# not all systems have accessible GPUs
print('cuda is available: ', torch.cuda.is_available())

# tensors - add vectors: z = tensor([5., 7., 9.])
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
z = x + y
print('z =', z)

# z = [5.0, 7.0, 9.0]
print('z =', z.tolist())

# tensors - zeros, ones, add matrices : # c = [[1.0, 1.0], [1.0, 1.0]]
a = torch.zeros((2, 2))
b = torch.ones((2, 2))
c = a + b
print('c =', c.tolist())

print('****************************************************************************************************')
print('PYTORCH - BACKWARD - SCALAR')
print('****************************************************************************************************')

import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
# dy/dx = 2*x + 3

# computes dy/dx and sets .grad for x
y.backward()

# prints 7.
print('dy/dx =', x.grad)

# reset x.grad
# trailing _ is a convention for in place mutations
# calling y.backward() populates x.grad, so we can ignore ty, the real time type checker enabled by replit
x.grad.zero_()

# prints 0.
print('dy/dx =', x.grad)

print('****************************************************************************************************')
print('PYTORCH - BACKWARD - TENSOR')
print('****************************************************************************************************')

import torch

v = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
f = v**2 + 3*v + 1
print(f) # output is: tensor([5., 11., 19.] ...)

f_sum = f.sum()
print(f_sum) # outpus is 5 + 11 + 19 = 35 : tensor(35. ...)

# run backward propagation
# by default, .backward() requires a scalar, and sum is a standard idiom for backward propagation
f_sum.backward()
# df/dv = 2v + 3
print("df/dv =", v.grad) # output is: tensor([5., 7., 9.] ...)

print('****************************************************************************************************')
print('MODULE')
print('****************************************************************************************************')

# this only effects the wild card import - from module import *
__all__ = ["add"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# using undersocre to mark private is only convention but the function is still imported
def _multiply(a, b):
    return a * b

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))

