# 2 >> 5 >> -4 >> 8
class Node:
    def __init__(self, val):
        self.value = val
    badi = None

    def __repr__(self) -> str:
        if self.badi is None:
            return f"{self.value}"
        else:
            return f"{self.value},{self.badi}"

# node1 = Node(2)
# node1.badi = Node(5)
# node1.badi.badi = Node(-4)

# queue = Node(1234)
# tail = queue
# for i in range(10):
#     tail.badi = Node(i**2)
#     tail = tail.badi
    
    
# print(f"My queue: {queue}")

# while queue is not None:
#     print(f"Now serving {queue.value}")
#     queue = queue.badi

# print(f"After while is run the queue is: {queue}")

q1 = Node(1)
q2 = Node(2)

tail1= q1
tail2= q2
for i in range(1, 5):
    tail1.badi = Node(tail1.value*i)
    tail1=tail1.badi
    tail2.badi = Node(tail2.value**i)
    tail2 = tail2.badi

print(f"q1={q1}")
print(f"q2={q2}")

tail1 = q1
while tail1.badi is not None:
    tail1= tail1.badi

tail1.badi = q2

print(f"q1+q2: {q1}")

q1 = 1, 2, 4 , 9 , 15
q2 = 3, 4, 8, 10, 13

merged = 1,2,3,4,4,8,9,10,13,15















