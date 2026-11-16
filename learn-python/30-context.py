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
