def plusOne(self, digits: List[int]) -> List[int]:
    st=""
    for num in digits:
        st+=str(num)
    digits=[]
    num=int(st)
    num=num+1
    st=str(num)
    for ch in st:
        digits.append(int(ch))
    return digits 