def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        k=0
        for i in range(len(nums)) :
            if nums[i] !=val:
                count +=1
            else:
                k+=1
        while k>0:
            nums.remove(val)
            k-=1