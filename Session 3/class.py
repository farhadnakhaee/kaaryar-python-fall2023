class Node:
    def __init__(self, num) -> None:
        self.value = num
        self.next = None

    def push(self, x):
        self.next = Node(x)


my_list = Node(1)
my_list.push(10)
