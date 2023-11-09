from linkedList import Item


if __name__ == '__main__':
    list1 = Item(1)
    list1.print_list()
    list1.extend_list([3,8,9,15,21])

    list2 = Item(0)
    list2.extend_list([2,3,8,11,17,43])

    list1.print_list()
    list2.print_list()