def swap(num_list:list, pos1:int, pos2:int):
    num_list[pos1],num_list[pos2] = num_list[pos2], num_list[pos1]

def qsort3(nums:list, left_index:int=0, right_index:int=None)->None:
    if right_index is None:
        right_index = len(nums)-1
    
    if left_index>=right_index:
        return
    
    pivot = nums[right_index]
    smaller_index = left_index
    greater_index = left_index

    while greater_index<right_index:
        if nums[greater_index]<pivot:
            swap(nums, greater_index, smaller_index)
        
        while nums[smaller_index] < pivot:
            smaller_index = smaller_index + 1
    swap(nums, smaller_index, right_index)
    # pivot = nums.pop(right_index)
    # nums.insert(smaller_index, pivot)
    qsort3(nums,smaller_index+1, right_index)
    qsort3(nums, left_index,smaller_index-1 )

    # [3,6,10,2,1,12,7,3,9,12,20,13]
    #                      s
    #                             g
if __name__ == "__main__":
    my_nums = [12,3,6,10,2,1,7,3,9,20,13,12,12]
    # my_nums = [12,3,6,10,2]
    # print(my_nums)
    qsort3(my_nums)

    # print(my_nums)
    # a= [1,2]
    # print(a)
    # swap(a, 0,1)
    # print(a)

# import time
# def quicksort1(nums: list)-> list:
#     numbers = nums.copy()
#     if not numbers:
#         return []
    
#     mid_point_index = len(numbers)//2
#     pivot = numbers.pop(mid_point_index)

#     less_numbers =[num for num in numbers if num<pivot]
#     ge_numbers =[num for num in numbers if num>=pivot]

#     return [ *quicksort1(less_numbers), pivot, *quicksort1(ge_numbers)]

# #     # [12,3,6,10,2,1,7,3,9,20,13,12]
# #     # [12,3,6,10,2,7,3,9,20,13,12]

# if __name__=="__main__":
#     # time.sleep(100)
#     my_nums = [12,3,6,10,2,1,7,3,9,20,13,12]
#     print(my_nums)
#     start = time.time()
#     for _ in range(100_000):
#         sorted = quicksort1(my_nums)
#     end = time.time()
#     print(sorted)
#     print(f"Time taken={(end-start)/1000}")

