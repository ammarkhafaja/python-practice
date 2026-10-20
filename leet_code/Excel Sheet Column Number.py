# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
def titleToNumber( columnTitle: str):
    c=1
    res=0
    for ch in reversed(columnTitle):
        num=ord(ch)-64
        res+=num*c
        c*=26
    return res
print(titleToNumber('B'))