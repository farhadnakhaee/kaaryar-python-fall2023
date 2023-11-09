def qsort_1(nums:list):
    if not nums:
        return []
    else:
        middle_index = len(nums)//2
        middle_element = nums.pop(middle_index)
        smaller_nums = [num for num in nums if num <middle_element]
        gte_nums = [num for num in nums if num >=middle_element]

        sorted_smaller_nums = qsort_1(smaller_nums)
        sorted_gte_nums = qsort_1(gte_nums)


        result = []
        result.extend(sorted_smaller_nums)
        result.append(middle_element)
        result.extend(sorted_gte_nums)

        return result
    
def qsort_2(nums: list)->list:
    if not nums:
        return []
    else:
        middle_index = len(nums)//2
        middle_element = nums.pop(middle_index)
        smaller_nums = []
        gte_nums = []
        for num in nums:
            if num >= middle_element:
                gte_nums.append(num)
            else:
                smaller_nums.append(num)
        return [*qsort_2(smaller_nums),middle_element, *qsort_2(gte_nums)]
        

    
if __name__ == "__main__":
    my_nums = [12,3,6,10,2,1,7,3,9,20,13,12]
    print(my_nums)
    my_sorted_nums = qsort_1(my_nums)

    print(my_nums)
    print(my_sorted_nums)

    my_nums2 = [12,3,6,10,2,1,7,3,9,20,13,12]
    print(my_nums2)
    my_q2_sorted_nums = qsort_2(my_nums2)
    print(my_nums2)
    print(my_q2_sorted_nums)