from typing import Callable


class Myclass:
    def __init__(self, **kwargs):
        [setattr(self, key, value) for key, value in kwargs.items()]


if __name__ == "__main__":
    my_instance = Myclass(a=1, b="Hello", myfunc=lambda x: x * x)
    print(my_instance.b)
    print(dir(my_instance))
    print(
        f"List of callables: {[item for item in dir(my_instance) if isinstance(getattr(my_instance, item), Callable)]}"
    )
    print(my_instance.myfunc(2))
