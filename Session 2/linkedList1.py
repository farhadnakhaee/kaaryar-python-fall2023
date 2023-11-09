class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

    def extend_list(self, item_list):
        if len(item_list)>0:
            self.next = Item(item_list[0])
            self.next.extend_list(item_list[1:])
    
    def print_list(self):
        print(self.value, end='')
        if self.next != None:
            print(',', end='')
            self.next.print_list()
        else:
            print('')

if __name__ == '__main__':
    head = Item(1)
    head.extend_list([3,4,5,6,7,8])
    head.next.print_list()