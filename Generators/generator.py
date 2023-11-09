import random

class RandomShuffle:
    def __init__(self, data) -> None:
        self.data = data.copy()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data)==0:
            raise StopIteration
        index = random.randint(0,len(self.data)-1)
        return self.data.pop(index)


if __name__=="__main__":
    data = list(range(10))
    print(data)
    shuffler = RandomShuffle(data)
    for i in shuffler:
        print(i)

    print(f"After for loop the data left: {shuffler.data}")
    shuffler = RandomShuffle(data)
    print(f"New data: {shuffler.data}")
    print(f"First element: {next(shuffler)}")
    print(f"Using list: {list(shuffler)}")
    shuffler = RandomShuffle(data)
    print("Using * to unpack:", *shuffler)
    print(f"After unpack with *: {shuffler.data}")
