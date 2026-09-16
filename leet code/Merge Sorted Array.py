def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    par1=nums1[:m]
    merge=sorted(par1+nums2[:n])
    nums1[:]=merge