# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(self, nums: list[int]) -> int:
    dict={}
    for num in nums:
        dict[num]=dict.get(num,0)+1
    for i in dict.keys():
        if dict[i]==1:
            return i
    