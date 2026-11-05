# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate( nums: list[int]):
    # dic={}
    # for item in nums:
    #     dic[item]=dic.get(item,0)+1
    #     if dic[item]>1:
    #         return False
    # return True
        return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,4]))