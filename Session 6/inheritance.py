class First:
    x=1
    def __init__(self) -> None:
        print("Call inside First")


class Second:
    x=2
    y=10
    def __init__(self) -> None:
        print("Call inside Second")


class Third:
    y=20
    def __init__(self) -> None:
        print("Call inside Third")


class Child(First, Second, Third):
    pass
    # def __init__(self) -> None:
    #     print("Inside Child init: ")
    #     super().__init__()


if __name__ == "__main__":
    child = Child()
    print(child.x, child.y)
