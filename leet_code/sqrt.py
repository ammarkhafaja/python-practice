import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0: return 0
        if x<=3:return 1
        k=1
        while k<x:
            if k*k==x:return k
            elif k*k>x:return k-1
            k+=1
