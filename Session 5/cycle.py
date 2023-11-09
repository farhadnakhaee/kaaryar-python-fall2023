class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

class FizzBuzzCycle:
    def __init__(self) -> None:
        self.head = Node("num")
        self.node = self.head
        for i in range(2,16):
            if i%(3*5) == 0:
                self.node.next = Node("FizzBuzz")
            elif i%5 == 0:
                self.node.next = Node("Buzz")
            elif i%3 == 0:
                self.node.next = Node("Fizz")
            else:
                self.node.next = Node("num")

            self.node = self.node.next

        self.node.next = self.head
        self.reset()

    def __next__(self)->None:
        self.node = self.node.next

    def reset(self)->None:
        self.node =  self.head
    

    


if __name__=="__main__":
    fb = FizzBuzzCycle()

    for i in range(13):
        if fb.node.label=="num":
            print(i+1)
        else:
            print(fb.node.label)
        next(fb)    

    fb.reset()
    for i in range(15):
        if fb.node.label=="num":
            print(i+1)
        else:
            print(fb.node.label)
        next(fb)    
