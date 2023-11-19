#               Node  
#         Left        Right 
#     left   right 

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value <= self.value:
            if self.left:
                self.left.insert(new_value)
                return
            elif self.left is None:
                self.left = Node(new_value)
                return 
        if self.right is None:
            self.right = Node(new_value)
            return 
        self.right.insert(new_value)

    def search(self, find_val)-> bool:
        if find_val==self.value:
            return True
        elif find_val<self.value and self.left:
            return self.left.search(find_val)
        elif self.right:
            return self.right.search(find_val)  
        return False
    
    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()





class BST:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insert(self, new_val)->None:
        self.root.insert(new_val) 

    def search(self, find_val):
        return self.root.search(find_val)
    

if __name__ == "__main__":

    tree = BST(4)

    tree.insert(2)
    tree.insert(1000)
    tree.insert(3)
    tree.insert(6)

    print(f"search 1: {tree.search(1)}")
    print(f"search 6: {tree.search(6)}")

    print(f"Min value = {tree.root.find_min()}")
