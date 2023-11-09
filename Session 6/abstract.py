from abc import ABC, abstractmethod


# class Generic:
#     def __init__(self, **kwargs) -> None:
#         [setattr(self, key, value) for key, value in kwargs.items()]

#     def __repr__(self) -> str:
#         return ""


class Generic(ABC):
    def __init__(self, **kwargs) -> None:
        [setattr(self, key, value) for key, value in kwargs.items()]

    @abstractmethod
    def __repr__(self) -> str:
        pass 

    def __greet__(self):
        return "Hello from Generic"


class Child(Generic):
    def _my_arttrs(self):
        attr_names = [name for name in dir(self) if not name.startswith("_")]
        attrs = {name: getattr(self, name) for name in attr_names}
        return attrs

    def __repr__(self) -> str:
        return f"{self._my_arttrs()}"


if __name__ == "__main__":
    # child1 = Generic()

    child2 = Child(nums=[1, 3, 6])
    print(child2)
    print(child2.__greet__())
