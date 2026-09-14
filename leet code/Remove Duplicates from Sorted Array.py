def removeDuplicates(self, nums: List[int]) -> int:
    k=1
    for  n in range (1,len(nums)):
        if not nums:
            return False
        if nums[n]!=nums[k-1]:
            nums[k]=nums[n]
            k+=1
    return k