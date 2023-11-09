from fibonacci import fibonacci, fibonnaci_generator
from time import time

if __name__ == "__main__":
    before = time()
    after = time()
    print(f"Time difference = {after-before:15.14f}")

    a = 1
    before = time()
    for _ in range(10_000):
        pass
        # a = 1*a
    after = time()
    print(f"Time difference of summation = {after-before:f}")
