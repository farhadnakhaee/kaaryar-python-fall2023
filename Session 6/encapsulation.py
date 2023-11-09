class Password:
    def set(self, password):
        self._password = password


class Parent:
    __private = "This is a private attribute"
    _protected = "This is a protected attribute"

    def print_private(self):
        print("Parent", self.__private)

    def print_protected(self):
        print("Parent", self._protected)


class Child1(Parent):
    pass


class Child2(Parent):
    def _private_method(self):
        pass

    def print_private(self):
        # print("Child2",self.__private)
        print("Child2", self._Parent__private)

    def print_protected(self):
        print("Child2", self._protected)


if __name__ == "__main__":
    parent = Parent()
    # print(f"Parent dir: {dir(parent)}")
    parent.print_private()
    parent.print_protected()

    child1 = Child1()
    # print(f"Child1 dir: {dir(child1)}")
    child1.print_private()
    child1.print_protected()

    child2 = Child2()
    
    child2.print_private()
    child2.print_protected()

    
