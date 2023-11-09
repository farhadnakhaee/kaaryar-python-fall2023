# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
# nums = [3,3];target = 6
# nums = [2,7,11,15]
# target=9
# data ={target-x:[ind,x] for ind, x in enumerate(nums)}
# print(data)
# result_dict = {}
# for ind, x in enumerate(nums):
#     complement = result_dict.get(x)
#     if complement is not None:
#         print([complement , ind])
#     else:
#         result_dict[target-x] = ind


# for ind1, i in enumerate(nums):
#     for ind2 in range(ind1+1, len(nums)):
#         j=nums[ind2]
#         if i+j==target:
#             print([ind1,ind2])


mydict = {
    2:[0,9-2],
    7:[1,9-7],
    11:[3,9-11],
    15:[4,9-15]
}

print(mydict.get(-6))