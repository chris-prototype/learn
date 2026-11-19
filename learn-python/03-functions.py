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
