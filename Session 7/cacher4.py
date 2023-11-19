import time
import functools

@functools.lru_cache(maxsize=5)
def fibonacci(n):
    if n<3:
        time.sleep(5)
        return 1
    else:
        time.sleep(1)
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":

    for i in range(1,10):
        print(f"{i})  {fibonacci(i)}")


    print(f"{1})  {fibonacci(1)}")



