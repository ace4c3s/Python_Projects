# This program returns the indices of two numbers such that they add up to the target

def twoSum(nums,target):
    num_indices = {}
    for index, value in enumerate(nums):
        compliment = target - value
        if compliment in num_indices:
            return [num_indices[compliment],index]
        num_indices[value] = index
    return []

integers = [1,2,3,4]
print(twoSum(integers,5))