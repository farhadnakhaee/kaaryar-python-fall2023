def swap(num_list:list, pos1:int, pos2:int):
    num_list[pos1],num_list[pos2] = num_list[pos2], num_list[pos1]
    

    

def qsort3(nums:list, left_index:int=0, right_index:int=None)->None:
    if right_index is None:
        right_index = len(nums)-1
    if left_index >= right_index:
        return 
    print(f"{nums[left_index:right_index+1]}", end="\t")
    pivot = nums[right_index]
    small_index = left_index
    greater_index = left_index
    while greater_index<=right_index:
        if nums[greater_index] < pivot:
            swap(nums, small_index, greater_index)
        greater_index +=1
        if nums[small_index]<pivot:
            small_index +=1
    pivot = nums.pop(right_index)
    nums.insert(small_index, pivot)
    print(f"{nums} ")
    qsort3(nums, left_index=left_index, right_index=small_index-1)
    qsort3(nums, left_index=small_index+1, right_index=right_index)
        

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