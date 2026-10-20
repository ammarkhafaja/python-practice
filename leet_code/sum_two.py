nums = [2,7,11,15]
target = 9

def twoSum(n: list, t: int):
    arr=list()
    for i in range(len(nums)-1):
        j=i+1
        while j<len(nums):
            if nums[i]+nums[j]==t:
                arr.append([i,j])
            j=j+1
    print(arr[0])
twoSum(n=nums, t=target)



