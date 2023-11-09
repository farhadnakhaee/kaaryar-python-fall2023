class Node:
    next = None
    def __init__(self, x:list):
        if x:
            self.value = x.pop(0)
            if x:
                self.next = Node(x=x)

    def __repr__(self) -> str:
        if self.next is None:
            return str(self.value)
        else: 
            return f"{self.value},{self.next}"

head1 = Node([1,3,7,9,12])
head2 = Node([2,4,7,11,15])

merge = 1,2,3,4,7,7,9,11,12,15