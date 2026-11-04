
def isHappy(n):
    res=set()
    while n!=1:
        if n in res: return False
        res.add(n)
        n=sum(int(ch)**2 for ch in str(n))
    return True 
print(isHappy(2))    