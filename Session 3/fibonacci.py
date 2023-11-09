# [1 1 2 3 5 8 13 21 ...]
# 1. 1
# 2. 1
# 3. 2
# 4. 3


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonnaci_generator():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def list_with_generator(n):
    return [fibonnaci_generator().__next__() for n in range(n)]


if __name__ == "__main__":
    fib_list = [fibonacci(n) for n in range(1, 11)]
    gen = fibonnaci_generator()
    fib_list_gen = [gen.__next__() for n in range(1, 11)]
    print(fib_list)
    print(fib_list_gen)
