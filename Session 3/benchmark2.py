from fibonacci import fibonacci, fibonnaci_generator
from timeit import timeit


if __name__ == "__main__":
    benchmarking_result = timeit(
        "[fibonacci(n) for n in range(20)]",
        setup="from fibonacci import fibonacci",
        number=10_000,
    )
    print(f"Benchmarking run result is: {benchmarking_result}")

    benchmarking_result = timeit(
        "list_with_generator(20)",
        setup="from fibonacci import list_with_generator",
        number=10_000,
    )
    print(f"Benchmarking run result is: {benchmarking_result}")
