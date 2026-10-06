# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3

# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

def convertToTitle(columnNumber: int):
    result = []
    while columnNumber > 0:
        columnNumber -= 1                      # shift to 0-based
        result.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
    return ''.join(reversed(result))
print(convertToTitle(28))

# recursive solution 
def convertToTitle(columnNumber: int) -> str:
    if columnNumber == 0:
        return ""
    columnNumber -= 1
    return convertToTitle(columnNumber // 26) + chr(ord('A') + columnNumber % 26)