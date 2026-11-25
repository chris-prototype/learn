print('****************************************************************************************************')
print('context management')
print('****************************************************************************************************')

import time

class Timer:
    def __init__(self, name="default name"):
        self.name = name
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        print(f"[{self.name} , {self.start}] - __enter__ ")
        return self 

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed =  self.end - self.start
        print(f"[{self.name}, {self.end}] - __exit__ ")

# only functions, classes, and comprehensions create new scope
# timer is available outside of this block and is an instance of Timer
# note that with wraps a block of code while @ wraps a function so that it is used every funcion call
with Timer("I am name") as timer:
    print(f"-> timer.start: {timer.start}")
    time.sleep(1)
    print(f"-> timer.start: {timer.start}")


print(f"timer.end: {timer.end}")
