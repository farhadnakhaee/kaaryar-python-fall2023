# 1 .. 100

# If divisible by 3 -> Fiz
#    divisible by 5 -> Buzz
#    divisible by 15 -> FizBuzz

def FizzBuzz(num):
    mod3 = num%3
    mod5 = num%5
    if mod3 and mod5:
        return "num" 
    if mod3==0 and mod5==0:
        return "FizzBuzz"
    if mod3==0:
        return "Fizz"
    if mod5==0:
        return "Buzz"
    # if i%15==0:
    #     return "FizzBuzz"
    # elif i%5 ==0:
    #     return "Buzz"
    # elif i%3==0:
    #     return "Fizz"
    # else:
    #     return i

# for i in range(1, 101):
#     print(FizzBuzz(i))

class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

class FizzBuzzCycle:
    def __init__(self) -> None:
        self.head = Node("num")
        self.current = self.head
        for i in range(2,16):
            self.current.next = Node(
                FizzBuzz(i)
            )

            # if i%(3*5) == 0:
            #     self.current.next = Node("FizzBuzz")
            # elif i%5 == 0:
            #     self.current.next = Node("Buzz")
            # elif i%3 == 0:
            #     self.current.next = Node("Fizz")
            # else:
            #     self.current.next = Node("num")

            self.current = self.current.next

        self.current.next = self.head
        #self.reset()

    def __next__(self)->None:
        self.current = self.current.next

    # def reset(self)->None:
    #     self.current =  self.head

if __name__=="__main__":
    fb = FizzBuzzCycle()

    for i in range(1, 36):
        next(fb)
        if fb.current.label=="num":
            print(i)
        else:
            print(fb.current.label)