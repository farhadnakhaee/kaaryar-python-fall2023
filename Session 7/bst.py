class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, new_value):
        if self.value is None:
            self.value = new_value
            return 
        
        if new_value<=self.value:
            if self.left is None:
                self.left = Node(new_value)
                return
            self.left.insert(new_value)
            return
        
        if self.right is None:
            self.right = Node(new_value)
            return 
        self.right.insert(new_value)

    def search(self, find_val):
        if self.value==find_val:
            return True
        elif find_val<self.value and self.left is not None:
            return self.left.search(find_val)
        elif find_val>self.value and self.right is not None:
            return self.right.search(find_val)
        return False
        

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
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    print(f"search 4: {tree.search(4)}")
    print(f"search 6: {tree.search(6)}")
